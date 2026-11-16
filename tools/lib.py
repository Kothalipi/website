"""Layout, SEO and helpers for the Kothalipi static site generator."""
import html
import json
import os

SITE = "https://kothalipi.tashanto.com"
GH = "https://github.com/Kothalipi"
SUPPORT = "https://www.supportkori.com/iamtashanto"
DESK = f"{GH}/kothalipi-desktop"
MAKER = "https://tashanto.com"
UPDATED = "2026-11-16"
VERSION = "0.1.0"

INSTALL_SH = "curl -fsSL https://kothalipi.tashanto.com/install.sh | sh"
INSTALL_PS = "irm https://kothalipi.tashanto.com/install.ps1 | iex"

ICON = {
    "check": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m4 10.5 4 4 8-9"/></svg>',
    "download": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 3v10m0 0-4-4m4 4 4-4M4 16h12"/></svg>',
    "menu": '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h14M3 10h14M3 14h14"/></svg>',
}

OUT = None  # set by build.py


def esc(s):
    return html.escape(s, quote=True)


def code(cmd, label=None):
    lab = f'<div class="code-label">{label}</div>' if label else ""
    return f'{lab}<div class="code"><pre>{html.escape(cmd)}</pre></div>'


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# Every generated page is recorded for the sitemap.
PAGES = []


def abs_url(path):
    return SITE + path


NAV = {
    "en": [("/#features", "Features", "features"), ("/models", "Models", "models"), ("/guides/", "Guides", "guides"), ("/docs/", "Docs", "docs"), ("/download", "Download", "download")],
    "bn": [("/bn/#features", "ফিচার", "features"), ("/models", "মডেল", "models"), ("/guides/", "গাইড", "guides"), ("/docs/", "ডকুমেন্টেশন", "docs"), ("/bn/download", "ডাউনলোড", "download")],
}
FOOT = {
    "en": {
        "tag": "Free, open-source Bangla and English voice typing for Mac, Windows and Linux.",
        "product": "Product", "guides": "Guides", "project": "Project",
        "links": {
            "product": [("/download", "Download"), ("/models", "Models & accuracy"), ("/docs/cloud", "Cloud & API keys"), ("/changelog", "Changelog")],
            "guides": [("/guides/bangla-voice-typing-mac", "Bangla voice typing on Mac"), ("/guides/bangla-voice-typing-windows", "On Windows"), ("/guides/bangla-voice-typing-linux", "On Linux"), ("/guides/free-gemini-api-key", "Free Gemini API key")],
            "project": [("/about", "About"), ("/privacy", "Privacy"), (DESK, "Source code"), (DESK + "/blob/main/NOTICE.md", "Credits"), (SUPPORT, "Support the project")],
        },
        "made": f'Made in Bangladesh 🇧🇩 by <a href="{MAKER}">TA Shanto</a>',
        "lic": "MIT licensed",
    },
    "bn": {
        "tag": "ম্যাক, উইন্ডোজ ও লিনাক্সের জন্য ফ্রি, ওপেন সোর্স বাংলা ও ইংরেজি ভয়েস টাইপিং।",
        "product": "প্রোডাক্ট", "guides": "গাইড", "project": "প্রজেক্ট",
        "links": {
            "product": [("/bn/download", "ডাউনলোড"), ("/models", "মডেল ও নির্ভুলতা"), ("/docs/cloud", "ক্লাউড ও API কি"), ("/changelog", "পরিবর্তনের তালিকা")],
            "guides": [("/guides/bangla-voice-typing-mac", "ম্যাকে বাংলা ভয়েস টাইপিং"), ("/guides/bangla-voice-typing-windows", "উইন্ডোজে"), ("/guides/bangla-voice-typing-linux", "লিনাক্সে"), ("/guides/free-gemini-api-key", "ফ্রি Gemini API কি")],
            "project": [("/about", "পরিচিতি"), ("/privacy", "প্রাইভেসি"), (DESK, "সোর্স কোড"), (DESK + "/blob/main/NOTICE.md", "কৃতজ্ঞতা"), (SUPPORT, "প্রজেক্টকে সাপোর্ট করুন")],
        },
        "made": f'বাংলাদেশে <a href="{MAKER}">TA Shanto</a>-র তৈরি 🇧🇩',
        "lic": "MIT লাইসেন্স",
    },
}


def page(path, title, desc, body, *, lang="en", current="", alt=None, og="/assets/og.png",
         og_alt="Kothalipi: speak Bangla or English, and it is written in any app", schema=None,
         noindex=False, body_class="", changefreq="monthly", priority="0.6", preload=None):
    """Render one page. `path` is the clean URL ('/', '/download', '/docs/macos')."""
    canonical = abs_url(path)
    alt = alt or {}
    hreflangs = ""
    if alt:
        for code_, url in alt.items():
            hreflangs += f'<link rel="alternate" hreflang="{code_}" href="{abs_url(url)}">\n  '
        hreflangs += f'<link rel="alternate" hreflang="x-default" href="{abs_url(alt.get("en", path))}">\n  '
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1"
    og_locale = "bn_BD" if lang == "bn" else "en_US"
    og_url = abs_url(og)
    switch_href = alt.get("bn" if lang == "en" else "en") or ("/bn/" if lang == "en" else "/")
    switch_label = "বাংলা" if lang == "en" else "English"
    switch_lang = "bn" if lang == "en" else "en"
    def nav_link(h, t, k):
        cur = ' aria-current="page"' if current == k else ""
        return f'<a href="{h}"{cur}>{esc(t)}</a>'

    links = "".join(nav_link(h, t, k) for h, t, k in NAV[lang])
    dl_href = "/download" if lang == "en" else "/bn/download"
    dl_text = "Download" if lang == "en" else "ডাউনলোড"
    home = "/" if lang == "en" else "/bn/"
    f = FOOT[lang]

    def col(key):
        return "".join(
            f'<li><a href="{h}">{esc(t)}</a></li>' for h, t in f["links"][key]
        )

    pre = "".join(f'<link rel="preload" href="{p}" as="font" type="font/woff2" crossorigin>' for p in (preload or []))
    schema_html = "\n  ".join(ld(s) for s in (schema or []))
    out = f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="robots" content="{robots}">
  <meta name="theme-color" content="#006a4e">
  <meta name="author" content="TA Shanto">
  <link rel="canonical" href="{canonical}">
  {hreflangs}<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta property="og:type" content="{"website" if not path.startswith("/guides/") or path == "/guides/" else "article"}">
  <meta property="og:site_name" content="Kothalipi">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_url}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{esc(og_alt)}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{og_url}">
  {pre}
  <link rel="stylesheet" href="/assets/fonts/fonts.css">
  <link rel="stylesheet" href="/style.css">
  {schema_html}
</head>
<body class="{body_class}{" bn" if lang == "bn" else ""}">
  <a class="skip" href="#main">{"Skip to content" if lang == "en" else "মূল অংশে যান"}</a>
  <header class="nav">
    <div class="container nav-inner">
      <a class="brand" href="{home}" aria-label="Kothalipi home"><img src="/assets/kothalipi-mark.svg" alt="" width="30" height="31">Kothalipi</a>
      <nav class="links" aria-label="Main">{links}</nav>
      <div class="nav-actions">
        <a class="lang-switch" href="{switch_href}" hreflang="{switch_lang}" lang="{switch_lang}">{switch_label}</a>
        <a class="btn btn-primary btn-sm" href="{dl_href}">{dl_text}</a>
        <button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false">{ICON["menu"]}</button>
      </div>
    </div>
  </header>
  <main id="main">
{body}
  </main>
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="brand" href="{home}"><img src="/assets/kothalipi-mark.svg" alt="" width="26" height="27">Kothalipi</a>
          <p>{f["tag"]}</p>
        </div>
        <div><h4>{f["product"]}</h4><ul>{col("product")}</ul></div>
        <div><h4>{f["guides"]}</h4><ul>{col("guides")}</ul></div>
        <div><h4>{f["project"]}</h4><ul>{col("project")}</ul></div>
      </div>
      <div class="footer-bottom"><span>{f["made"]}</span><span>{f["lic"]} · © 2026 TA Shanto</span></div>
    </div>
  </footer>
  <script src="/main.js" defer></script>
</body>
</html>
"""
    # file location: '/x' -> x.html, '/x/' -> x/index.html, '/' -> index.html
    if path.endswith("/"):
        file = path.lstrip("/") + "index.html"
    else:
        file = path.lstrip("/") + ".html"
    write(file, out)
    if not noindex:
        PAGES.append({"path": path, "alt": alt, "changefreq": changefreq, "priority": priority})


def crumbs(items):
    """items: [(path, label), ...] ending at the current page. Returns (html, schema)."""
    parts = []
    for i, (p, label) in enumerate(items):
        parts.append(f'<a href="{p}">{esc(label)}</a>' if i < len(items) - 1 else esc(label))
    html_ = '<nav class="crumbs" aria-label="Breadcrumb">' + " / ".join(parts) + "</nav>"
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": label, "item": abs_url(p)} for i, (p, label) in enumerate(items)
        ],
    }
    return html_, schema


PERSON = {"@type": "Person", "name": "TA Shanto", "url": MAKER}
ORG = {"@type": "Organization", "name": "Kothalipi", "url": SITE, "logo": SITE + "/assets/icon-512.png", "founder": PERSON, "sameAs": [GH, DESK]}


def app_schema(lang="en"):
    return {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "Kothalipi",
        "alternateName": "কথালিপি",
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "macOS, Windows, Linux",
        "softwareVersion": VERSION,
        "description": "Free, open-source Bangla and English voice typing. Hold a key, speak, and text appears in any app. Works offline, with optional Gemini or OpenAI cloud.",
        "inLanguage": ["bn", "en"],
        "url": SITE + "/",
        "downloadUrl": SITE + "/download",
        "license": "https://opensource.org/licenses/MIT",
        "isAccessibleForFree": True,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "availability": "https://schema.org/InStock"},
        "author": PERSON,
        "publisher": ORG,
        "image": SITE + "/assets/og.png",
        "screenshot": [SITE + "/assets/screens/voices.webp", SITE + "/assets/screens/listen.webp"],
        "featureList": [
            "Bangla and English dictation in any app",
            "One hotkey per language",
            "Offline mode with Bangla-trained models",
            "Optional Google Gemini and OpenAI cloud with automatic fallback",
            "Device-aware model recommendations",
        ],
    }


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "name": "Kothalipi", "url": SITE + "/", "inLanguage": ["en", "bn"], "publisher": ORG}


def faq_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items
        ],
    }


def article_schema(title, desc, path):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "mainEntityOfPage": abs_url(path),
        "image": SITE + "/assets/og.png",
        "datePublished": UPDATED,
        "dateModified": UPDATED,
        "author": PERSON,
        "publisher": ORG,
        "inLanguage": "en",
    }


def faq_html(items):
    return "".join(f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in items)
