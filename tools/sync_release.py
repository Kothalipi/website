#!/usr/bin/env python3
"""Write latest.json and updater.json from published releases (Desktop + Mobile).

Run this after publishing a release, then commit and push:
    python3 tools/sync_release.py
"""
import json, os, subprocess, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def gh_json(endpoint):
    out = subprocess.check_output(["gh", "api", endpoint], text=True)
    return json.loads(out)

is_app = lambda n: not n.endswith((".sig", ".json"))

# 1. Fetch latest desktop release + all desktop & mobile releases
j = gh_json("repos/Kothalipi/kothalipi-desktop/releases/latest")
desk_releases = gh_json("repos/Kothalipi/kothalipi-desktop/releases?per_page=100")
mob_releases = gh_json("repos/Kothalipi/kothalipi-mobile/releases?per_page=100")

desktop_downloads = 0
downloads_by_release = {}
for r in desk_releases:
    tag = r.get("tag_name", "")
    dl = sum(a.get("download_count", 0) for a in r.get("assets", []) if is_app(a.get("name", "")))
    downloads_by_release[tag] = dl
    desktop_downloads += dl

android_downloads = 0
ios_downloads = 0
for r in mob_releases:
    for a in r.get("assets", []):
        name = a.get("name", "").lower()
        cnt = a.get("download_count", 0)
        if name.endswith(".apk"):
            android_downloads += cnt
        elif name.endswith(".ipa"):
            ios_downloads += cnt

mobile_downloads = android_downloads + ios_downloads
total_downloads = desktop_downloads + mobile_downloads
latest_downloads = downloads_by_release.get(j["tag_name"], 0)

slim = {
    "tag_name": j["tag_name"],
    "published_at": j["published_at"],
    "total_downloads": total_downloads,
    "desktop_downloads": desktop_downloads,
    "mobile_downloads": mobile_downloads,
    "android_downloads": android_downloads,
    "ios_downloads": ios_downloads,
    "release_downloads": latest_downloads,
    "downloads_by_release": downloads_by_release,
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
    json.dump(slim, f, indent=2)
    f.write("\n")

print(
    f"latest.json -> {slim['tag_name']} (total={total_downloads}, desktop={desktop_downloads}, "
    f"mobile={mobile_downloads} [android={android_downloads}, ios={ios_downloads}])"
)

# 2. Mirror Tauri updater latest.json asset to updater.json
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
