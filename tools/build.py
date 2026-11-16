#!/usr/bin/env python3
"""Build the Kothalipi website (static HTML, no dependencies).

    python3 tools/build.py            # writes pages into the repo root
    python3 tools/serve.py            # preview at http://localhost:4321
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import lib  # noqa: E402

lib.OUT = ROOT

import content  # noqa: E402
import home  # noqa: E402

home.home("en")
home.home("bn")
home.download("en")
home.download("bn")
content.models()
content.changelog()
content.about()
content.privacy()
content.guides()
content.docs()
content.not_found()

# ---- sitemap, robots, manifest, llms.txt
S = lib.SITE
urls = []
for p in sorted(lib.PAGES, key=lambda x: (-float(x["priority"]), x["path"])):
    loc = S + p["path"]
    alts = "".join(
        f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{S + u}"/>' for l, u in p["alt"].items()
    )
    if alts:
        alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{S + p["alt"]["en"]}"/>'
    urls.append(
        f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lib.UPDATED}</lastmod>\n    <changefreq>{p["changefreq"]}</changefreq>\n    <priority>{p["priority"]}</priority>{alts}\n  </url>'
    )
lib.write(
    "sitemap.xml",
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    + "\n".join(urls)
    + "\n</urlset>\n",
)
lib.write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {S}/sitemap.xml\n")
lib.write(
    "site.webmanifest",
    '{\n  "name": "Kothalipi",\n  "short_name": "Kothalipi",\n  "description": "Free Bangla and English voice typing",\n  "start_url": "/",\n  "display": "browser",\n  "background_color": "#faf9f6",\n  "theme_color": "#006a4e",\n  "icons": [\n    {"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"},\n    {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"}\n  ]\n}\n',
)
lib.write(
    "llms.txt",
    f"""# Kothalipi

> Kothalipi (কথালিপি) is free, open-source voice typing for Bangla and English on macOS, Windows and Linux. Hold a key, speak, and the text appears in any app. It works offline with Bangla-trained models, or in the cloud with the user's own Google Gemini or OpenAI key, with automatic fallback to offline. Made by TA Shanto (https://tashanto.com). MIT licensed.

## Key facts
- Languages: Bangla and English (one hotkey per language)
- Platforms: macOS 10.15+, Windows 10/11, Linux (Android and iOS planned)
- Offline models: Qwen3-ASR 0.6B Bangla, Bengali.AI Whisper Medium; English: Parakeet 0.6B, Whisper Small/Base
- Cloud engines (user's own key): Google Gemini, OpenAI. Claude has no audio input.
- Privacy: no account, no analytics, no servers; offline audio never leaves the computer

## Pages
- [Home]({S}/): overview and demo
- [Download]({S}/download): installers and one-line terminal install
- [Models and accuracy]({S}/models): models, sizes, licenses, device picks
- [Guides]({S}/guides/): Bangla voice typing on Mac, Windows, Linux; free Gemini API key
- [Docs]({S}/docs/): getting started, keys, cloud, per-OS guides, troubleshooting
- [Privacy]({S}/privacy)
- [Source code]({lib.DESK})
""",
)
print(f"built {len(lib.PAGES)} indexable pages")
