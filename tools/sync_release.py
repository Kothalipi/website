#!/usr/bin/env python3
"""Write latest.json and updater.json from published releases.

The site and installers read /latest.json first (same origin, no GitHub API
rate limit). Run this after publishing a release, then commit and push:

    python3 tools/sync_release.py
"""
import json, os, subprocess, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Fetch latest release
out = subprocess.check_output(
    ["gh", "api", "repos/Kothalipi/kothalipi-desktop/releases/latest"], text=True)
j = json.loads(out)

# 2. Fetch all releases to compute download metrics
all_out = subprocess.check_output(
    ["gh", "api", "repos/Kothalipi/kothalipi-desktop/releases"], text=True)
all_releases = json.loads(all_out)

total_downloads = 0
downloads_by_release = {}
for r in all_releases:
    tag = r.get("tag_name", "")
    dl = sum(a.get("download_count", 0) for a in r.get("assets", []))
    downloads_by_release[tag] = dl
    total_downloads += dl

latest_downloads = downloads_by_release.get(j["tag_name"], 0)

slim = {
    "tag_name": j["tag_name"],
    "published_at": j["published_at"],
    "total_downloads": total_downloads,
    "release_downloads": latest_downloads,
    "downloads_by_release": downloads_by_release,
    # name -> sha256, so the installers can verify a download before running it.
    "sha256": {
        a["name"]: a["digest"].split(":", 1)[1]
        for a in j["assets"]
        if a.get("digest", "").startswith("sha256:")
    },
    "assets": [
        {
            "name": a["name"],
            "size": a["size"],
            "download_count": a.get("download_count", 0),
            "browser_download_url": a["browser_download_url"]
        }
        for a in j["assets"]
    ],
}

with open(os.path.join(ROOT, "latest.json"), "w") as f:
    json.dump(slim, f, indent=1)
    f.write("\n")

print(f"latest.json -> {slim['tag_name']} ({len(slim['assets'])} assets, {total_downloads} total downloads)")

# 3. If latest release contains a Tauri updater latest.json asset, download and mirror it to updater.json
updater_asset = next((a for a in j["assets"] if a["name"] == "latest.json"), None)
if updater_asset:
    url = updater_asset["browser_download_url"]
    updater_path = os.path.join(ROOT, "updater.json")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Kothalipi-Sync"})
        with urllib.request.urlopen(req) as resp, open(updater_path, "wb") as out_f:
            out_f.write(resp.read())
        print(f"updater.json -> synced from release asset {url}")
    except Exception as e:
        print(f"Failed to fetch updater latest.json: {e}")

