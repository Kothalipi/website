# kothalipi.tashanto.com

Website for [Kothalipi](https://github.com/Kothalipi/kothalipi), open-source voice typing
for Bangla, English and Banglish.

Plain HTML, CSS and JS. No build step. Hosted on GitHub Pages.

```bash
python3 -m http.server 4321   # then open http://localhost:4321
```

| Path | What |
|---|---|
| `index.html` | Home (English, with a Bangla toggle via `data-i18n` keys) |
| `download.html` | Download page: picks the right file for your OS from the latest GitHub release |
| `docs/` | Getting started, keys, cloud keys, macOS, Windows, Linux, troubleshooting |
| `privacy.html`, `404.html` | Privacy notice, not-found page |
| `install.sh` | `curl -fsSL https://kothalipi.tashanto.com/install.sh \| sh` (macOS, Linux) |
| `install.ps1` | `irm https://kothalipi.tashanto.com/install.ps1 \| iex` (Windows) |
| `main.js` | Bangla translations (`BN`), demo, copy buttons, release lookup |
| `style.css` | Brand colors (#006A4E, #F42A41), light/dark, responsive |
