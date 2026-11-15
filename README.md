# kothalipi.tashanto.com

Website for [Kothalipi](https://github.com/Kothalipi/kothalipi), open-source voice typing
for Bangla, English and Banglish.

Plain HTML, CSS and JS. No build step. Hosted on GitHub Pages.

```bash
python3 -m http.server 4321   # then open http://localhost:4321
```

- `index.html`: page content (English) with `data-i18n` keys
- `main.js`: Bangla translations (`BN`), language toggle, hold-to-speak preview
- `style.css`: brand colors (#006A4E, #F42A41), light/dark, responsive
