#!/usr/bin/env python3
"""Write latest.json from the newest published release.

The site and installers read /latest.json first (same origin, no GitHub API
rate limit). Run this after publishing a release, then commit and push:

    python3 tools/sync_release.py
"""
import json, os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = subprocess.check_output(
    ["gh", "api", "repos/Kothalipi/kothalipi-desktop/releases/latest"], text=True)
j = json.loads(out)
slim = {
    "tag_name": j["tag_name"],
    "published_at": j["published_at"],
    # name -> sha256, so the installers can verify a download before running it.
    "sha256": {
        a["name"]: a["digest"].split(":", 1)[1]
        for a in j["assets"]
        if a.get("digest", "").startswith("sha256:")
    },
    "assets": [
        {"name": a["name"], "size": a["size"], "browser_download_url": a["browser_download_url"]}
        for a in j["assets"]
    ],
}
with open(os.path.join(ROOT, "latest.json"), "w") as f:
    json.dump(slim, f, indent=1)
    f.write("\n")
print("latest.json ->", slim["tag_name"], len(slim["assets"]), "assets")
