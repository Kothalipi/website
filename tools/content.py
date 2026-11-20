"""Models, changelog, about, privacy, guides, docs and 404 pages (English)."""
from lib import *  # noqa: F401,F403


def wide_page(path, title, desc, body_html, *, current="", crumb_items=None, schema_extra=None, article=False, changefreq="monthly", priority="0.6", meta=None):
    schema = list(schema_extra or [])
    cr = ""
    if crumb_items:
        cr, bc = crumbs(crumb_items)
        schema.append(bc)
    if article:
        schema.append(article_schema(title, desc, path))
    meta_html = f'<p class="meta">{meta}</p>' if meta else ""
    body = f'<article class="container doc wide">{cr}{body_html.replace("<!--META-->", meta_html)}</article>'
    page(path, title, desc, body, current=current, schema=schema, changefreq=changefreq, priority=priority)


RELATED = [
    ("/guides/bangla-voice-typing-mac", "Bangla voice typing on a Mac"),
    ("/guides/bangla-voice-typing-windows", "Bangla voice typing on Windows"),
    ("/guides/bangla-voice-typing-linux", "Bangla voice typing on Linux"),
    ("/guides/free-gemini-api-key", "Get a free Gemini API key for Bangla"),
]


def related(exclude):
    items = "".join(f'<a class="card" href="{p}"><h3>{esc(t)}</h3></a>' for p, t in RELATED if p != exclude)
    return f'<h2>Keep reading</h2><div class="cards">{items}</div>'


def guides():
    # ---------------------------------------------------------------- Mac
    p = "/guides/bangla-voice-typing-mac"
    t = "How to Type Bangla with Your Voice on a Mac (Free)"
    d = "Set up free Bangla voice typing on macOS with Kothalipi: install, allow Microphone and Accessibility, download the Bangla model, and fix key conflicts."
    wide_page(p, t, d, f"""
      <h1>How to type Bangla with your voice on a Mac</h1>
      <p class="lead">Dictate Bangla into any Mac app with Kothalipi, free and offline. Setup takes about five minutes, most of it the model download.</p>
      <!--META-->
      <h2>1. Install Kothalipi</h2>
      <p>Open Terminal and run:</p>
      {code(INSTALL_SH)}
      <p>Or download the <code>.dmg</code> from the <a href="/download">download page</a> and drag Kothalipi to Applications. If macOS says it could not verify the app, open <b>System Settings → Privacy &amp; Security</b> and click <b>Open Anyway</b> (early releases are not notarized yet).</p>
      <h2>2. Allow Microphone and Accessibility</h2>
      <p>Kothalipi asks for two permissions. <b>Microphone</b> lets it hear you while you hold the key. <b>Accessibility</b> lets the keys work in every app and lets Kothalipi type where your cursor is. If a switch is off, turn on Kothalipi in <b>System Settings → Privacy &amp; Security</b>.</p>
      <h2>3. Choose Offline and download the Bangla model</h2>
      <p>Pick <b>Offline</b> to stay free and private. Setup reads your Mac's memory and chip and marks the best model. For Bangla that is <b>Qwen3-ASR 0.6B Bangla</b> (about 811 MB). Download it; you can continue while it finishes. Also download the English model if you want the English key.</p>
      <div class="note"><p>Short on memory (4 GB)? Choose <b>Cloud</b> instead and add a free Gemini key: <a href="/guides/free-gemini-api-key">how to get one</a>.</p></div>
      <h2>4. Check your keys</h2>
      <p>The defaults are <kbd>Right ⌘</kbd> for Bangla and <kbd>fn</kbd> for English. macOS can use both for its own features, and setup warns you if it does:</p>
      <ul>
        <li><b>Globe key:</b> System Settings → Keyboard → set <b>“Press 🌐 key to”</b> to <b>Do Nothing</b>.</li>
        <li><b>Dictation:</b> System Settings → Keyboard → Dictation → change the <b>Shortcut</b> away from “Press Right Command Key Twice”, or turn it off.</li>
      </ul>
      <p>You can also pick other keys in <b>Settings → General</b>.</p>
      <h2>5. Dictate</h2>
      <p>Click into any text field. Hold <kbd>Right ⌘</kbd>, speak Bangla, and let go. The text appears at your cursor. A small pill shows <b>BN</b> while you record.</p>
      <h2>Tips for better Bangla results</h2>
      <ul>
        <li>Speak in natural phrases and pause briefly between sentences.</li>
        <li>Use a headset or a close microphone in a quiet room.</li>
        <li>For long dictation, tap the key once to start and tap again to stop.</li>
        <li>For sentences that mix Bangla and English, use the Bangla key, and try Cloud mode with Gemini for the best accuracy.</li>
      </ul>
      <p>Problems? See <a href="/docs/troubleshooting">troubleshooting</a> or the full <a href="/docs/macos">macOS guide</a>.</p>
      {related(p)}
    """, current="guides", crumb_items=[("/", "Home"), ("/guides/", "Guides"), (p, "Bangla voice typing on Mac")], article=True, meta=f"Updated {UPDATED} · 5 min read")

    # ---------------------------------------------------------------- Windows
    p = "/guides/bangla-voice-typing-windows"
    t = "How to Type Bangla with Your Voice on Windows (Free)"
    d = "Set up free Bangla voice typing on Windows 10 and 11 with Kothalipi: install, allow the microphone, download the model, and use the Bangla and English keys."
    wide_page(p, t, d, f"""
      <h1>How to type Bangla with your voice on Windows</h1>
      <p class="lead">Dictate Bangla into any Windows app with Kothalipi, free and offline, on Windows 10 and 11.</p>
      <!--META-->
      <h2>1. Install Kothalipi</h2>
      <p>Open PowerShell and run:</p>
      {code(INSTALL_PS)}
      <p>It installs for your user account, with no administrator rights. Or download the <code>-setup.exe</code> from the <a href="/download">download page</a> and run it.</p>
      <div class="warn"><p><b>“Windows protected your PC”:</b> early releases are not code-signed yet, so SmartScreen warns you. Click <b>More info</b>, then <b>Run anyway</b>.</p></div>
      <h2>2. Allow the microphone</h2>
      <p>Setup asks for microphone access. If it is blocked, open <b>Settings → Privacy &amp; security → Microphone</b> and turn on <b>Microphone access</b> and <b>Let desktop apps access your microphone</b>.</p>
      <h2>3. Download the Bangla model</h2>
      <p>Choose <b>Offline</b> and download <b>Qwen3-ASR 0.6B Bangla</b> (about 811 MB), or choose <b>Cloud</b> with a free Gemini key (<a href="/guides/free-gemini-api-key">guide</a>). Setup reads your memory and recommends the best option.</p>
      <h2>4. Use the keys</h2>
      <p>Hold <kbd>Right Alt</kbd> for Bangla and <kbd>Right Ctrl</kbd> for English. Hold while you speak and let go to type, or tap once to start and again to stop.</p>
      <div class="note"><p>On some keyboard layouts Right Alt acts as <b>AltGr</b> and is used to type symbols. If that gets in the way, choose a different key in <b>Settings → General</b>.</p></div>
      <h2>Good to know</h2>
      <ul>
        <li>Windows blocks typing from a normal app into windows running as administrator. Run Kothalipi as administrator too if you need that.</li>
        <li>On Windows on ARM, the ARM installer is used automatically.</li>
        <li>To uninstall: Settings → Apps → Installed apps → Kothalipi.</li>
      </ul>
      <p>More in the <a href="/docs/windows">Windows guide</a> and <a href="/docs/troubleshooting">troubleshooting</a>.</p>
      {related(p)}
    """, current="guides", crumb_items=[("/", "Home"), ("/guides/", "Guides"), (p, "Bangla voice typing on Windows")], article=True, meta=f"Updated {UPDATED} · 4 min read")

    # ---------------------------------------------------------------- Linux
    p = "/guides/bangla-voice-typing-linux"
    t = "How to Type Bangla with Your Voice on Linux (Free)"
    d = "Set up free Bangla voice typing on Linux with Kothalipi: .deb, .rpm or AppImage, X11 and Wayland setup, and keyboard shortcuts."
    wide_page(p, t, d, f"""
      <h1>How to type Bangla with your voice on Linux</h1>
      <p class="lead">Dictate Bangla on Linux with Kothalipi. It works best on X11; Wayland needs a small typing helper.</p>
      <!--META-->
      <h2>1. Install</h2>
      {code(INSTALL_SH, "One line: picks .deb, .rpm or AppImage for you")}
      {code("sudo apt install ./Kothalipi_*_amd64.deb", "Debian and Ubuntu")}
      {code("sudo dnf install ./Kothalipi-*.x86_64.rpm", "Fedora")}
      {code("chmod +x Kothalipi_*_amd64.AppImage && ./Kothalipi_*_amd64.AppImage", "AppImage (any distribution)")}
      <p>If it will not start and mentions <code>libgtk-layer-shell.so.0</code>, install it: <code>sudo apt install libgtk-layer-shell0</code>.</p>
      <h2>2. Allow typing into other apps</h2>
      <h3>X11</h3>
      <p>Nothing to do. Kothalipi types through the X server.</p>
      <h3>Wayland</h3>
      <p>Wayland has no standard way for one app to type into another, so install a helper:</p>
      {code("sudo apt install wtype", "wlroots compositors such as Sway and Hyprland")}
      <p>On GNOME (for example Ubuntu 26.04), use <code>ydotool</code> with its service enabled.</p>
      <h2>3. Download the model and set your keys</h2>
      <p>Follow setup: choose Offline and download the Bangla model, or Cloud with a Gemini key. Default keys are <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>B</kbd> for Bangla and <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>E</kbd> for English.</p>
      <p>On Wayland, global keys are set in your desktop's keyboard settings. Bind a custom shortcut to <code>kothalipi --toggle-transcription</code>.</p>
      <p>More in the <a href="/docs/linux">Linux guide</a>.</p>
      {related(p)}
    """, current="guides", crumb_items=[("/", "Home"), ("/guides/", "Guides"), (p, "Bangla voice typing on Linux")], article=True, meta=f"Updated {UPDATED} · 4 min read")

    # ---------------------------------------------------------------- Gemini key
    p = "/guides/free-gemini-api-key"
    t = "Get a Free Gemini API Key for Bangla Voice Typing"
    d = "How to create a free Google Gemini API key and use it in Kothalipi for accurate cloud Bangla and English dictation, with automatic offline fallback."
    wide_page(p, t, d, f"""
      <h1>Get a free Gemini API key for Bangla voice typing</h1>
      <p class="lead">Cloud mode uses your own Google Gemini key. It is the most accurate choice for Bangla, especially when you mix Bangla and English.</p>
      <!--META-->
      <h2>1. Create the key</h2>
      <ol>
        <li>Open <a href="https://aistudio.google.com/apikey">Google AI Studio → API keys</a> and sign in with a Google account.</li>
        <li>Click <b>Create API key</b> and copy it.</li>
      </ol>
      <p>In Kothalipi's setup, the <b>Get a free key</b> button opens the same page.</p>
      <h2>2. Add it to Kothalipi</h2>
      <ol>
        <li>Open <b>Settings → General → Listening</b> and choose <b>Cloud (your keys)</b>.</li>
        <li>Paste the key under <b>Google Gemini</b> and click <b>Check &amp; Save</b>. Kothalipi checks the key before saving it.</li>
        <li>Hold your Bangla key and speak.</li>
      </ol>
      <p>Kothalipi uses the <code>gemini-3.5-transcribe</code> model by default. You can change the model name in the same settings.</p>
      <h2>What if the limit runs out?</h2>
      <p>The free tier has daily limits. When Gemini refuses a request, Kothalipi tries the next engine you enabled (for example OpenAI), and when every cloud engine fails, or you are offline, it falls back to your <b>offline model</b>. Keep the Bangla model downloaded so dictation never stops. You can reorder or turn off engines with the arrows in the same settings.</p>
      <h2>Optional: a second provider</h2>
      <p>Add an OpenAI key under <b>OpenAI (ChatGPT)</b> as a backup. OpenAI's API is paid per minute of audio. Kothalipi uses <code>gpt-transcribe</code> by default.</p>
      <h2>Privacy</h2>
      <ul>
        <li>Your key is stored on your computer and sent only to its provider.</li>
        <li>Audio goes straight from your computer to Google. It never passes through Kothalipi, which has no servers.</li>
        <li>Read Google's Gemini API terms: on unpaid tiers they can allow submitted content to be used to improve Google products. For anything sensitive, use <b>Offline</b> mode.</li>
      </ul>
      <p>Claude cannot transcribe audio, so it is not a speech engine here. It can polish your text afterwards in <b>Settings → Post-Processing</b>.</p>
      {related(p)}
    """, current="guides", crumb_items=[("/", "Home"), ("/guides/", "Guides"), (p, "Free Gemini API key")], article=True, meta=f"Updated {UPDATED} · 3 min read")

    # ---------------------------------------------------------------- index
    cards = "".join(
        f'<a class="card" href="{pp}"><h3>{esc(tt)}</h3><p>{esc(dd)}</p></a>'
        for pp, tt, dd in [
            ("/guides/bangla-voice-typing-mac", "Bangla voice typing on a Mac", "Install, permissions, the Bangla model and key conflicts."),
            ("/guides/bangla-voice-typing-windows", "Bangla voice typing on Windows", "Install, SmartScreen, microphone and the Bangla key."),
            ("/guides/bangla-voice-typing-linux", "Bangla voice typing on Linux", ".deb, .rpm, AppImage, X11 and Wayland."),
            ("/guides/free-gemini-api-key", "Free Gemini API key", "Cloud mode, fallback and privacy."),
        ]
    )
    wide_page("/guides/", "Guides: Bangla Voice Typing Step by Step | Kothalipi", "Step-by-step guides for Bangla voice typing on Mac, Windows and Linux, and how to use a free Gemini API key with Kothalipi.",
              f'<h1>Guides</h1><p class="lead">Step-by-step help for Bangla voice typing.</p><div class="cards">{cards}</div>',
              current="guides", crumb_items=[("/", "Home"), ("/guides/", "Guides")])


def models():
    p = "/models"
    t = "Bangla & English Speech Models, Accuracy and Device Picks | Kothalipi"
    d = "Which Bangla and English speech models Kothalipi uses, their size, license and published accuracy, and which fits your computer's memory."
    body = f"""
      <h1>Models and accuracy</h1>
      <p class="lead">Kothalipi runs open speech models on your computer, or your own cloud key. Setup picks the best fit for your memory and chip.</p>
      <!--META-->
      <h2>Bangla (offline)</h2>
      <table class="table"><thead><tr><th>Model</th><th>Size</th><th>License</th><th>About</th></tr></thead><tbody>
        <tr><td><b>Qwen3-ASR 0.6B Bangla</b> <span class="badge">Recommended</span></td><td>811 MB</td><td>Apache-2.0</td><td>Fine-tuned for Bangla on 1,174 hours of speech across nine datasets. Its authors report 14.74% word error rate and 5.34% character error rate on a 10,485-utterance held-out test set.</td></tr>
        <tr><td><b>Bengali.AI Whisper Medium</b></td><td>514 MB</td><td>Apache-2.0</td><td>Bengali.AI's Bangla fine-tune of Whisper. Strong on read speech, slower.</td></tr>
      </tbody></table>
      <p class="muted">Figures for Qwen3-ASR are from its model card, measured on its authors' test set, not on Kothalipi. Results on your voice, microphone and topic will differ.</p>
      <h2>English (offline)</h2>
      <table class="table"><thead><tr><th>Model</th><th>Size</th><th>Best for</th></tr></thead><tbody>
        <tr><td><b>Parakeet 0.6B</b> <span class="badge">Recommended</span></td><td>697 MB</td><td>Most accurate English, very fast.</td></tr>
        <tr><td><b>Whisper Small (English)</b></td><td>257 MB</td><td>Older or lighter computers.</td></tr>
        <tr><td><b>Whisper Base (English)</b></td><td>80 MB</td><td>Very low memory.</td></tr>
      </tbody></table>
      <h2>Cloud (your own key)</h2>
      <table class="table"><thead><tr><th>Engine</th><th>Default model</th><th>Notes</th></tr></thead><tbody>
        <tr><td><b>Google Gemini</b></td><td><code>gemini-3.5-transcribe</code></td><td>Free tier with daily limits. Usually best for Bangla mixed with English.</td></tr>
        <tr><td><b>OpenAI</b></td><td><code>gpt-transcribe</code></td><td>Paid per minute of audio. A good backup.</td></tr>
      </tbody></table>
      <p>If every cloud engine fails or you are offline, Kothalipi falls back to your offline model.</p>
      <h2>Which one fits your computer?</h2>
      <table class="table"><thead><tr><th>Memory</th><th>Recommendation</th></tr></thead><tbody>
        <tr><td>Under 8 GB</td><td>Cloud mode (Gemini) for the best accuracy. Offline still works with the Bangla model; use Whisper Small for English.</td></tr>
        <tr><td>8 to 15 GB</td><td>Offline with Qwen3-ASR 0.6B Bangla and Parakeet 0.6B.</td></tr>
        <tr><td>16 GB or more (or Apple Silicon with 12 GB+)</td><td>Same models, with plenty of room for your other apps.</td></tr>
      </tbody></table>
      <h2>A public benchmark is coming</h2>
      <p>We are building an open Bangla test set (read speech, phone recordings and Bangla mixed with English) to compare every model on the same audio, and will publish the results here. Want to help? <a href="{GH}/kothalipi/blob/main/CONTRIBUTING.md">Contribute recordings</a>.</p>
      <p class="muted">Credits: Qwen3-ASR Bangla by SayedShaun (GGUF by sheikhmufrad), Bengali.AI Whisper (ggml by winshades), Parakeet by NVIDIA, Whisper by OpenAI. Each model keeps its own license.</p>
    """
    wide_page(p, t, d, body, current="models", crumb_items=[("/", "Home"), (p, "Models")], article=True, meta=f"Updated {UPDATED}", priority="0.8")


def changelog():
    p = "/changelog"
    body = f"""
      <h1>Changelog</h1>
      <p class="lead">What changed in each version of Kothalipi.</p>
      <h2 id="v0-1-6">v0.1.6 · {UPDATED}</h2>
      <p>Live Bangla to English Voice Translation, mobile apps, and theme switcher.</p>
      <ul>
        <li><b>Real-time Bangla to English Voice Translation:</b> Speak naturally in everyday Bangla, and Kothalipi automatically writes out fluent, grammatically polished English using Google Gemini AI.</li>
        <li><b>Kothalipi Mobile (Android & iOS):</b> Released Wispr Flow-style floating bubble and voice keyboard extension for instant dictation in any app.</li>
        <li><b>Light / Dark Mode:</b> One-click toggle button on navbar with zero-flicker instant theme loading.</li>
        <li><b>Direct Voice Typing from Tray:</b> Trigger voice typing directly from system tray menu.</li>
        <li><b>Enhanced Contrast:</b> Optimized readability and colors for AI translation cards and button UI.</li>
      </ul>
      <h2 id="v0-1-0">v0.1.0</h2>
      <p>The first desktop release.</p>
      <ul>
        <li><b>Two keys, two languages.</b> Hold Right ⌘ (Windows: Right Alt) for Bangla and fn (Windows: Right Ctrl) for English. Each key picks its own language and model.</li>
        <li><b>Offline or cloud.</b> Offline runs Bangla models on your computer. Cloud uses your Gemini or OpenAI key, with automatic fallback to the offline model.</li>
        <li><b>Bangla models built in:</b> Qwen3-ASR 0.6B Bangla and Bengali.AI Whisper Medium, verified by SHA-256 after download.</li>
        <li><b>Device-aware setup.</b> Reads your memory and chip and recommends the best models; low-memory computers are steered to Cloud.</li>
        <li><b>Guided onboarding</b> with API key checks, model downloads and macOS key-conflict detection.</li>
        <li><b>Recording pill</b> shows BN or EN for the active key.</li>
        <li><b>Bangla interface</b> for the core screens (the rest falls back to English).</li>
        <li>Installers for macOS (Apple Silicon and Intel), Windows (x64 and ARM) and Linux (.deb, .rpm, AppImage). Not code-signed yet.</li>
      </ul>
      <p>Full release notes and downloads: <a href="{DESK}/releases">GitHub Releases</a>.</p>
    """
    wide_page(p, "Changelog: What's New in Kothalipi", "Release notes for every version of Kothalipi, the free Bangla and English voice typing app.", body, crumb_items=[("/", "Home"), (p, "Changelog")], changefreq="weekly", priority="0.5")


def about():
    p = "/about"
    body = f"""
      <h1>About Kothalipi</h1>
      <p class="lead">Bangla deserves software that listens. Kothalipi (কথালিপি, “speech-script”) turns your voice into Bangla and English text in any app.</p>
      <!--META-->
      <h2>Why it exists</h2>
      <p>Most voice typing tools are built for English first, and Bangla comes later, with models that make many mistakes. Kothalipi starts from Bangla: Bangla-trained models, a key for each language, and a setup that works on ordinary computers. It is free and open source so that anyone can use it, check it and improve it.</p>
      <h2>Made by</h2>
      <p><b>TA Shanto</b>, a developer from Bangladesh. <a href="{MAKER}">tashanto.com</a> · <a href="https://github.com/iamtashanto">GitHub</a></p>
      <h2>Built on open work</h2>
      <p>Kothalipi's speech engine, hotkey handling and text insertion began from the open-source <a href="https://github.com/cjpais/Handy">Handy</a> project by CJ Pais (MIT). On-device recognition uses transcribe.cpp and ggml, and the Bangla models are open models from the community. Everything else is Kothalipi's own. See the full <a href="{DESK}/blob/main/NOTICE.md">credits</a>.</p>
      <h2>Support the project</h2>
      <p>Kothalipi is free and has no ads, accounts or tracking. If it saves you time and you would like to help keep it going, you can <a href="{SUPPORT}" rel="noopener">support its development</a>. Telling a friend, reporting a wrong word or sharing a recording helps just as much.</p>
      <h2>Get involved</h2>
      <ul>
        <li><a href="{GH}/kothalipi/discussions">Discussions</a>: ask questions, share ideas.</li>
        <li><a href="{DESK}/issues">Issues</a>: report a bug or wrong words.</li>
        <li><a href="{GH}/kothalipi/blob/main/CONTRIBUTING.md">Contribute</a>: recordings, models, translations, code.</li>
      </ul>
    """
    schema = [{"@context": "https://schema.org", "@type": "AboutPage", "name": "About Kothalipi", "url": abs_url(p), "mainEntity": ORG}]
    wide_page(p, "About Kothalipi: Open-Source Bangla Voice Typing by TA Shanto", "Why Kothalipi exists, who makes it, and the open projects it is built on.", body, crumb_items=[("/", "Home"), (p, "About")], schema_extra=schema, priority="0.4")


def privacy():
    p = "/privacy"
    body = """
      <h1>Privacy</h1>
      <p class="lead">Short version: Kothalipi collects nothing.</p>
      <!--META-->
      <h2>The app</h2>
      <ul>
        <li><b>No account, no analytics, no servers.</b> Kothalipi has no backend that receives your data.</li>
        <li><b>Offline mode</b> turns speech into text on your computer. Audio never leaves it.</li>
        <li><b>Cloud mode</b> sends a recording only to the provider whose key you added (Google or OpenAI), under that provider's terms. It is off until you turn it on.</li>
        <li><b>Smart Polish</b> is off until you turn it on. When on, the <i>text</i> of what you said (never the audio) is sent to Google Gemini with your own key to fix spelling and punctuation.</li>
        <li><b>API keys</b> are stored in the app's settings on your computer and sent only to their provider.</li>
        <li><b>History</b> of transcripts and recordings is kept on your computer so you can review it. You can turn it off or delete it in Settings.</li>
        <li><b>Model downloads</b> come from Hugging Face, and update checks and installers from GitHub, like any download.</li>
      </ul>
      <h2>This website</h2>
      <ul>
        <li>No cookies, no analytics, no ads, no third-party scripts. Fonts are served from this site.</li>
        <li>The download page asks GitHub's public API for the latest release, so GitHub sees your IP address as with any request to it.</li>
        <li>The site is hosted on GitHub Pages, which keeps standard server logs.</li>
      </ul>
      <p>The code is open: <a href="https://github.com/Kothalipi/kothalipi-desktop">check it yourself</a>.</p>
    """
    wide_page(p, "Privacy: Kothalipi Collects Nothing", "Kothalipi has no accounts, analytics or servers. Offline mode keeps audio on your computer; cloud mode is optional and uses your own key.", body, crumb_items=[("/", "Home"), (p, "Privacy")], priority="0.3")


# ---------------------------------------------------------------------- docs
DOCS_NAV = [
    ("Start", [("/docs/", "Getting started"), ("/docs/shortcuts", "Keys & shortcuts"), ("/docs/cloud", "Cloud & API keys")]),
    ("Install", [("/docs/macos", "macOS"), ("/docs/windows", "Windows"), ("/docs/linux", "Linux")]),
    ("Help", [("/docs/troubleshooting", "Troubleshooting")]),
]
DOC_ORDER = [p for _, items in DOCS_NAV for p, _ in items]


def doc(path, title, desc, body, label):
    nav = ""
    labels = {}
    for group, items in DOCS_NAV:
        nav += f"<h4>{group}</h4>"
        for h, l in items:
            labels[h] = l
            cur = ' aria-current="page"' if h == path else ""
            nav += f'<a href="{h}"{cur}>{esc(l)}</a>'
    i = DOC_ORDER.index(path)
    prev = f'<a href="{DOC_ORDER[i-1]}">← {labels[DOC_ORDER[i-1]]}</a>' if i > 0 else "<span></span>"
    nxt = f'<a href="{DOC_ORDER[i+1]}">{labels[DOC_ORDER[i+1]]} →</a>' if i < len(DOC_ORDER) - 1 else "<span></span>"
    cr, bc = crumbs([("/", "Home"), ("/docs/", "Docs")] + ([(path, label)] if path != "/docs/" else []))
    body = f'<div class="container docs"><nav class="docs-nav" aria-label="Docs">{nav}</nav><article class="doc">{cr}{body}<div class="pager">{prev}{nxt}</div></article></div>'
    page(path, title, desc, body, current="docs", schema=[bc, article_schema(title, desc, path)], priority="0.7")


def docs():
    doc("/docs/", "Getting Started with Kothalipi | Docs", "Install Kothalipi and dictate your first sentence in Bangla or English in about two minutes.", f"""
      <h1>Getting started</h1>
      <p class="lead">From download to your first Bangla sentence in about five minutes.</p>
      <h2>1. Install</h2>
      <p>Download from the <a href="/download">download page</a>, or use the terminal:</p>
      {code(INSTALL_SH, "macOS and Linux")}
      {code(INSTALL_PS, "Windows (PowerShell)")}
      <p>Platform details: <a href="/docs/macos">macOS</a> · <a href="/docs/windows">Windows</a> · <a href="/docs/linux">Linux</a>.</p>
      <h2>2. Follow the setup</h2>
      <ol>
        <li><b>Permissions.</b> Allow the microphone. On a Mac, also allow Accessibility so Kothalipi can type into other apps.</li>
        <li><b>Choose how it listens.</b> <em>Offline</em> is free and private. <em>Cloud</em> uses your own Gemini or ChatGPT key and is the most accurate. Low-memory computers are steered to Cloud. See <a href="/docs/cloud">Cloud &amp; API keys</a>.</li>
        <li><b>Download the voice models.</b> Setup recommends the best Bangla and English model for your computer. In Cloud mode they are your offline backup.</li>
        <li><b>Check your keys.</b> On a Mac, Kothalipi spots macOS settings that steal the keys and opens the right page.</li>
        <li><b>Try it.</b> Hold the Bangla key, speak, let go.</li>
      </ol>
      <h2>3. Use it anywhere</h2>
      <table class="table"><tr><th></th><th>macOS</th><th>Windows</th><th>Linux</th></tr>
        <tr><td>বাংলা</td><td><kbd>Right ⌘</kbd></td><td><kbd>Right Alt</kbd></td><td><kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>B</kbd></td></tr>
        <tr><td>English</td><td><kbd>fn</kbd></td><td><kbd>Right Ctrl</kbd></td><td><kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>E</kbd></td></tr></table>
      <p><b>Hold</b> the key while you talk, or <b>tap</b> once to start and again to stop. Change keys in <b>Settings → General</b>.</p>
    """, "Getting started")

    doc("/docs/shortcuts", "Keys & Shortcuts | Kothalipi Docs", "Default Bangla and English keys, hold and tap, and how to change them.", f"""
      <h1>Keys &amp; shortcuts</h1>
      <p class="lead">One key per language. The key decides the language and the model for that recording.</p>
      <table class="table"><tr><th>Key</th><th>macOS</th><th>Windows</th><th>Linux</th><th>What it does</th></tr>
        <tr><td>Bangla</td><td><kbd>Right ⌘</kbd></td><td><kbd>Right Alt</kbd></td><td><kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>B</kbd></td><td>Bangla script, using your Bangla model</td></tr>
        <tr><td>English</td><td><kbd>fn</kbd></td><td><kbd>Right Ctrl</kbd></td><td><kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>E</kbd></td><td>English, using your English model</td></tr>
        <tr><td>Transcribe</td><td><kbd>⌥ Option</kbd>+<kbd>Space</kbd></td><td><kbd>Ctrl</kbd>+<kbd>Space</kbd></td><td><kbd>Ctrl</kbd>+<kbd>Space</kbd></td><td>Your selected model and language</td></tr>
        <tr><td>Cancel</td><td colspan="3"><kbd>Esc</kbd></td><td>Discards the current recording</td></tr></table>
      <h2>Hold or tap</h2>
      <p>Hold a key while you speak and let go to type, or tap it once to start and again to stop. Tapping is handy for long dictation.</p>
      <h2>Which language is active?</h2>
      <p>The recording pill shows <b>BN</b> or <b>EN</b> while you speak, so a wrong key is obvious right away.</p>
      <h2>Change a key</h2>
      <ol><li>Open Kothalipi from the menu bar or system tray.</li><li>Go to <b>Settings → General</b>.</li><li>Click the key you want to change and press the new one. A single modifier such as Right Command works on Mac and Windows.</li></ol>
      <div class="warn"><p><b>Mac:</b> macOS can use <kbd>fn</kbd> (🌐) and <kbd>Right ⌘</kbd> for its own features. See <a href="/docs/macos#keys">fixing key conflicts</a>.</p></div>
    """, "Keys & shortcuts")

    doc("/docs/cloud", "Cloud Mode & API Keys | Kothalipi Docs", "Use your own Gemini or ChatGPT key for the most accurate Bangla dictation, with automatic fallback to offline.", f"""
      <h1>Cloud &amp; API keys</h1>
      <p class="lead">Cloud mode sends your recording to the provider you choose, using your own key. It is the most accurate option, especially for Bangla mixed with English.</p>
      <h2>How fallback works</h2>
      <p>Kothalipi tries your engines in order: <b>Gemini</b>, then <b>OpenAI</b>. If a key is over its limit, rejected, the provider is down or you have no internet, it moves to the next. When every cloud engine fails it uses your <b>offline model</b>, so keep the Bangla model downloaded. With no offline model either, it asks you to download one.</p>
      <h2 id="gemini">Get a free Gemini key</h2>
      <ol>
        <li>Open <a href="https://aistudio.google.com/apikey">Google AI Studio → API keys</a> and sign in.</li>
        <li>Click <b>Create API key</b> and copy it.</li>
        <li>In Kothalipi: <b>Settings → General → Listening</b>, choose <b>Cloud</b>, paste it under Google Gemini and click <b>Check &amp; Save</b>.</li>
      </ol>
      <p>Gemini has a free tier with daily limits; usage above it is billed by Google to you. Default model: <code>gemini-3.5-transcribe</code>. Full walkthrough: <a href="/guides/free-gemini-api-key">free Gemini API key guide</a>.</p>
      <h2 id="openai">Add an OpenAI (ChatGPT) key</h2>
      <p>Create a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a> (paid per minute of audio) and paste it under <b>OpenAI (ChatGPT)</b>. Default model: <code>gpt-transcribe</code>. Use the arrows to try OpenAI before Gemini.</p>
      <h2 id="claude">What about Claude?</h2>
      <p>Claude does not take audio input, so it cannot turn speech into text. It can polish your text afterwards: set it up in <b>Settings → Post-Processing</b> with your Anthropic API key.</p>
      <h2>Where your keys and audio go</h2>
      <ul><li>Keys are stored on your computer and sent only to their provider.</li><li>Audio goes straight from your computer to that provider. Kothalipi has no servers.</li><li>Offline mode sends nothing anywhere.</li></ul>
    """, "Cloud & API keys")

    doc("/docs/macos", "Kothalipi on macOS: Install, Permissions, Keys | Docs", "Install Kothalipi on a Mac, allow Microphone and Accessibility, and fix key conflicts.", f"""
      <h1>macOS</h1>
      <p class="lead">For Apple Silicon (M1 or newer) and Intel Macs on macOS 10.15 or later.</p>
      <h2>Install</h2>
      <h3>Terminal (recommended)</h3>
      {code(INSTALL_SH)}
      <p>Installs <code>Kothalipi.app</code> into Applications and opens it.</p>
      <h3>Disk image</h3>
      <ol><li>Download the <code>.dmg</code> from the <a href="/download">download page</a>.</li><li>Open it and drag <b>Kothalipi</b> into <b>Applications</b>.</li><li>Open Kothalipi from Applications.</li></ol>
      <div class="warn"><p><b>“Apple could not verify Kothalipi…”</b> Early releases are not notarized by Apple yet. Open <b>System Settings → Privacy &amp; Security</b>, scroll down and click <b>Open Anyway</b> next to Kothalipi, then confirm. You only do this once. The terminal installer avoids this step.</p></div>
      <h2>Permissions</h2>
      <table class="table"><tr><th>Permission</th><th>Why</th><th>Where</th></tr>
        <tr><td>Microphone</td><td>To hear you while you hold a key. Nothing is recorded otherwise.</td><td>System Settings → Privacy &amp; Security → Microphone</td></tr>
        <tr><td>Accessibility</td><td>So the keys work in every app and Kothalipi can type where your cursor is.</td><td>System Settings → Privacy &amp; Security → Accessibility</td></tr></table>
      <p>If a switch is off, turn on <b>Kothalipi</b> in that list. If it is not listed, click <b>+</b> and add it from Applications.</p>
      <h2 id="keys">Fix key conflicts</h2>
      <p>Two macOS settings can steal Kothalipi's default keys. Setup checks both and opens Keyboard settings for you.</p>
      <ol>
        <li><b>Globe (🌐/fn) key:</b> System Settings → Keyboard → set <b>“Press 🌐 key to”</b> to <b>Do Nothing</b>.</li>
        <li><b>Dictation shortcut:</b> System Settings → Keyboard → Dictation → <b>Shortcut</b>: choose anything other than <b>“Press Right Command Key Twice”</b> or the 🌐 key, or turn it off.</li>
      </ol>
      <p>Or change Kothalipi's keys in <b>Settings → General</b>.</p>
      <h2>Uninstall</h2>
      {code('rm -rf /Applications/Kothalipi.app "$HOME/Library/Application Support/com.kothalipi.desktop"')}
    """, "macOS")

    doc("/docs/windows", "Kothalipi on Windows: Install & Setup | Docs", "Install Kothalipi on Windows 10 or 11 and fix SmartScreen and microphone issues.", f"""
      <h1>Windows</h1>
      <p class="lead">For Windows 10 and 11, 64-bit and ARM.</p>
      <h2>Install</h2>
      <h3>PowerShell (recommended)</h3>
      {code(INSTALL_PS)}
      <p>Installs for your user account (no administrator rights) and opens Kothalipi.</p>
      <h3>Installer</h3>
      <ol><li>Download the <code>-setup.exe</code> from the <a href="/download">download page</a>.</li><li>Run it and follow the steps.</li></ol>
      <div class="warn"><p><b>“Windows protected your PC”:</b> early releases are not code-signed yet, so SmartScreen warns you. Click <b>More info</b>, then <b>Run anyway</b>.</p></div>
      <h2>Microphone</h2>
      <p>If Kothalipi cannot hear you: <b>Settings → Privacy &amp; security → Microphone</b>, turn on <b>Microphone access</b> and <b>Let desktop apps access your microphone</b>.</p>
      <h2>Keys</h2>
      <p>Bangla: <kbd>Right Alt</kbd>. English: <kbd>Right Ctrl</kbd>. On some layouts Right Alt is AltGr; choose another key in Settings → General if it gets in the way. Apps running as administrator block typing from other apps; run Kothalipi as administrator too if you need it there.</p>
      <h2>Uninstall</h2>
      <p>Settings → Apps → Installed apps → Kothalipi → Uninstall.</p>
    """, "Windows")

    doc("/docs/linux", "Kothalipi on Linux: Install, X11 & Wayland | Docs", "Install Kothalipi on Linux with .deb, .rpm or AppImage, and set up typing on X11 and Wayland.", f"""
      <h1>Linux</h1>
      <p class="lead">x86_64 and ARM64. Works best on X11; Wayland needs a typing helper.</p>
      <h2>Install</h2>
      {code(INSTALL_SH, "Terminal (picks .deb, .rpm or AppImage for you)")}
      <h3>Manually</h3>
      {code("sudo apt install ./Kothalipi_*_amd64.deb", "Debian / Ubuntu")}
      {code("sudo dnf install ./Kothalipi-*.x86_64.rpm", "Fedora")}
      {code("chmod +x Kothalipi_*_amd64.AppImage && ./Kothalipi_*_amd64.AppImage", "AppImage")}
      <h2>Wayland</h2>
      <p>Wayland has no standard way for one app to type into another. Install a helper:</p>
      {code("sudo apt install wtype      # wlroots compositors (Sway, Hyprland…)", "wtype")}
      <p>On GNOME (Ubuntu 26.04+), use <code>ydotool</code> with its service enabled. Global keys on Wayland are set in your desktop's keyboard settings: bind a custom shortcut to <code>kothalipi --toggle-transcription</code>.</p>
      <h2>Missing libraries</h2>
      <p>If it will not start and <code>libgtk-layer-shell.so.0</code> is missing:</p>
      {code("sudo apt install libgtk-layer-shell0")}
    """, "Linux")

    doc("/docs/troubleshooting", "Troubleshooting Kothalipi | Docs", "Fix common problems: keys not working, nothing typed, wrong Bangla words, or cloud mode stopping.", f"""
      <h1>Troubleshooting</h1>
      <h2>Nothing happens when I hold the key</h2>
      <ul><li>Mac: check Accessibility is on for Kothalipi (<a href="/docs/macos">guide</a>) and fix <a href="/docs/macos#keys">key conflicts</a>.</li><li>Make sure Kothalipi is running (menu bar or system tray icon).</li><li>Try the other key, or set a new one in Settings → General.</li></ul>
      <h2>It hears me but types nothing</h2>
      <ul><li>Click into a text field first; the text goes where your cursor is.</li><li>Check the microphone in Settings → Sound.</li></ul>
      <h2>Wrong words in Bangla</h2>
      <ul><li>Use the Bangla key, not the general Transcribe key. The pill should show <b>BN</b>.</li><li>Download <b>Qwen3-ASR 0.6B Bangla</b> in Settings → Models.</li><li>For Bangla mixed with English, Cloud mode with a Gemini key is the most accurate.</li><li>Tell us: <a href="https://github.com/Kothalipi/kothalipi-desktop/issues/new?template=wrong_transcription.md">report wrong words</a>.</li></ul>
      <h2>Cloud stopped working</h2>
      <p>Your key may be over its daily limit. Kothalipi falls back to offline automatically; add a second key or wait for the limit to reset. Check the key in Settings → General → Listening.</p>
      <h2>Still stuck?</h2>
      <p>Ask in <a href="https://github.com/Kothalipi/kothalipi/discussions">Discussions</a> or <a href="https://github.com/Kothalipi/kothalipi-desktop/issues">open an issue</a>.</p>
    """, "Troubleshooting")


def not_found():
    body = '<section class="container notfound"><h1>Page not found</h1><p class="lead center">That page does not exist.</p><p style="margin-top:28px"><a class="btn btn-primary" href="/">Go home</a></p></section>'
    page("/404", "Page not found | Kothalipi", "This page does not exist.", body, noindex=True)


def get_pages():
    """/get/mac, /get/windows, /get/linux: shareable shortcuts that start the right download."""
    names = {"mac": "macOS", "windows": "Windows", "linux": "Linux"}
    for k, n in names.items():
        body = (f'<section class="container get-page" data-get="{k}"><div class="spinner" aria-hidden="true"></div>'
                f'<h1 id="get-msg" style="font-size:34px">Getting Kothalipi for {n}…</h1>'
                f'<p class="lead center" id="get-sub">Your download starts in a moment.</p>'
                f'<p style="margin-top:22px"><a class="btn btn-primary" id="get-link" hidden href="/download">Download again</a></p>'
                f'<noscript><p><a href="/download">Go to the download page</a></p></noscript></section>')
        page(f"/get/{k}", f"Download Kothalipi for {n}", f"Start the free Kothalipi download for {n}. Bangla and English voice typing, set up in about two minutes.", body, noindex=True)
