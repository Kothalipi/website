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
    ("/guides/free-groq-api-key", "Get a free Groq Whisper API key (Ultra-Fast)"),
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
      <p>The free tier has daily limits. When Gemini refuses a request, Kothalipi automatically tries the next engine you enabled — such as <b>Groq Whisper (Free)</b> (<a href="/guides/free-groq-api-key">get a free Groq key</a>) or OpenAI — and when every cloud engine fails or you are offline, it falls back to your <b>offline model</b>. Keep the Bangla model downloaded (or Offline Mode ready on Mobile) so dictation never stops.</p>
      <h2>Optional: a second free provider (Groq Whisper)</h2>
      <p>Add a free <b>Groq Whisper</b> key (<a href="https://console.groq.com/keys">console.groq.com/keys</a>) for ultra-fast <code>whisper-large-v3-turbo</code> transcription, or an OpenAI key as a paid backup.</p>
      <h2>Privacy</h2>
      <ul>
        <li>Your key is stored on your computer or phone and sent only to its provider.</li>
        <li>Audio goes straight from your device to Google/Groq/OpenAI. It never passes through Kothalipi, which has no servers.</li>
        <li>Read Google's Gemini API terms: on unpaid tiers they can allow submitted content to be used to improve Google products. For anything sensitive, use <b>Offline</b> mode.</li>
      </ul>
      <p>Claude cannot transcribe audio, so it is not a speech engine here. It can polish your text afterwards in <b>Settings → Post-Processing</b>.</p>
      {related(p)}
    """, current="guides", crumb_items=[("/", "Home"), ("/guides/", "Guides"), (p, "Free Gemini API key")], article=True, meta=f"Updated {UPDATED} · 3 min read")

    # ---------------------------------------------------------------- Groq key
    p = "/guides/free-groq-api-key"
    t = "Get a Free Groq Whisper API Key (Ultra-Fast Bangla & English)"
    d = "Step-by-step guide to creating a free Groq API key for whisper-large-v3-turbo in Kothalipi Desktop and Mobile (Android & iOS)."
    wide_page(p, t, d, f"""
      <h1>Get a free Groq Whisper API key</h1>
      <p class="lead">Groq runs OpenAI's <code>whisper-large-v3-turbo</code> on custom LPU hardware with a generous free tier. It transcribes Bangla and English in under a second and makes the perfect free backup alongside Google Gemini.</p>
      <!--META-->
      <h2>Step 1: Create your free Groq API key</h2>
      <ol>
        <li>Open <a href="https://console.groq.com/keys">console.groq.com/keys</a> and sign in with Google or GitHub (no credit card required).</li>
        <li>Click <b>Create API Key</b>, give it a name like <code>Kothalipi</code>, and copy the key (starts with <code>gsk_...</code>).</li>
      </ol>
      <div class="note"><p><b>Tip:</b> In both Kothalipi Desktop and Kothalipi Mobile, you can tap the <b>Get a free key / Groq Key ↗</b> button in Settings to open this page directly.</p></div>
      <h2>Step 2: Add it to Kothalipi Desktop (v0.1.8+)</h2>
      <ol>
        <li>Open Kothalipi → <b>Settings → General → Listening</b> and select <b>Cloud (your keys)</b>.</li>
        <li>Paste your <code>gsk_...</code> key under <b>Groq Whisper (Free, Ultra-Fast)</b>.</li>
        <li>Click <b>Save</b>. Kothalipi verifies the key automatically.</li>
        <li>Use the up/down arrows to choose whether <b>Gemini</b> or <b>Groq Whisper</b> runs first — if one hits its free quota, Kothalipi automatically falls back to the other!</li>
      </ol>
      <h2>Step 3: Add it to Kothalipi Mobile (Android &amp; iOS v0.2.0+)</h2>
      <ol>
        <li>Open the <b>Kothalipi</b> mobile app and tap <b>⚙️ Settings</b>.</li>
        <li>Paste your key into the <b>Groq Whisper Key</b> field and tap <b>Test</b> to confirm connection.</li>
        <li>Set <b>Primary Provider</b> to <b>Auto</b> (automatic fallback between Gemini &amp; Groq) or <b>Groq</b>, then tap <b>Save</b>.</li>
      </ol>
      <h2>Free tier limits &amp; usage</h2>
      <p>Groq offers a generous free tier for <code>whisper-large-v3-turbo</code>. You can check your live usage anytime at <a href="https://console.groq.com/settings/limits">console.groq.com/settings/limits</a>.</p>
      {related(p)}
    """, current="guides", crumb_items=[("/", "Home"), ("/guides/", "Guides"), (p, "Free Groq Whisper API key")], article=True, meta=f"Updated {UPDATED} · 2 min read")

    # ---------------------------------------------------------------- index
    cards = "".join(
        f'<a class="card" href="{pp}"><h3>{esc(tt)}</h3><p>{esc(dd)}</p></a>'
        for pp, tt, dd in [
            ("/guides/bangla-voice-typing-mac", "Bangla voice typing on a Mac", "Install, permissions, the Bangla model and key conflicts."),
            ("/guides/bangla-voice-typing-windows", "Bangla voice typing on Windows", "Install, SmartScreen, microphone and the Bangla key."),
            ("/guides/bangla-voice-typing-linux", "Bangla voice typing on Linux", ".deb, .rpm, AppImage, X11 and Wayland."),
            ("/guides/free-gemini-api-key", "Free Gemini API key", "Step-by-step Google AI Studio key setup, fallback and privacy."),
            ("/guides/free-groq-api-key", "Free Groq Whisper API key", "Ultra-fast whisper-large-v3-turbo setup for Desktop & Mobile."),
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
      <h2>Cloud (your own free or paid key)</h2>
      <table class="table"><thead><tr><th>Engine</th><th>Default model</th><th>Cost</th><th>Notes</th></tr></thead><tbody>
        <tr><td><b>Google Gemini</b> <span class="badge">Recommended</span></td><td><code>gemini-2.5-flash</code> (Mobile)<br><code>gemini-3.5-transcribe</code> (Desktop)</td><td>Free tier</td><td>Best accuracy for Bangla, natural Banglish code-switching, Smart Polish, and Live Bangla→English translation. <a href="/guides/free-gemini-api-key">Get free key →</a></td></tr>
        <tr><td><b>Groq Whisper</b> <span class="badge">New · Free</span></td><td><code>whisper-large-v3-turbo</code></td><td>Free tier</td><td>Sub-second ultra-fast transcription on Groq LPU hardware. Perfect free backup when Gemini reaches daily limits. <a href="/guides/free-groq-api-key">Get free key →</a></td></tr>
        <tr><td><b>OpenAI</b></td><td><code>gpt-transcribe</code> / <code>whisper-1</code></td><td>Paid</td><td>Pay-per-minute backup option for heavy cloud users.</td></tr>
      </tbody></table>
      <p>Kothalipi supports automatic multi-provider fallback: <b>Gemini → Groq Whisper → OpenAI → Offline</b>. See <a href="/docs/cloud">Cloud &amp; API keys</a> for step-by-step setup.</p>

      <h2>Mobile on-device offline (Android &amp; iOS)</h2>
      <table class="table"><thead><tr><th>Platform</th><th>Engine</th><th>Extra Size</th><th>Notes</th></tr></thead><tbody>
        <tr><td><b>Android</b></td><td>OS Native <code>SpeechRecognizer</code> (<code>bn-BD</code> / <code>en-US</code>)</td><td>0 MB</td><td>100% free, zero API keys, works offline when Android's Bangla language pack is downloaded.</td></tr>
        <tr><td><b>iPhone / iOS</b></td><td>Apple <code>SFSpeechRecognizer</code> (On-Device)</td><td>0 MB</td><td>100% free on-device speech recognition with live partial text streaming.</td></tr>
      </tbody></table>
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
      <h2 id="v0-1-8">v0.1.8 (Desktop) &amp; v0.2.0 (Mobile) · {UPDATED}</h2>
      <p>Free Groq Whisper integration on Desktop &amp; Mobile, plus a major Mobile v0.2.0 overhaul with Voice Snippets, Voice Edit, Hold-to-Talk, Auto-Stop (VAD), and Free Offline Mode.</p>
      <ul>
        <li><b>Groq Whisper (Free, Ultra-Fast):</b> Built-in <code>whisper-large-v3-turbo</code> provider on Desktop and Mobile with one-click Get Free Key links and automatic Gemini → Groq → OpenAI → Offline fallback.</li>
        <li><b>Mobile v0.2.0 Complete Overhaul (Android &amp; iOS):</b> Fixed Gemini 2.5 Flash audio pipeline, Android 14+ Floating Bubble foreground service, real iOS Voice Keyboard dictation, Voice Snippets, Voice Edit Commands, Hold-to-Talk, 2-second Auto-Silence Stop (VAD), and 0-MB Free Offline Mode.</li>
      </ul>
      <h2 id="v0-1-7">v0.1.7 · {UPDATED}</h2>
      <p>Natural Bangla+English code-switching, App-Aware Tone, Vibe Coding, Voice Snippets, Personal Dictionary, Bot-free Meeting Notes, and smarter onboarding.</p>
      <ul>
        <li><b>Natural Banglish Code-Switching (On by default):</b> Speak Bangla with English words or technical terms mixed in, and Kothalipi keeps English words in proper English script automatically (toggleable in Settings).</li>
        <li><b>App-Aware Tone &amp; Vibe Coding Mode:</b> Automatically adapts tone to the active app — casual in WhatsApp/Messenger/Slack, formal in Mail/Docs, and structured English developer prompts in Cursor, VS Code, Windsurf, and Terminal.</li>
        <li><b>Voice Snippets (Quick Triggers):</b> Define Bangla or English triggers (e.g., "আমার ইমেইল" or "meeting link") to instantly expand full emails, addresses, or links offline or online.</li>
        <li><b>Bangla-English Personal Dictionary:</b> Save custom names, brands, and technical terms once — sent directly to Gemini, OpenAI, and Smart Polish so spellings stay accurate.</li>
        <li><b>Bot-free Bangla-English Meeting Notes:</b> Record Zoom, Google Meet, or in-person meetings without any bot joining your call, and get structured summaries, key points, and action items with one-click Markdown copy.</li>
        <li><b>Unified Bangla &amp; Translation Settings:</b> Translation, Banglish, App-Aware Tone, Vibe Coding, and Smart Polish now live together in one clean card with live Gemini/offline status.</li>
        <li><b>Dynamic Onboarding &amp; Auto-Download:</b> Device-aware recommendations with a Single All-in-One model option and automatic background downloads on Continue.</li>
      </ul>
      <h2 id="v0-1-6">v0.1.6 · 2026-11-19</h2>
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
    ("Install", [
        ("/docs/macos", "macOS"),
        ("/docs/windows", "Windows"),
        ("/docs/linux", "Linux"),
        ("/docs/android", "Android (APK)"),
        ("/docs/ios", "iPhone / iOS (IPA)"),
    ]),
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

      <div class="note" style="border-left: 4px solid #8A2BE2; background: rgba(138, 43, 226, 0.05); padding: 18px 20px; border-radius: 8px; margin: 16px 0 24px;">
        <h3 style="margin-top:0; color: #8A2BE2; display: flex; align-items: center; gap: 8px;">
          <span>📱</span> Kothalipi Mobile (Wispr Flow Edition)
        </h3>
        <p>Looking for smartphone voice typing? Kothalipi is now available for Android and iPhone with <strong>Wispr Flow-style floating mic</strong>, custom voice keyboard, and real-time <strong>Bangla-to-English translation</strong>.</p>
        <p style="margin-bottom:14px">Speak in everyday Bangla over WhatsApp, Messenger, or Notes, and have fluent English or polished Bangla typed instantly at your cursor.</p>
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
          <a class="btn btn-primary btn-sm" href="/docs/android">Android Guide &amp; APK</a>
          <a class="btn btn-sm" style="background:#8A2BE2;color:#fff" href="/docs/ios">iOS Guide &amp; IPA</a>
          <a class="btn btn-sm" href="/download#mobile">Download APK / IPA</a>
        </div>
      </div>

      <h2>1. Install</h2>
      <p>Download from the <a href="/download">download page</a>, or use the terminal:</p>
      {code(INSTALL_SH, "macOS and Linux")}
      {code(INSTALL_PS, "Windows (PowerShell)")}
      <p>Platform guides: <a href="/docs/macos">macOS</a> · <a href="/docs/windows">Windows</a> · <a href="/docs/linux">Linux</a> · <a href="/docs/android">Android</a> · <a href="/docs/ios">iOS</a>.</p>
      <h2>2. Follow the setup</h2>
      <ol>
        <li><b>Permissions.</b> Allow the microphone. On a Mac, also allow Accessibility so Kothalipi can type into other apps. On Android, allow Floating Overlay and Accessibility.</li>
        <li><b>Choose how it listens.</b> <em>Offline</em> is free and private. <em>Cloud</em> uses your own Gemini or ChatGPT key and is the most accurate. Low-memory computers are steered to Cloud. See <a href="/docs/cloud">Cloud &amp; API keys</a>.</li>
        <li><b>Download the voice models.</b> Setup recommends the best Bangla and English model for your computer. In Cloud mode they are your offline backup.</li>
        <li><b>Check your keys.</b> On a Mac, Kothalipi spots macOS settings that steal the keys and opens the right page.</li>
        <li><b>Try it.</b> Hold the Bangla key, speak, let go.</li>
      </ol>
      <h2>3. Use it anywhere</h2>
      <table class="table"><tr><th>Platform</th><th>Trigger</th><th>What it does</th></tr>
        <tr><td>macOS</td><td><kbd>Right ⌘</kbd> (Bangla) · <kbd>fn</kbd> (English)</td><td>Types text directly at your cursor in any Mac application.</td></tr>
        <tr><td>Windows</td><td><kbd>Right Alt</kbd> (Bangla) · <kbd>Right Ctrl</kbd> (English)</td><td>Types text directly at your cursor in any Windows app.</td></tr>
        <tr><td>Linux</td><td><kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>B</kbd> · <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>E</kbd></td><td>Types through X11 or Wayland helper (wtype / ydotool).</td></tr>
        <tr><td>Android</td><td>Floating mic bubble or Voice keyboard</td><td>Dictates over WhatsApp, Messenger, Notes without switching keyboards.</td></tr>
        <tr><td>iPhone / iOS</td><td>Kothalipi Keyboard or Action Button</td><td>1-tap voice dictation with real-time translation and haptics.</td></tr></table>
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

    doc("/docs/cloud", "Cloud Mode & API Keys | Kothalipi Docs", "Step-by-step guide to getting free Google Gemini and Groq Whisper API keys for Kothalipi Desktop and Mobile, with automatic fallback to offline.", f"""
      <h1>Cloud &amp; API keys</h1>
      <p class="lead">Cloud mode sends your recording directly to the AI provider you choose using your own API key. It gives the highest accuracy for Bangla, Banglish, and live Bangla-to-English translation — completely free with Gemini and Groq.</p>

      <h2>How automatic fallback works</h2>
      <p>Kothalipi tries your configured engines in order: <b>Google Gemini → Groq Whisper (Free) → OpenAI → Offline</b>. If one provider hits its free rate limit, fails, or you lose internet, Kothalipi automatically switches to the next engine so your typing never stops.</p>

      <h2 id="gemini">1. Get a free Google Gemini API key (Recommended)</h2>
      <ol>
        <li>Open <a href="https://aistudio.google.com/apikey">Google AI Studio → API keys</a> and sign in with your Google account.</li>
        <li>Click <b>Create API key</b> and copy the key (starts with <code>AIzaSy...</code>).</li>
        <li><b>On Desktop:</b> Open <b>Settings → General → Listening</b> → choose <b>Cloud (your keys)</b> → paste under <b>Google Gemini</b> → click <b>Save</b>.</li>
        <li><b>On Mobile (Android / iOS):</b> Open <b>⚙️ Settings</b> → paste under <b>Google Gemini API Key</b> → tap <b>Test</b> → tap <b>Save</b>.</li>
      </ol>
      <p>Gemini includes a generous free tier with daily limits. Full walkthrough: <a href="/guides/free-gemini-api-key">Free Gemini API key guide →</a></p>

      <h2 id="groq">2. Get a free Groq Whisper API key (Ultra-Fast Backup)</h2>
      <ol>
        <li>Open <a href="https://console.groq.com/keys">console.groq.com/keys</a> and sign in with Google or GitHub (free, no card required).</li>
        <li>Click <b>Create API Key</b>, name it <code>Kothalipi</code>, and copy the key (starts with <code>gsk_...</code>).</li>
        <li><b>On Desktop (v0.1.8+):</b> Paste under <b>Groq Whisper (Free, Ultra-Fast)</b> in <b>Settings → General → Listening</b> and click <b>Save</b>.</li>
        <li><b>On Mobile (v0.2.0+):</b> Paste under <b>Groq Whisper Key</b> in <b>⚙️ Settings</b>, tap <b>Test</b>, and tap <b>Save</b>.</li>
      </ol>
      <p>Powered by <code>whisper-large-v3-turbo</code> on Groq LPUs for sub-second speed. Full walkthrough: <a href="/guides/free-groq-api-key">Free Groq Whisper key guide →</a></p>

      <h2 id="openai">3. Optional: Add an OpenAI (ChatGPT) key</h2>
      <ol>
        <li>Create a key at <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a> (paid per minute of audio).</li>
        <li>Paste it under <b>OpenAI (ChatGPT)</b> in Desktop or Mobile Settings and click <b>Save / Test</b>.</li>
      </ol>

      <h2 id="claude">What about Claude?</h2>
      <p>Claude does not take audio input, so it cannot turn speech into text. On Desktop, it can polish your text afterwards in <b>Settings → Post-Processing</b> with your Anthropic API key.</p>

      <h2>Privacy: where your keys and audio go</h2>
      <ul>
        <li>Your API keys are stored locally on your computer or phone and sent only to their respective provider.</li>
        <li>Audio goes straight from your device to Google, Groq, or OpenAI. Kothalipi has no middleman servers.</li>
        <li>Offline mode sends nothing anywhere.</li>
      </ul>
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

    doc("/docs/android", "Kothalipi on Android: Wispr Flow Floating Mic & Setup | Docs", "Install Kothalipi APK on Android, enable the Wispr Flow-style floating mic bubble over any app, and set up live Bangla to English voice translation.", f"""
      <h1>Android</h1>
      <p class="lead">Hands-free Bangla voice typing with a Wispr Flow-style floating mic bubble and voice keyboard. Works on Android 8.0 and newer.</p>
      <h2>1. Download and Install the APK</h2>
      <ol>
        <li>Download the latest release: <a class="btn btn-primary btn-sm" style="display:inline-flex;margin:4px 0" href="https://github.com/Kothalipi/kothalipi-mobile/releases/download/v0.2.0/Kothalipi-v0.2.0.apk">Download Kothalipi-v0.2.0.apk</a></li>
        <li>Open your browser's Downloads or Files app and tap <code>Kothalipi-v0.2.0.apk</code>.</li>
        <li>If prompted with <b>“For your security, your phone is not allowed to install unknown apps from this source”</b>, tap <b>Settings</b> and toggle on <b>Allow from this source</b>, then tap <b>Install</b>.</li>
      </ol>
      <div class="note"><p>You can also download the APK directly from our <a href="{DESK}/releases/tag/v0.1.6">Desktop Release page</a> or the <a href="/download#mobile">Download section</a>.</p></div>

      <h2>2. Enable the Wispr Flow Floating Bubble</h2>
      <p>The floating mic button is the most seamless way to dictate. You don't need to switch away from your favorite keyboard (like Ridmik or Gboard):</p>
      <ol>
        <li>Open the <b>Kothalipi</b> app.</li>
        <li>Tap <b>Enable Floating Bubble</b>. Android will take you to <b>Display over other apps</b>. Find Kothalipi and turn it <b>ON</b>.</li>
        <li>Tap <b>Enable Accessibility Service</b> and turn on <b>Kothalipi Accessibility Service</b>.</li>
      </ol>
      <div class="note"><p><b>Why Accessibility is needed:</b> Accessibility allows Kothalipi to automatically type your transcribed text right where your cursor is inside WhatsApp, Gmail, Facebook Messenger, Notes, or any browser.</p></div>

      <h2>3. (Optional) Enable Kothalipi Voice Keyboard</h2>
      <p>If you prefer an on-screen keyboard dictation experience:</p>
      <ol>
        <li>Go to <b>Settings → System → Languages &amp; input → On-screen keyboard → Manage on-screen keyboards</b>.</li>
        <li>Toggle on <b>Kothalipi Voice Keyboard</b>.</li>
        <li>Whenever typing in an app, tap the keyboard switcher icon at the bottom right to switch to Kothalipi.</li>
      </ol>

      <h2>4. Setup Free Gemini Key (Live Translation &amp; Polish)</h2>
      <p>Kothalipi comes with 3 killer mobile features powered by your personal Google Gemini API key:</p>
      <ul>
        <li><b>Bangla ➔ English Live Conversion:</b> Speak naturally in conversational Bangla (e.g., <i>“ভাই প্রজেক্টের কাজ শেষ, একটু দেখে ফিডব্যাক দিন”</i>) and it types fluent English (<i>“Brother, the project is completed. I would appreciate your feedback.”</i>).</li>
        <li><b>AI Smart Polish:</b> Strips filler words (<i>“উমম”</i>, <i>“মানে”</i>) and applies proper punctuation.</li>
        <li><b>100% Free &amp; Private:</b> Enter your free Gemini API key in app settings. Your voice and data never hit third-party tracking servers. Follow our <a href="/guides/free-gemini-api-key">free Gemini key guide</a> to grab one in 30 seconds.</li>
      </ul>

      <h2>Troubleshooting</h2>
      <ul>
        <li><b>Bubble disappears after restart:</b> Some Android brands (Xiaomi MIUI/HyperOS, Samsung OneUI, Realme) aggressively kill background services. In <b>App Info → Battery</b>, select <b>Unrestricted</b> / <b>Don't optimize</b>, and enable <b>Autostart</b>.</li>
        <li><b>Cursor doesn't receive text:</b> Make sure the Accessibility Service is active in Android Accessibility settings.</li>
      </ul>
    """, "Android (APK)")

    doc("/docs/ios", "Kothalipi on iPhone / iOS: Install & Setup | Docs", "Install Kothalipi on your physical iPhone using Xcode, AltStore or TrollStore, enable the Voice Keyboard extension, and map the Action Button.", f"""
      <h1>iPhone / iOS</h1>
      <p class="lead">Minimalist voice dictation for iPhone with a custom SwiftUI Voice Hub, system keyboard extension, 3 dictation modes (Bangla, English, and Bangla-to-English translation), and Action Button integration. Requires iOS 16.0 or newer.</p>

      <h2>1. Download the IPA &amp; Source Code</h2>
      <p>Download the latest iOS package: <a class="btn btn-primary btn-sm" style="display:inline-flex;margin:4px 0" href="https://github.com/Kothalipi/kothalipi-mobile/releases/download/v0.2.0/Kothalipi-v0.2.0.ipa">Download Kothalipi-v0.2.0.ipa</a></p>
      <p>Also available on the <a href="/download#mobile">Download page</a> and <a href="https://github.com/Kothalipi/kothalipi-mobile/releases/tag/v0.2.0">GitHub Releases (v0.2.0)</a>.</p>

      <h2>2. How to Install on your Physical iPhone (আপনার আসল আইফোনে ইনস্টল)</h2>
      <p>হ্যাঁ, ১০০% আপনার নিজের আইফোনে ইনস্টল করা যাবে! অ্যাপল কোনো পেইড ডেভেলপার অ্যাকাউন্ট ছাড়াই ব্যক্তিগত ব্যবহারের জন্য নিজের ফোনে অ্যাপ ইনস্টল করার সম্পূর্ণ সুযোগ দেয়। নিচে সবচেয়ে সহজ ৩টি উপায় দেওয়া হলো:</p>

      <h3>উপায় ১: সরাসরি আপনার Mac ও Xcode দিয়ে (সবচেয়ে সহজ ও ফ্রি ⭐️)</h3>
      <ol>
        <li>USB ক্যাবল দিয়ে আপনার আসল iPhone-টি Mac-এর সাথে কানেক্ট করুন।</li>
        <li>আইফোনের <b>Settings → Privacy &amp; Security → Developer Mode</b> অন করুন এবং ফোনটি একবার রিস্টার্ট দিন।</li>
        <li>আপনার Mac-এর টার্মিনালে এই কমান্ড দিয়ে Xcode ওপেন করুন:</li>
      </ol>
      {code("cd kothalipi-mobile/ios && xed .")}
      <ol start="4">
        <li>Xcode উইন্ডোর উপরে ডিভাইস ড্রপডাউনে "My Mac" বা সিমুলেটরের জায়গায় আপনার <b>কানেক্টেড iPhone</b> সিলেক্ট করুন।</li>
        <li><b>Signing &amp; Capabilities</b> ট্যাবে গিয়ে আপনার ব্যক্তিগত Apple ID (Personal Team) সিলেক্ট করুন (এটি সম্পূর্ণ ফ্রি)।</li>
        <li>উপরে <b>▶️ (Run)</b> বাটনে চাপুন বা কিবোর্ডে <kbd>Cmd</kbd>+<kbd>R</kbd> চাপুন।</li>
        <li>অ্যাপটি সরাসরি আপনার আইফোনে ইনস্টল হয়ে ওপেন হয়ে যাবে!</li>
      </ol>
      <div class="note"><p><b>প্রথমবার রান করার পর:</b> আইফোনের <b>Settings → General → VPN &amp; Device Management</b>-এ গিয়ে আপনার Apple ID-তে ট্যাপ করে <b>Trust</b> চাপুন।</p></div>

      <h3>উপায় ২: AltStore বা SideStore দিয়ে (ক্যাবল ছাড়া)</h3>
      <p>যদি কম্পিউটারের সাথে না লাগিয়ে নিজের ফোনেই সবসময় অ্যাপ ইনস্টল ও সাইডলোড রাখতে চান:</p>
      <ol>
        <li>আইফোনে <a href="https://altstore.io">AltStore</a> অথবা <a href="https://sidestore.io">SideStore</a> সেটআপ করে নিন।</li>
        <li>আমাদের রিলিজ পেইজ থেকে <code>Kothalipi-v0.2.0.ipa</code> ফাইলটি Safari দিয়ে ডাউনলোড করুন।</li>
        <li>AltStore অ্যাপে গিয়ে <b>My Apps → “+” বাটনে</b> চাপ দিয়ে ডাউনলোড করা IPA ফাইলটি সিলেক্ট করুন। আপনার নিজস্ব Apple ID দিয়ে অ্যাপটি সাইন হয়ে ফোনে ইনস্টল হয়ে যাবে।</li>
      </ol>

      <h3>উপায় ৩: Sideloadly দিয়ে (Windows / Mac)</h3>
      <ol>
        <li><a href="https://sideloadly.io">Sideloadly</a> ডাউনলোড করে ওপেন করুন এবং iPhone USB দিয়ে কানেক্ট করুন।</li>
        <li><code>Kothalipi-v0.2.0.ipa</code> ড্র্যাগ-অ্যান্ড-ড্রপ করে আপনার Apple ID দিয়ে <b>Start</b> ক্লিক করুন।</li>
        <li>ইনস্টল শেষে <b>Settings → General → VPN &amp; Device Management → Trust</b> করুন।</li>
      </ol>

      <h3>উপায় ৪: TrollStore (iOS 14.0 – 16.6.1)</h3>
      <p>যদি আপনার আইফোনে iOS 14.0 থেকে 16.6.1 এর মধ্যে থাকে এবং TrollStore ইনস্টল থাকে, তবে কোনো ৭ দিনের রিনিউয়াল ঝামেলা ছাড়াই পার্মানেন্টলি Kothalipi IPA এক ক্লিকে ইনস্টল করে আজীবন ব্যবহার করতে পারবেন।</p>

      <h2>3. ৪টি ডিকটেশন মোড + অফলাইন মোড</h2>
      <p>কথালিপি মোবাইল v0.2.0-এ রয়েছে এক ক্লিকে মোড পরিবর্তনের সুবিধা:</p>
      <ul>
        <li><b>🇧🇩 বাংলা:</b> আপনি মুখে যা বলবেন, তা খাঁটি বাংলা হরফে নিখুঁতভাবে টাইপ হবে।</li>
        <li><b>🇬🇧 English:</b> শুধুমাত্র ইংরেজিতে মুখে কথা বলে সরাসরি ইংলিশ টেক্সট টাইপ হবে।</li>
        <li><b>বাংলা ➔ 🇬🇧 English (Live Translation):</b> কথ্য বাংলায় স্বাভাবিকভাবে কথা বলবেন, আর ব্যাকরণগতভাবে নির্ভুল ইংরেজিতে টাইপ হয়ে যাবে।</li>
        <li><b>✨ Auto &amp; 📴 Offline Mode:</b> বাংলা-ইংরেজি অটো ডিটেক্ট এবং ইন্টারনেট/API Key ছাড়াই ফ্রি On-Device Offline ডিক্টেশন!</li>
      </ul>

      <h2>4. Enable the Voice Keyboard Extension</h2>
      <p>iOS অন্যান্য অ্যাপের ওপর ফ্লোটিং বাবল অনুমতি দেয় না, তাই কথালিপিতে রয়েছে আল্ট্রা-স্লিক ভয়েস কিবোর্ড এক্সটেনশন:</p>
      <ol>
        <li>iPhone <b>Settings → General → Keyboard → Keyboards</b> এ যান।</li>
        <li><b>Add New Keyboard…</b> এ ট্যাপ করে <b>Kothalipi</b> সিলেক্ট করুন।</li>
        <li>কিবোর্ড লিস্টে <b>Kothalipi</b> তে ট্যাপ করে <b>Allow Full Access</b> অন করে দিন।</li>
      </ol>
      <div class="note"><p><b>কেন Full Access প্রয়োজন:</b> iOS পলিসির কারণে কিবোর্ড এক্সটেনশন থেকে মাইক্রোফোন ও নেটওয়ার্ক রিকোয়েস্ট এক্সেস করতে "Full Access" লাগে। কথালিপি সম্পূর্ণ প্রাইভেট এবং কোনো কি-স্ট্রোক রেকর্ড বা সেন্ড করে না।</p></div>

      <h2>5. Action Button &amp; Back Tap (১-ক্লিক ট্রিগার)</h2>
      <p>যদি আপনার iPhone 15 Pro, 15 Pro Max, 16 বা 16 Pro থাকে, তবে পাশের <b>Action Button</b> টিকেই ভয়েস টাইপিং বাটনে রূপান্তর করতে পারবেন:</p>
      <ol>
        <li>iPhone-এর <b>Shortcuts</b> অ্যাপ ওপেন করুন।</li>
        <li><b>+</b> চাপুন, <b>“Open Kothalipi”</b> শর্টকাট যুক্ত করুন।</li>
        <li><b>Settings → Action Button</b>-এ গিয়ে <b>Shortcut</b> সিলেক্ট করে কথালিপি বেছে নিন।</li>
        <li>যেকোনো সময় অ্যাকশন বাটন এক চাপেই কথা বলা শুরু করতে পারবেন!</li>
      </ol>
      <div class="note"><p><b>অন্যান্য আইফোনের জন্য:</b> <b>Settings → Accessibility → Touch → Back Tap</b>-এ গিয়ে Double Tap-এ কথালিপি শর্টকাট সিলেক্ট করে রাখতে পারেন।</p></div>

      <h2>6. ফ্রি API Key সেটআপ (Gemini / Groq Whisper / OpenAI)</h2>
      <ol>
        <li>কথালিপি অ্যাপ ওপেন করে উপরে <b>⚙️ Settings</b> আইকনে ট্যাপ করুন।</li>
        <li><a href="https://aistudio.google.com/apikey">Google AI Studio</a> থেকে ফ্রি <b>Gemini API Key</b> এবং ব্যাকআপ হিসেবে <a href="https://console.groq.com/keys">Groq Console</a> থেকে ফ্রি <b>Groq Whisper Key</b> নিয়ে পেস্ট করুন (<a href="/docs/cloud">ধাপে ধাপে API Key গাইড →</a>)।</li>
        <li>প্রতিটি Key-এর পাশে <b>Test</b> চাপুন এবং <b>Save</b> করুন।</li>
        <li>ইন্টারনেট বা API Key ছাড়াই ব্যবহার করতে চাইলে হোম স্ক্রিনের <b>Offline</b> চিপটি অন করুন।</li>
      </ol>

      <h2>7. প্রো ফিচার (Snippets, Voice Edit ও Auto-Stop)</h2>
      <ul>
        <li><b>ভয়েস স্ন্যাপেট (Snippets ট্যাব):</b> <code>"আমার ঠিকানা বলো"</code> বা <code>"বিকাশ নম্বর"</code> সেভ করে রাখলে মুখে বলার সাথে সাথেই পুরো টেক্সট অটো পেস্ট হবে।</li>
        <li><b>Voice Edit (AI Rewrite):</b> কোনো টেক্সট টাইপ হওয়ার পর রেজাল্ট কার্ডের <b>Voice Edit</b> বাটনে ট্যাপ করে বলুন <i>"এটাকে ফর্মাল ইমেইল বানাও"</i> বা <i>"পয়েন্ট আকারে সাজাও"</i>।</li>
        <li><b>Hold-to-Talk &amp; Auto-Stop (VAD):</b> মাইক চেপে ধরে কথা বলে ছেড়ে দিলেই স্টপ হবে, অথবা <b>Auto-Stop</b> অন রাখলে ২ সেকেন্ড চুপ থাকলে অটোমেটিক টাইপ হয়ে যাবে।</li>
      </ul>
    """, "iPhone / iOS (IPA)")

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
