#!/bin/sh
# Kothalipi installer for macOS and Linux.
#
#   curl -fsSL https://kothalipi.tashanto.com/install.sh | sh
#
# Downloads the latest release from github.com/Kothalipi/kothalipi-desktop
# and installs it:
#   macOS  → /Applications/Kothalipi.app (or ~/Applications if not writable)
#   Linux  → .deb (apt) or .rpm (dnf/zypper) when available, else an AppImage
#            in ~/.local/bin with a menu entry.
set -eu

REPO="Kothalipi/kothalipi-desktop"
API="https://kothalipi.tashanto.com/latest.json"
API_FALLBACK="https://api.github.com/repos/$REPO/releases/latest"

say() { printf '\033[1;32m==>\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33mwarning:\033[0m %s\n' "$*" >&2; }
die() { printf '\033[1;31merror:\033[0m %s\n' "$*" >&2; exit 1; }

need() { command -v "$1" >/dev/null 2>&1 || die "'$1' is required but not installed."; }
need curl
need uname

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

OS=$(uname -s)
ARCH=$(uname -m)

say "Finding the latest Kothalipi release"
RELEASE_JSON=$(curl -fsSL "$API" 2>/dev/null || curl -fsSL -H "Accept: application/vnd.github+json" "$API_FALLBACK") ||
  die "Couldn't reach GitHub. Check your internet connection."

# Print the download URL of the first asset whose name ends with $1.
asset_url() {
  printf '%s' "$RELEASE_JSON" |
    grep -o '"browser_download_url": *"[^"]*"' |
    sed 's/.*"\(https[^"]*\)"/\1/' |
    grep -E "$1\$" | head -n 1
}

sha256_of() {
  if command -v shasum >/dev/null 2>&1; then shasum -a 256 "$1" | cut -d' ' -f1
  elif command -v sha256sum >/dev/null 2>&1; then sha256sum "$1" | cut -d' ' -f1
  else echo ""; fi
}

download() {
  url=$1
  out=$2
  name=$(basename "$url")
  say "Downloading $name"
  curl -fL --progress-bar -o "$out" "$url" || die "Download failed: $url"
  # Check the file against the published SHA-256 before anything runs it.
  expected=$(printf '%s' "$RELEASE_JSON" | grep -o "\"$name\": *\"[0-9a-f]\{64\}\"" | grep -o '[0-9a-f]\{64\}' | head -n 1 || true)
  if [ -n "$expected" ]; then
    actual=$(sha256_of "$out")
    if [ -z "$actual" ]; then
      warn "Can't verify the download (no shasum or sha256sum on this system)."
    elif [ "$actual" != "$expected" ]; then
      rm -f "$out"
      die "Checksum mismatch for $name. The download was not installed."
    else
      say "Checksum verified"
    fi
  else
    warn "No published checksum for $name; installing without verifying it."
  fi
}

install_macos() {
  case "$ARCH" in
    arm64) pattern='_aarch64\.dmg' ;;
    x86_64) pattern='_x64\.dmg' ;;
    *) die "Unsupported Mac architecture: $ARCH" ;;
  esac
  url=$(asset_url "$pattern")
  [ -n "$url" ] || die "No macOS download found in the latest release."
  download "$url" "$TMP/Kothalipi.dmg"

  mnt="$TMP/mnt"
  mkdir -p "$mnt"
  hdiutil attach -nobrowse -quiet -mountpoint "$mnt" "$TMP/Kothalipi.dmg" ||
    die "Couldn't open the disk image."
  app=$(find "$mnt" -maxdepth 1 -name '*.app' | head -n 1)
  [ -n "$app" ] || { hdiutil detach -quiet "$mnt"; die "The disk image has no app."; }

  dest="/Applications"
  [ -w "$dest" ] || dest="$HOME/Applications"
  mkdir -p "$dest"
  if pgrep -x kothalipi >/dev/null 2>&1; then
    say "Closing the running Kothalipi"
    osascript -e 'quit app "Kothalipi"' >/dev/null 2>&1 || true
    sleep 1
  fi
  rm -rf "$dest/Kothalipi.app"
  say "Installing to $dest"
  ditto "$app" "$dest/Kothalipi.app"
  hdiutil detach -quiet "$mnt" || true

  # Downloaded with curl, so macOS hasn't quarantined it; clear it anyway in
  # case the app was copied from somewhere that did.
  xattr -dr com.apple.quarantine "$dest/Kothalipi.app" 2>/dev/null || true

  say "Kothalipi is installed. Opening it…"
  open "$dest/Kothalipi.app" || true
  cat <<'EOF'

Next: allow Microphone and Accessibility when Kothalipi asks.
Guide: https://kothalipi.tashanto.com/docs/macos.html
EOF
}

sudo_cmd() {
  if [ "$(id -u)" -eq 0 ]; then "$@"; else
    command -v sudo >/dev/null 2>&1 || die "Installing needs root (sudo not found)."
    sudo "$@"
  fi
}

install_appimage() {
  url=$(asset_url "$1")
  [ -n "$url" ] || die "No AppImage found in the latest release."
  bin="$HOME/.local/bin"
  mkdir -p "$bin" "$HOME/.local/share/applications"
  download "$url" "$bin/Kothalipi.AppImage"
  chmod +x "$bin/Kothalipi.AppImage"
  cat >"$HOME/.local/share/applications/kothalipi.desktop" <<EOF
[Desktop Entry]
Name=Kothalipi
Comment=Voice typing in Bangla and English
Exec=$bin/Kothalipi.AppImage
Terminal=false
Type=Application
Categories=Utility;Accessibility;
EOF
  say "Installed to $bin/Kothalipi.AppImage (find Kothalipi in your app menu)"
  case ":$PATH:" in *":$bin:"*) ;; *) warn "$bin is not on your PATH." ;; esac
}

install_linux() {
  case "$ARCH" in
    x86_64 | amd64) deb='_amd64\.deb'; rpm='\.x86_64\.rpm'; appimage='_amd64\.AppImage' ;;
    aarch64 | arm64) deb='_arm64\.deb'; rpm='\.aarch64\.rpm'; appimage='_aarch64\.AppImage' ;;
    *) die "Unsupported Linux architecture: $ARCH" ;;
  esac

  if command -v apt-get >/dev/null 2>&1 && [ -n "$(asset_url "$deb")" ]; then
    download "$(asset_url "$deb")" "$TMP/kothalipi.deb"
    say "Installing with apt (may ask for your password)"
    sudo_cmd apt-get install -y "$TMP/kothalipi.deb"
  elif command -v dnf >/dev/null 2>&1 && [ -n "$(asset_url "$rpm")" ]; then
    download "$(asset_url "$rpm")" "$TMP/kothalipi.rpm"
    say "Installing with dnf (may ask for your password)"
    sudo_cmd dnf install -y "$TMP/kothalipi.rpm"
  elif command -v zypper >/dev/null 2>&1 && [ -n "$(asset_url "$rpm")" ]; then
    download "$(asset_url "$rpm")" "$TMP/kothalipi.rpm"
    say "Installing with zypper (may ask for your password)"
    sudo_cmd zypper --non-interactive install --allow-unsigned-rpm "$TMP/kothalipi.rpm"
  else
    install_appimage "$appimage"
    return
  fi
  say "Kothalipi is installed. Find it in your app menu."
  if [ "${XDG_SESSION_TYPE:-}" = "wayland" ]; then
    warn "Wayland: install 'wtype' (or ydotool) so Kothalipi can type into apps."
    echo "Guide: https://kothalipi.tashanto.com/docs/linux.html"
  fi
}

case "$OS" in
  Darwin) install_macos ;;
  Linux) install_linux ;;
  *) die "This installer is for macOS and Linux. On Windows, see https://kothalipi.tashanto.com/download.html" ;;
esac
