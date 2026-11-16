# kothalipi.tashanto.com

Website for [Kothalipi](https://github.com/Kothalipi/kothalipi-desktop): free, open-source Bangla and
English voice typing. Static HTML on GitHub Pages, no frameworks, no tracking, fonts self-hosted.

## Edit and preview

Pages are generated from `tools/*.py`. Edit the Python, then:

```bash
python3 tools/build.py     # writes the HTML, sitemap.xml, robots.txt, llms.txt
python3 tools/check.py     # SEO and link checks (titles, descriptions, canonicals, JSON-LD, links)
python3 tools/serve.py     # preview at http://localhost:4321 (clean URLs like /download work)
```

| Path | What |
|---|---|
| `tools/lib.py` | Layout, navigation, footer, SEO head, JSON-LD helpers |
| `tools/home.py` | Home and download pages, English and Bangla (`/bn/`) |
| `tools/content.py` | Models, changelog, about, privacy, guides, docs, 404 |
| `tools/build.py` | Runs everything and writes sitemap, robots, manifest |
| `style.css`, `main.js` | Design system and small enhancements (site works without JS) |
| `install.sh`, `install.ps1` | Terminal installers, served from the site root |
| `assets/` | Logo, icons, app screenshots (WebP), self-hosted Hind Siliguri, OG image |

## SEO

- One H1, unique title and description per page, canonical URLs, Open Graph and Twitter cards
- Real Bangla pages (`/bn/`, `/bn/download`) with `hreflang` alternates, not a JavaScript toggle
- JSON-LD: SoftwareApplication, WebSite, FAQPage, Article, BreadcrumbList
- `sitemap.xml` with alternates, `robots.txt`, `llms.txt`, web manifest

After the first deploy, add the site in Google Search Console and Bing Webmaster Tools and submit
`https://kothalipi.tashanto.com/sitemap.xml`.

## Screenshots

App screenshots come from the desktop repo's browser preview (`bun run dev`, open `/?mock&onboarding&step=voices`).
