# Kothalipi installer for Windows.
#
#   irm https://kothalipi.tashanto.com/install.ps1 | iex
#
# Downloads the latest installer from github.com/Kothalipi/kothalipi-desktop
# and runs it. No admin rights needed: it installs for the current user.

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'  # much faster Invoke-WebRequest

$Repo = 'Kothalipi/kothalipi-desktop'
$Api = "https://api.github.com/repos/$Repo/releases/latest"

function Say($msg) { Write-Host "==> $msg" -ForegroundColor Green }

$arch = if ($env:PROCESSOR_ARCHITECTURE -eq 'ARM64') { 'arm64' } else { 'x64' }

Say 'Finding the latest Kothalipi release'
try {
    $release = Invoke-RestMethod -Uri $Api -Headers @{ Accept = 'application/vnd.github+json' }
} catch {
    throw "Couldn't reach GitHub. Check your internet connection."
}

$asset = $release.assets | Where-Object { $_.name -like "*_$arch-setup.exe" } | Select-Object -First 1
if (-not $asset) { throw "No Windows ($arch) installer found in the latest release." }

$installer = Join-Path $env:TEMP $asset.name
Say "Downloading $($asset.name)"
Invoke-WebRequest -Uri $asset.browser_download_url -OutFile $installer

Say 'Installing Kothalipi'
# /S = silent NSIS install for the current user.
$p = Start-Process -FilePath $installer -ArgumentList '/S' -Wait -PassThru
Remove-Item $installer -ErrorAction SilentlyContinue
if ($p.ExitCode -ne 0) { throw "The installer exited with code $($p.ExitCode)." }

$exe = Get-ChildItem "$env:LOCALAPPDATA\Kothalipi", "$env:LOCALAPPDATA\Programs\Kothalipi" -Filter '*.exe' -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -notlike 'uninstall*' } | Select-Object -First 1
if ($exe) {
    Say 'Kothalipi is installed. Opening it...'
    Start-Process $exe.FullName
} else {
    Say 'Kothalipi is installed. Open it from the Start menu.'
}
Write-Host ''
Write-Host 'Guide: https://kothalipi.tashanto.com/docs/windows.html'
