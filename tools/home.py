"""Home and download pages, English and Bangla."""
import json

from lib import *  # noqa: F401,F403

SHOTS = {
    "en": [
        ("listen", "Choose how it listens", "Offline for free and private, or Cloud with your own key. Low-memory computers are steered to Cloud.", "Kothalipi setup screen: choose between Offline (free) and Cloud (most accurate)", 1600, 1240),
        ("voices", "Models picked for your computer", "Setup reads your memory and chip, then marks the best Bangla and English model.", "Kothalipi setup screen listing Bangla and English voice models with a Best for this computer badge", 1600, 1240),
        ("keys", "Your keys, checked for conflicts", "On a Mac, Kothalipi spots settings that steal the keys and opens the right page to fix them.", "Kothalipi shortcut screen showing the Bangla and English keys and a macOS conflict warning", 1600, 1240),
        ("settings", "Everything in one calm place", "Change keys, listening mode, API keys and models any time.", "Kothalipi settings window showing the Bangla key, English key and listening mode", 1600, 1240),
    ],
    "bn": [
        ("listen", "কীভাবে শুনবে, বেছে নিন", "ফ্রি ও প্রাইভেট অফলাইন, অথবা নিজের কি দিয়ে ক্লাউড। কম মেমরির কম্পিউটারকে ক্লাউডের দিকে নিয়ে যাওয়া হয়।", "কথালিপির সেটআপ স্ক্রিন: অফলাইন (ফ্রি) ও ক্লাউডের মধ্যে বেছে নেওয়া", 1600, 1240),
        ("voices", "আপনার কম্পিউটারের জন্য বাছাই করা মডেল", "সেটআপ আপনার মেমরি ও চিপ দেখে সেরা বাংলা ও ইংরেজি মডেলে চিহ্ন দেয়।", "কথালিপির সেটআপ স্ক্রিনে বাংলা ও ইংরেজি ভয়েস মডেলের তালিকা", 1600, 1240),
        ("keys", "কি-তে সমস্যা আছে কি না, আগেই দেখে নেয়", "ম্যাকে কোনো সেটিং কি দখল করলে কথালিপি ধরে ফেলে, আর ঠিক পেজটা খুলে দেয়।", "কথালিপির কি স্ক্রিনে বাংলা ও ইংরেজি কি এবং macOS-এর সতর্কবার্তা", 1600, 1240),
        ("settings", "সবকিছু এক জায়গায়", "কি, শোনার ধরন, API কি আর মডেল, যখন খুশি বদলান।", "কথালিপির সেটিংস উইন্ডো", 1600, 1240),
    ],
}


def shots_html(lang):
    out = []
    for i, (name, cap_title, cap, alt, w, h) in enumerate(SHOTS[lang]):
        loading = "" if i == 0 else ' loading="lazy" decoding="async"'
        out.append(
            f'<figure class="shot"><div class="window"><div class="window-bar"><i></i><i></i><i></i><span>Kothalipi</span></div>'
            f'<img src="/assets/screens/{name}.webp" width="{w}" height="{h}" alt="{esc(alt)}"{loading}></div>'
            f'<figcaption><b>{esc(cap_title)}.</b> {esc(cap)}</figcaption></figure>'
        )
    return '<div class="shots">' + "".join(out) + "</div>"


EN_FAQ = [
    ("Is Kothalipi really free?", "Yes. It is free and open source under the MIT license, with no account, trial or card. Offline mode costs nothing to run. Cloud mode uses your own API key: Google Gemini has a free tier with daily limits, and OpenAI bills per minute of audio."),
    ("Can Kothalipi translate Bangla voice to English text?", "Yes! Speak naturally in Bangla and Kothalipi translates your speech in real time into fluent, grammatically polished English before pasting it into any app. With a free Google Gemini API key it works instantly with any model — or use Whisper Large v3 for 100% offline translation."),
    ("What is Vibe Coding Mode and App-Aware Tone?", "App-Aware Tone detects the app you are typing into — keeping WhatsApp/Messenger casual, Mail/Docs formal, and automatically switching to Vibe Coding Mode in Cursor, VS Code, Windsurf, or Terminal so your spoken Bangla/Banglish ideas become clean English developer prompts."),
    ("Does Kothalipi support Voice Snippets and Bot-free Meeting Notes?", "Yes (v0.1.7)! Define Voice Snippets in Bangla or English (like 'আমার ইমেইল' → your email address) for instant expansion, and use the built-in Bot-free Meeting Notes tab to record Zoom/Google Meet calls and generate Bangla-English summaries and action items."),
    ("Does Bangla voice typing work offline?", "Yes. Offline mode runs a Bangla speech model on your computer, so it works without internet and your voice never leaves the machine. You download the model once (about 810 MB)."),
    ("How accurate is it for Bangla?", "It depends on the model. The recommended offline model, Qwen3-ASR 0.6B Bangla, was trained on 1,174 hours of Bangla speech and its authors report 14.74% word error rate and 5.34% character error rate on their own test set. Cloud mode with Google Gemini is usually best when you mix Bangla and English. We are building a public benchmark and will publish results."),
    ("Can I mix Bangla and English in one sentence?", "Yes, that is a design goal. Use the Bangla key for sentences with English words in them. Cloud mode handles mixed speech best."),
    ("Which computers does it run on?", "macOS 10.15 or later (Apple Silicon and Intel), Windows 10 and 11 (x64 and ARM) and Linux (.deb, .rpm and AppImage; X11 and Wayland). Android and iOS keyboards are planned."),
    ("Where do my recordings go?", "In offline mode, nowhere: audio is turned into text on your computer. In cloud mode, a recording is sent only to the provider whose key you added (Google or OpenAI), never to Kothalipi. Kothalipi has no servers, accounts or analytics."),
    ("Do I need an API key?", "Only for cloud mode. Offline mode needs no key. Get a free Gemini key in about a minute: see the free Gemini API key guide."),
    ("What happens when my API limit runs out or I lose internet?", "Kothalipi tries your engines in order (Gemini, then OpenAI) and then falls back to the offline model automatically, so dictation keeps working."),
    ("Does it work in every app?", "It types where your cursor is, so it works in chat apps, email, browsers, documents and code editors. Some apps running as administrator (Windows) or with secure input (macOS) can block typing."),
    ("Who makes Kothalipi?", "Kothalipi is made by TA Shanto in Bangladesh. The speech engine began from the open-source Handy project by CJ Pais (MIT); see the credits."),
]
BN_FAQ = [
    ("কথালিপি কি সত্যিই ফ্রি?", "হ্যাঁ। MIT লাইসেন্সে ফ্রি ও ওপেন সোর্স। অ্যাকাউন্ট, ট্রায়াল বা কার্ড লাগে না। অফলাইন মোড চালাতে কোনো খরচ নেই। ক্লাউড মোডে আপনার নিজের API কি লাগে: Google Gemini-র দৈনিক সীমাসহ ফ্রি ব্যবহার আছে, আর OpenAI অডিওর মিনিট ধরে চার্জ করে।"),
    ("কথালিপি কি মুখে বলা বাংলা সরাসরি ইংরেজিতে অনুবাদ করতে পারে?", "হ্যাঁ! বাংলায় স্বাভাবিকভাবে কথা বললে কথালিপি তাৎক্ষণিকভাবে তা সাবলীল ও শুদ্ধ ইংরেজিতে অনুবাদ করে আপনার অ্যাপে টাইপ করে দেয়। ফ্রি Google Gemini API কি থাকলে কোনো বড় মডেল ছাড়াই চলে, আর অফলাইনে Whisper Large v3 দিয়েও অনুবাদ করা যায়।"),
    ("Vibe Coding মোড এবং অ্যাপ অনুযায়ী টোন কী?", "অ্যাপ অনুযায়ী টোন নিজেই চিনে নেয় আপনি কোন অ্যাপে লিখছেন — WhatsApp/Messenger-এ স্বাভাবিক বাংলিশ, Mail/Docs-এ প্রফেশনাল ফর্মাল, আর Cursor, VS Code বা Terminal-এ বাংলায় বললে ক্লিন ইংরেজি ডেভেলপার প্রম্পট বানিয়ে পেস্ট করে দেয়।"),
    ("ভয়েস স্নিপেট ও বট-মুক্ত মিটিং নোট কীভাবে কাজ করে?", "v0.1.7-এ আপনি 'আমার ইমেইল' বা 'meeting link'-এর মতো শর্ট ট্রিগার সেট করলে সাথে সাথে পুরো লেখা পেস্ট হবে। আর মিটিং নোট ট্যাবে কোনো বট ছাড়াই Zoom/Google Meet রেকর্ড করে বাংলা-ইংরেজি সামারি ও Action Items পাবেন।"),
    ("ইন্টারনেট ছাড়া কি বাংলা ভয়েস টাইপিং চলে?", "হ্যাঁ। অফলাইন মোডে বাংলা স্পিচ মডেল আপনার কম্পিউটারেই চলে, তাই ইন্টারনেট লাগে না আর আপনার কণ্ঠ কম্পিউটার ছেড়ে যায় না। মডেলটা একবার ডাউনলোড করতে হয় (প্রায় ৮১০ MB)।"),
    ("বাংলায় কতটা নির্ভুল?", "মডেলের উপর নির্ভর করে। সুপারিশ করা অফলাইন মডেল Qwen3-ASR 0.6B Bangla ১,১৭৪ ঘণ্টা বাংলা কথায় ট্রেইন করা, আর এর নির্মাতারা নিজেদের টেস্ট সেটে ১৪.৭৪% WER ও ৫.৩৪% CER জানিয়েছেন। বাংলা-ইংরেজি মিশিয়ে বললে সাধারণত Google Gemini দিয়ে ক্লাউড মোড সবচেয়ে ভালো। আমরা একটা পাবলিক বেঞ্চমার্ক বানাচ্ছি, ফল প্রকাশ করব।"),
    ("এক বাক্যে বাংলা আর ইংরেজি মেশানো যায়?", "হ্যাঁ, এটা আমাদের মূল লক্ষ্য। ইংরেজি শব্দসহ বাক্যের জন্য বাংলা কি ব্যবহার করুন। মেশানো কথায় ক্লাউড মোড সবচেয়ে ভালো কাজ করে।"),
    ("কোন কম্পিউটারে চলে?", "macOS 10.15 বা নতুন (Apple Silicon ও Intel), Windows 10 ও 11 (x64 ও ARM), আর Linux (.deb, .rpm ও AppImage; X11 ও Wayland)। Android ও iOS কিবোর্ড পরিকল্পনায় আছে।"),
    ("আমার রেকর্ডিং কোথায় যায়?", "অফলাইন মোডে কোথাও না, কণ্ঠ আপনার কম্পিউটারেই লেখায় বদলায়। ক্লাউড মোডে শুধু আপনার কি দেওয়া প্রোভাইডারের (Google বা OpenAI) কাছে যায়, কথালিপির কাছে কখনো না। কথালিপির কোনো সার্ভার, অ্যাকাউন্ট বা অ্যানালিটিক্স নেই।"),
    ("API কি কি লাগবেই?", "শুধু ক্লাউড মোডে। অফলাইন মোডে কোনো কি লাগে না। ফ্রি Gemini কি নিতে এক মিনিটের মতো লাগে: ফ্রি Gemini API কি গাইডটা দেখুন।"),
    ("API-র সীমা শেষ হলে বা ইন্টারনেট চলে গেলে কী হয়?", "কথালিপি আপনার ইঞ্জিনগুলো ক্রমে চেষ্টা করে (আগে Gemini, তারপর OpenAI), শেষে নিজে থেকেই অফলাইন মডেলে চলে যায়। তাই লেখা থামে না।"),
    ("সব অ্যাপে কাজ করে?", "কার্সর যেখানে সেখানেই লেখে, তাই চ্যাট অ্যাপ, ইমেইল, ব্রাউজার, ডকুমেন্ট ও কোড এডিটরে চলে। Windows-এ অ্যাডমিন হিসেবে চলা বা macOS-এ সিকিউর ইনপুট চালু থাকা অ্যাপে লেখা আটকে যেতে পারে।"),
    ("কথালিপি কে বানিয়েছেন?", "কথালিপি বাংলাদেশে TA Shanto-র তৈরি। স্পিচ ইঞ্জিনের শুরুটা CJ Pais-এর ওপেন সোর্স Handy প্রজেক্ট (MIT) থেকে; কৃতজ্ঞতা পেজ দেখুন।"),
]


def home(lang):
    en = lang == "en"
    dl = "/download" if en else "/bn/download"
    faq = EN_FAQ if en else BN_FAQ
    labels = json.dumps({"mac": "Download for Mac", "windows": "Download for Windows", "linux": "Download for Linux"} if en else {"mac": "ম্যাকের জন্য ডাউনলোড", "windows": "উইন্ডোজের জন্য ডাউনলোড", "linux": "লিনাক্সের জন্য ডাউনলোড"}, ensure_ascii=False)
    t = dict(
        eyebrow="Free · Open source · Works offline" if en else "ফ্রি · ওপেন সোর্স · অফলাইনে চলে",
        h1="Speak Bangla.<br><span class='grad'>It's written.</span>" if en else "বাংলায় বলুন।<br><span class='grad'>লেখা হয়ে যাবে।</span>",
        lead="Kothalipi is free voice typing for Bangla and English on Mac, Windows and Linux. Hold a key, speak, let go, and your words appear in any app." if en else "কথালিপি ম্যাক, উইন্ডোজ ও লিনাক্সের জন্য ফ্রি বাংলা ও ইংরেজি ভয়েস টাইপিং। একটা কি চেপে ধরে বলুন, ছেড়ে দিন, যেকোনো অ্যাপে লেখা চলে আসবে।",
        cta1="Download for free" if en else "ফ্রি ডাউনলোড",
        cta2="See how it works" if en else "কীভাবে কাজ করে দেখুন",
        trust=["MIT open source", "No account", "Works offline", "Gemini or ChatGPT optional"] if en else ["MIT ওপেন সোর্স", "অ্যাকাউন্ট লাগে না", "অফলাইনে চলে", "Gemini বা ChatGPT ঐচ্ছিক"],
    )
    dl_trust = f"<li>{ICON['check']}<strong data-total-downloads>280+</strong> {'downloads' if en else 'ডাউনলোড'}</li>"
    trust = dl_trust + "".join(f"<li>{ICON['check']}{esc(x)}</li>" for x in t["trust"])
    hold = "Hold to speak" if en else "চেপে ধরে বলুন"
    note = "Preview only. In the app you hold a key and your real words appear." if en else "এটা শুধু প্রিভিউ। অ্যাপে কি চেপে ধরলে আপনার আসল কথা লেখা হয়।"
    win_label = "Messages" if en else "মেসেজ"
    meta_label = "To: Rafi" if en else "প্রতি: রাফি"

    steps = (
        [("1", "Hold a key", "Hold Right ⌘ for Bangla or fn for English. On Windows: Right Alt and Right Ctrl."),
         ("2", "Speak naturally", "Talk the way you talk. Mixing Bangla and English in one sentence is normal."),
         ("3", "Let go", "Your words appear where your cursor is: chat, email, documents, code editors.")]
        if en else
        [("১", "কি চেপে ধরুন", "বাংলার জন্য Right ⌘, ইংরেজির জন্য fn। Windows-এ Right Alt আর Right Ctrl।"),
         ("২", "স্বাভাবিকভাবে বলুন", "যেভাবে কথা বলেন সেভাবেই বলুন। এক বাক্যে বাংলা-ইংরেজি মেশানো একদম স্বাভাবিক।"),
         ("৩", "ছেড়ে দিন", "কার্সর যেখানে, লেখা সেখানে: চ্যাট, ইমেইল, ডকুমেন্ট, কোড এডিটর।")]
    )
    steps_html = "".join(f'<div class="step"><div class="n">{n}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for n, h, p in steps)

    new_badge = (
        '<a class="new-badge" href="/changelog"><b>v0.1.8 · Mobile v0.2.0</b> <span>✨ Free Groq Whisper, Voice Edit &amp; Offline</span></a><br>'
        if en
        else '<a class="new-badge" href="/changelog"><b>v0.1.8 · মোবাইল v0.2.0</b> <span>✨ ফ্রি Groq Whisper, Voice Edit ও অফলাইন</span></a><br>'
    )

    if en:
        bento = f"""
      <div class="bento">
        <article class="tile translation-tile s4"><span class="tag">✨ Desktop v0.1.8 &amp; Mobile v0.2.0</span><h3>Bangla, Natural Banglish, Live Translation &amp; AI Voice Edit</h3>
          <p>Speak Bangla with English words mixed in — Kothalipi keeps English terms in proper English automatically. Plus real-time Bangla→English translation, <b>Voice Edit Commands</b> ("make this a formal email"), App-Aware Tone, Vibe Coding prompts, Voice Snippets, and Bot-free Meeting Notes.</p>
          <div class="flow" role="img" aria-label="Bangla speech with English words and live translation"><span class="chip chip-spoken">🗣️ "কালকে meeting-এ project review করব"</span><span class="arrow">→</span><span class="chip chip-translated">✍️ Proper Banglish / Fluent English</span></div></article>
        <article class="tile s2"><span class="tag">📱 Mobile v0.2.0 · Android &amp; iOS</span><h3>Floating Bubble &amp; iOS Keyboard</h3><p>Dictate over WhatsApp, Messenger &amp; Notes with Hold-to-Talk, 2s Auto-Stop (VAD), Voice Edit, and 0-MB Free Offline Mode. <a href="/download#mobile">Get Mobile →</a></p></article>
        <article class="tile accent s4"><span class="tag">Multi-AI + Free Offline Fallback</span><h3>Free Gemini + Free Groq Whisper + Offline. Never hits a wall.</h3>
          <p>Bring your own free <b>Gemini</b> and <b>Groq Whisper</b> (<code>whisper-large-v3-turbo</code>) keys, or optional OpenAI. If a free quota runs out or internet drops, Kothalipi automatically falls back to the next engine or 100% free Offline mode.</p>
          <div class="flow" role="img" aria-label="Fallback order: Gemini, Groq Whisper, then Offline"><span class="chip">Gemini (Free)</span><span class="arrow">→</span><span class="chip">Groq Whisper (Free)</span><span class="arrow">→</span><span class="chip">Offline</span></div></article>
        <article class="tile s2"><span class="tag">⚡ Voice Snippets &amp; Shortcuts</span><h3>Say a trigger, paste full text</h3><p>Say "আমার ঠিকানা বলো" or "বিকাশ নম্বর" to instantly paste saved addresses, links, or templates on Desktop &amp; Mobile.</p></article>
        <article class="tile s2"><span class="tag">🎯 App-Aware &amp; Vibe Coding</span><h3>Adapts to every app</h3><p>Casual Banglish in WhatsApp, formal in Mail, and clean English developer prompts in Cursor, VS Code &amp; Terminal.</p></article>
        <article class="tile s2"><span class="tag">📝 Meeting Notes</span><h3>Bot-free Bangla-English notes</h3><p>Record Zoom or Google Meet without any bot joining. Get AI summary, key points, and action items in Markdown.</p></article>
        <article class="tile s2"><span class="tag">Two languages</span><h3>One key for each</h3><p>The key decides the language and the model for that recording.</p>
          <div class="keys-row"><span class="keycap">Right ⌘ <small class="muted">বাংলা</small></span><span class="keycap fn">fn <small class="muted">English</small></span></div></article>
        <article class="tile s2"><span class="tag">Smart setup</span><h3>Models for your device</h3><p>Desktop setup reads your memory and chip and picks the best fit automatically.</p>
          <div class="devcard"><b>Apple M2 · 16 GB</b><span class="ok">Best for this computer</span><br>Qwen3-ASR 0.6B Bangla · Parakeet 0.6B</div></article>
        <article class="tile s2"><span class="tag">Private</span><h3>No account, no tracking</h3><p>Offline audio never leaves your device. Kothalipi has no servers and no analytics.</p></article>
        <article class="tile s2"><span class="tag">Open</span><h3>Open source, MIT</h3><p>Read the code, report a wrong word, or help add your language.</p></article>
      </div>"""
        sec = dict(
            how_h="Hold. Speak. Let go.", how_p="That is the whole app.",
            feat_h="Built for the way Bangla is really written", feat_p="Two keys, Bangla-trained models, and a setup that does the hard parts for you.",
            see_h="See it", see_p="Real screens from the app.",
            inst_h="Install in one line", inst_p="Or download the installer. Setup takes about two minutes.",
            models_h="Bangla-trained models, not an afterthought", models_p="Stock speech models struggle with Bangla. Kothalipi ships models trained on it and lets you compare them.",
            plat_h="On every computer you use", faq_h="Questions", band_h="Start writing Bangla with your voice", band_p="Free, open source and ready in two minutes.",
            models_link="Models and accuracy →", guide_link="Read the setup guides",
        )
    else:
        bento = f"""
      <div class="bento">
        <article class="tile translation-tile s4"><span class="tag">✨ Desktop v0.1.8 ও Mobile v0.2.0</span><h3>বাংলার মাঝে প্রপার ইংরেজি, লাইভ অনুবাদ ও Voice Edit</h3>
          <p>বাংলায় কথা বলার সময় মাঝে যে ইংরেজি শব্দ বলবেন, তা স্বয়ংক্রিয়ভাবে সঠিক ইংরেজি অক্ষরে বসবে। সাথে আছে রিয়েল-টাইম বাংলা→ইংরেজি অনুবাদ, <b>Voice Edit কমান্ড</b> ("এটাকে ফর্মাল ইমেইল বানাও"), অ্যাপ অনুযায়ী টোন, Vibe Coding, ভয়েস স্নিপেট ও বট-মুক্ত মিটিং নোট।</p>
          <div class="flow" role="img" aria-label="বাংলা ও ইংরেজি একসাথে এবং লাইভ অনুবাদ"><span class="chip chip-spoken">🗣️ "কালকে meeting-এ project review করব"</span><span class="arrow">→</span><span class="chip chip-translated">✍️ নিখুঁত বাংলিশ / সাবলীল ইংরেজি</span></div></article>
        <article class="tile s2"><span class="tag">📱 Mobile v0.2.0 · Android ও iOS</span><h3>ফ্লোটিং বাবল ও iOS কীবোর্ড</h3><p>WhatsApp, Messenger ও Notes-এ Hold-to-Talk, ২ সেকেন্ড Auto-Stop (VAD), Voice Edit ও ফ্রি অফলাইন মোড। <a href="/bn/download#mobile">মোবাইল ডাউনলোড →</a></p></article>
        <article class="tile accent s4"><span class="tag">Multi-AI + ফ্রি অফলাইন ফলব্যাক</span><h3>ফ্রি Gemini + ফ্রি Groq Whisper + অফলাইন। লেখা কখনো থামবে না।</h3>
          <p>আপনার নিজের ফ্রি <b>Gemini</b> এবং সুপার-ফাস্ট <b>Groq Whisper</b> (<code>whisper-large-v3-turbo</code>) কি ব্যবহার করুন। একটার কোটা শেষ হলে বা নেট না থাকলে অটোমেটিক পরের ইঞ্জিন বা ১০০% ফ্রি অফলাইন মোডে চলবে।</p>
          <div class="flow" role="img" aria-label="ক্রম: Gemini, Groq Whisper, তারপর অফলাইন"><span class="chip">Gemini (ফ্রি)</span><span class="arrow">→</span><span class="chip">Groq Whisper (ফ্রি)</span><span class="arrow">→</span><span class="chip">অফলাইন</span></div></article>
        <article class="tile s2"><span class="tag">⚡ ভয়েস স্নিপেট ও শর্টকাট</span><h3>ট্রিগার বললেই পুরো টেক্সট পেস্ট</h3><p>"আমার ঠিকানা বলো" বা "বিকাশ নম্বর" বললেই সেভ করা পুরো লেখা অটো পেস্ট হবে ডেস্কটপ ও মোবাইলে।</p></article>
        <article class="tile s2"><span class="tag">🎯 অ্যাপ টোন ও Vibe Coding</span><h3>প্রতিটি অ্যাপে মানানসই স্টাইল</h3><p>WhatsApp-এ স্বাভাবিক বাংলিশ, Mail-এ ফর্মাল, আর Cursor/VS Code-এ বাংলায় বললে ক্লিন ইংরেজি ডেভেলপার প্রম্পট।</p></article>
        <article class="tile s2"><span class="tag">📝 মিটিং নোট</span><h3>বট-মুক্ত বাংলা-ইংরেজি নোট</h3><p>কোনো বট ছাড়াই Zoom বা Google Meet রেকর্ড করে বাংলা-ইংরেজি সামারি, মূল পয়েন্ট ও Action Items পান।</p></article>
        <article class="tile s2"><span class="tag">দুই ভাষা</span><h3>প্রতি ভাষায় একটা কি</h3><p>কি-ই ঠিক করে ওই রেকর্ডিংয়ের ভাষা ও মডেল।</p>
          <div class="keys-row"><span class="keycap">Right ⌘ <small class="muted">বাংলা</small></span><span class="keycap fn">fn <small class="muted">English</small></span></div></article>
        <article class="tile s2"><span class="tag">স্মার্ট সেটআপ</span><h3>আপনার ডিভাইসের মডেল</h3><p>ডেস্কটপ সেটআপ আপনার মেমরি ও চিপ দেখে সবচেয়ে মানানসই মডেল বাছে।</p>
          <div class="devcard"><b>Apple M2 · 16 GB</b><span class="ok">এই কম্পিউটারের জন্য সেরা</span><br>Qwen3-ASR 0.6B Bangla · Parakeet 0.6B</div></article>
        <article class="tile s2"><span class="tag">প্রাইভেট</span><h3>অ্যাকাউন্ট নেই, ট্র্যাকিং নেই</h3><p>অফলাইনে অডিও ডিভাইস ছেড়ে যায় না। কথালিপির কোনো সার্ভার বা অ্যানালিটিক্স নেই।</p></article>
        <article class="tile s2"><span class="tag">উন্মুক্ত</span><h3>ওপেন সোর্স, MIT</h3><p>কোড পড়ুন, ভুল শব্দ জানান, বা নিজের ভাষা যোগ করতে সাহায্য করুন।</p></article>
      </div>"""
        sec = dict(
            how_h="চাপুন। বলুন। ছাড়ুন।", how_p="পুরো অ্যাপটাই এই তিন ধাপ।",
            feat_h="বাংলা যেভাবে সত্যিই লেখা হয়, সেভাবে বানানো", feat_p="দুটো কি, বাংলায় ট্রেইন করা মডেল, আর কঠিন কাজগুলো নিজে করে দেওয়া সেটআপ।",
            see_h="নিজের চোখে দেখুন", see_p="অ্যাপের আসল স্ক্রিন।",
            inst_h="এক লাইনে ইনস্টল", inst_p="অথবা ইনস্টলার ডাউনলোড করুন। সেটআপে প্রায় দুই মিনিট লাগে।",
            models_h="বাংলায় ট্রেইন করা মডেল, শুধু নামকাওয়াস্তে নয়", models_p="সাধারণ স্পিচ মডেল বাংলায় দুর্বল। কথালিপি বাংলায় ট্রেইন করা মডেল দেয় এবং আপনাকে তুলনা করতে দেয়।",
            plat_h="আপনার সব কম্পিউটারে", faq_h="প্রশ্ন", band_h="আজই কণ্ঠ দিয়ে বাংলা লেখা শুরু করুন", band_p="ফ্রি, ওপেন সোর্স, আর দুই মিনিটেই তৈরি।",
            models_link="মডেল ও নির্ভুলতা →", guide_link="সেটআপ গাইড পড়ুন",
        )

    plat = (
        [("macOS", "Apple Silicon & Intel", True), ("Windows", "10 & 11 · x64 & ARM", True), ("Linux", ".deb · .rpm · AppImage", True), ("Android", "Wispr Flow APK", True), ("iOS", "SwiftUI IPA", True)]
        if en else
        [("macOS", "Apple Silicon ও Intel", True), ("Windows", "10 ও 11 · x64 ও ARM", True), ("Linux", ".deb · .rpm · AppImage", True), ("Android", "ফ্লোটিং APK", True), ("iOS", "সুইফট IPA", True)]
    )
    plat_html = "".join(f'<div class="platform{"" if ok else " soon"}"><b>{n}</b><span class="{"ok" if ok else ""}">{esc(d)}</span></div>' for n, d, ok in plat)

    body = f"""
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <span class="eyebrow"><i></i>{esc(t["eyebrow"])}</span><br>
          {new_badge}
          <h1>{t["h1"]}</h1>
          <p class="lead">{esc(t["lead"])}</p>
          <div class="cta">
            <a class="btn btn-primary btn-lg" id="hero-download" data-dl data-labels='{labels}' href="{dl}">{ICON["download"]}<span id="hero-download-label">{esc(t["cta1"])}</span></a>
            <a class="btn btn-secondary btn-lg" href="#how">{esc(t["cta2"])}</a>
          </div>
          <div class="after-dl" id="after-dl"></div>
          <p class="kbd-hint">{'Shortcut: press <kbd>D</kbd> to download' if en else 'শর্টকাট: ডাউনলোডের জন্য <kbd>D</kbd> চাপুন'}</p>
          <ul class="trust">{trust}</ul>
        </div>
        <div class="stage" aria-label="{'Interactive preview' if en else 'ইন্টারঅ্যাকটিভ প্রিভিউ'}">
          <div class="demo-tabs" role="tablist"><button role="tab" aria-selected="true" data-mode="bn" class="on">বাংলা</button><button role="tab" aria-selected="false" data-mode="en">English</button></div>
          <div class="demo-win">
            <div class="window">
              <div class="window-bar"><i></i><i></i><i></i><span>{win_label}</span></div>
              <div class="window-body"><p class="meta">{meta_label}</p><p class="typed" id="typed"><span class="cursor"></span></p></div>
            </div>
            <div class="pill-rec" id="pill" aria-hidden="true"><span class="dot"></span><span class="bars"><b></b><b></b><b></b><b></b><b></b><b></b></span><span id="pill-lang">BN</span></div>
          </div>
          <button class="holdbtn" id="hold" type="button">{hold} <kbd id="hold-key">Right ⌘</kbd></button>
          <p class="demo-note">{esc(note)}</p>
        </div>
      </div>
    </section>

    <section class="section" id="how">
      <div class="container">
        <div class="section-head"><h2>{esc(sec["how_h"])}</h2><p>{esc(sec["how_p"])}</p></div>
        <div class="steps">{steps_html}</div>
      </div>
    </section>

    <section class="section tint" id="features">
      <div class="container">
        <div class="section-head"><h2>{esc(sec["feat_h"])}</h2><p>{esc(sec["feat_p"])}</p></div>
        {bento}
      </div>
    </section>

    <section class="section" id="screens">
      <div class="container">
        <div class="section-head"><h2>{esc(sec["see_h"])}</h2><p>{esc(sec["see_p"])}</p></div>
        {shots_html(lang)}
      </div>
    </section>

    <section class="section tint" id="install">
      <div class="container">
        <div class="section-head"><h2>{esc(sec["inst_h"])}</h2><p>{esc(sec["inst_p"])}</p></div>
        <div class="tabs doc" style="margin:0 auto">
          <div role="tablist" aria-label="{'Operating system' if en else 'অপারেটিং সিস্টেম'}"><button role="tab" data-tab="mac" aria-selected="true">macOS</button><button role="tab" data-tab="linux" aria-selected="false">Linux</button><button role="tab" data-tab="windows" aria-selected="false">Windows</button></div>
          <div role="tabpanel" data-panel="mac">{code(INSTALL_SH)}</div>
          <div role="tabpanel" data-panel="linux">{code(INSTALL_SH)}</div>
          <div role="tabpanel" data-panel="windows">{code(INSTALL_PS)}</div>
          <p class="muted" style="margin-top:14px"><a href="{dl}">{'Or download the installer' if en else 'অথবা ইনস্টলার ডাউনলোড করুন'}</a> · <a href="/guides/">{esc(sec["guide_link"])}</a></p>
        </div>
      </div>
    </section>

    <section class="section" id="models">
      <div class="container">
        <div class="section-head"><h2>{esc(sec["models_h"])}</h2><p>{esc(sec["models_p"])}</p>
          <p style="margin-top:18px"><a class="btn btn-secondary" href="/models">{esc(sec["models_link"])}</a></p></div>
        <div class="section-head" style="margin-bottom:28px"><h3>{esc(sec["plat_h"])}</h3></div>
        <div class="platforms">{plat_html}</div>
      </div>
    </section>

    <section class="section tint" id="faq">
      <div class="container">
        <div class="section-head"><h2>{esc(sec["faq_h"])}</h2></div>
        <div class="faq">{faq_html(faq)}</div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="band">
          <h2>{esc(sec["band_h"])}</h2><p>{esc(sec["band_p"])}</p>
          <div class="cta" style="justify-content:center"><a class="btn btn-primary btn-lg" data-dl href="{dl}">{ICON["download"]}{esc(t["cta1"])}</a><a class="btn btn-secondary btn-lg" href="/docs/">{'Read the docs' if en else 'ডকুমেন্টেশন পড়ুন'}</a></div>
        </div>
      </div>
    </section>"""

    if en:
        title = "Kothalipi: Free Bangla & English Voice Typing for Mac, Windows, Linux"
        desc = "Free, open-source Bangla and English voice typing. Hold a key, speak, and text appears in any app. Works offline; optional Gemini or ChatGPT cloud."
    else:
        title = "কথালিপি: ফ্রি বাংলা ও ইংরেজি ভয়েস টাইপিং, ম্যাক, উইন্ডোজ ও লিনাক্সে"
        desc = "ফ্রি ও ওপেন সোর্স বাংলা ও ইংরেজি ভয়েস টাইপিং। কি চেপে বলুন, যেকোনো অ্যাপে লেখা চলে আসবে। অফলাইনে চলে; চাইলে Gemini বা ChatGPT ক্লাউড।"
    schema = [app_schema(lang), website_schema(), faq_schema([(q, a) for q, a in faq])]
    page("/" if en else "/bn/", title, desc, body, lang=lang, alt={"en": "/", "bn": "/bn/"},
         schema=schema, priority="1.0", changefreq="weekly",
         preload=["/assets/fonts/hind-siliguri-latin-700.woff2"] if en else ["/assets/fonts/hind-siliguri-bengali-700.woff2"])


def download(lang):
    en = lang == "en"
    path = "/download" if en else "/bn/download"
    labels = json.dumps({"mac": "Download for Mac", "windows": "Download for Windows", "linux": "Download for Linux"} if en else {"mac": "ম্যাকের জন্য ডাউনলোড", "windows": "উইন্ডোজের জন্য ডাউনলোড", "linux": "লিনাক্সের জন্য ডাউনলোড"}, ensure_ascii=False)
    if en:
        h1, lead = "Download Kothalipi", f"Free for macOS, Windows and Linux. Version <span data-version>v{VERSION}</span>."
        loading, soon = "Finding the latest version…", "The first release is on its way. Watch the project on GitHub to get it."
        main_label = "Download"
        os_h = [("macOS", "macOS 10.15 or later."), ("Windows", "Windows 10 or 11."), ("Linux", "X11 and Wayland.")]
        term_h, term_p = "Install from the terminal", "One line. It downloads the latest release from GitHub and installs it."
        mac_l, win_l = "macOS and Linux", "Windows (PowerShell)"
        req_h = "Requirements"
        req = [("macOS", "10.15 or later, Apple Silicon or Intel. About 1 GB free for the Bangla model."), ("Windows", "Windows 10 or 11, 64-bit or ARM. About 1 GB free for the Bangla model."), ("Linux", "A recent 64-bit distribution with GTK 3 and ALSA or PipeWire. Wayland needs <code>wtype</code> or <code>ydotool</code>."), ("Memory", "8 GB recommended for offline mode. With 4 GB, use Cloud mode.")]
        unsigned = "<b>Early releases are not code-signed yet.</b> macOS and Windows may show a warning the first time. It is safe to continue, and the guides show how: <a href=\"/docs/macos\">macOS</a> · <a href=\"/docs/windows\">Windows</a>. The terminal installer avoids the macOS prompt."
        after = "After installing, follow the <a href=\"/docs/\">getting started guide</a>. Every version and its files are on <a href=\"" + DESK + "/releases\">GitHub Releases</a>."
        title = "Download Kothalipi for Mac, Windows & Linux (Free)"
        desc = "Download Kothalipi, free Bangla and English voice typing, for macOS, Windows and Linux. Or install with one line in the terminal."
    else:
        h1, lead = "কথালিপি ডাউনলোড", f"macOS, Windows ও Linux-এর জন্য ফ্রি। ভার্সন <span data-version>v{VERSION}</span>।"
        loading, soon = "সর্বশেষ ভার্সন খোঁজা হচ্ছে…", "প্রথম রিলিজ আসছে। পেতে GitHub-এ প্রজেক্টটা ফলো করুন।"
        main_label = "ডাউনলোড"
        os_h = [("macOS", "macOS 10.15 বা নতুন।"), ("Windows", "Windows 10 বা 11।"), ("Linux", "X11 ও Wayland।")]
        term_h, term_p = "টার্মিনাল থেকে ইনস্টল", "এক লাইন। GitHub থেকে সর্বশেষ রিলিজ নামিয়ে ইনস্টল করে দেয়।"
        mac_l, win_l = "macOS ও Linux", "Windows (PowerShell)"
        req_h = "যা লাগবে"
        req = [("macOS", "10.15 বা নতুন, Apple Silicon বা Intel। বাংলা মডেলের জন্য প্রায় ১ GB ফাঁকা জায়গা।"), ("Windows", "Windows 10 বা 11, ৬৪-বিট বা ARM। বাংলা মডেলের জন্য প্রায় ১ GB ফাঁকা জায়গা।"), ("Linux", "GTK 3 ও ALSA বা PipeWire সহ নতুন ৬৪-বিট ডিস্ট্রো। Wayland-এ <code>wtype</code> বা <code>ydotool</code> লাগে।"), ("মেমরি", "অফলাইন মোডের জন্য ৮ GB সুপারিশ করা হয়। ৪ GB হলে ক্লাউড মোড ব্যবহার করুন।")]
        unsigned = "<b>প্রথম দিকের রিলিজে এখনো কোড সাইনিং নেই।</b> প্রথমবার macOS ও Windows সতর্কবার্তা দেখাতে পারে। এগিয়ে যাওয়া নিরাপদ, গাইডে কীভাবে তা দেখানো আছে: <a href=\"/docs/macos\">macOS</a> · <a href=\"/docs/windows\">Windows</a>। টার্মিনাল ইনস্টলারে macOS-এর এই ধাপ আসে না।"
        after = "ইনস্টলের পর <a href=\"/docs/\">শুরু করার গাইড</a> অনুসরণ করুন। সব ভার্সন ও ফাইল <a href=\"" + DESK + "/releases\">GitHub Releases</a>-এ আছে।"
        title = "কথালিপি ডাউনলোড: ম্যাক, উইন্ডোজ ও লিনাক্সের জন্য ফ্রি"
        desc = "ফ্রি বাংলা ও ইংরেজি ভয়েস টাইপিং কথালিপি ডাউনলোড করুন, macOS, Windows ও Linux-এ। অথবা টার্মিনালে এক লাইনে ইনস্টল করুন।"
    android_html = """
    <section class="container" id="mobile" style="padding-bottom:30px">
      <div class="section-head" style="margin-bottom:24px">
        <h2>Kothalipi Mobile (Android & iOS)</h2>
        <p>AI voice dictation, Wispr Flow-style floating bubble, and live Bangla-to-English translation.</p>
        <p class="muted" style="margin-top:8px;font-size:14px"><strong data-mobile-downloads>17+</strong> mobile downloads</p>
      </div>
      <div class="os-cards" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
        <article class="os-card" id="android">
          <h3>Android <span class="tag" style="margin-left:8px;background:#8A2BE2;color:white">v0.2.0</span></h3>
          <p>Wispr Flow floating bubble + Voice keyboard + Offline mode for Bangla & English. Android 8 or later.</p>
          <ul style="display:flex;gap:8px;flex-wrap:wrap;list-style:none;padding:0;margin:6px 0">
            <li><a class="btn btn-primary btn-sm" style="display:inline-flex;width:auto;padding:10px 18px" href="https://github.com/Kothalipi/kothalipi-mobile/releases/download/v0.2.0/Kothalipi-v0.2.0.apk">Download Android APK (v0.2.0)</a></li>
            <li><a class="btn btn-secondary btn-sm" style="display:inline-flex;width:auto;padding:10px 14px" href="/docs/android">Setup Guide</a></li>
          </ul>
          <ul class="muted" style="margin-top:12px;font-size:14px;list-style:disc;padding-left:18px">
            <li><strong>Multi-AI + Offline:</strong> Free Gemini, Groq Whisper, OpenAI auto-fallback, plus 100% free Offline Mode.</li>
            <li><strong>Floating Bubble &amp; Snippets:</strong> Dictate over WhatsApp/Gmail, expand Voice Snippets &amp; AI Voice Edit.</li>
            <li><strong>Hold-to-Talk &amp; Auto-Stop:</strong> Hold to speak or auto-stop after 2 seconds of silence.</li>
          </ul>
        </article>

        <article class="os-card" id="ios">
          <h3>iPhone / iOS <span class="tag" style="margin-left:8px;background:#8A2BE2;color:white">v0.2.0</span></h3>
          <p>SwiftUI Voice Hub + Real iOS Voice Keyboard + Offline mode. iOS 16.0 or later.</p>
          <ul style="display:flex;gap:8px;flex-wrap:wrap;list-style:none;padding:0;margin:6px 0">
            <li><a class="btn btn-primary btn-sm" style="display:inline-flex;width:auto;padding:10px 18px" href="https://github.com/Kothalipi/kothalipi-mobile/releases/download/v0.2.0/Kothalipi-v0.2.0.ipa">Download iOS IPA (v0.2.0)</a></li>
            <li><a class="btn btn-secondary btn-sm" style="display:inline-flex;width:auto;padding:10px 14px" href="/docs/ios">Setup Guide</a></li>
          </ul>
          <ul class="muted" style="margin-top:12px;font-size:14px;list-style:disc;padding-left:18px">
            <li><strong>iOS Voice Keyboard:</strong> Hands-free voice typing directly in any iOS text field.</li>
            <li><strong>Multi-AI + Offline:</strong> Gemini, Groq Whisper, OpenAI + Free On-Device Speech Recognition.</li>
            <li><strong>Action Button &amp; Voice Edit:</strong> 1-press dictation, Voice Snippets, and AI Rewrite commands.</li>
          </ul>
        </article>
      </div>
    </section>""" if en else """
    <section class="container" id="mobile" style="padding-bottom:30px">
      <div class="section-head" style="margin-bottom:24px">
        <h2>কথালিপি মোবাইল (Android ও iOS)</h2>
        <p>এআই ভয়েস ডিকটেশন, Wispr Flow স্টাইল ফ্লোটিং বাবল, ভয়েস স্ন্যাপেট, ফ্রি অফলাইন মোড এবং বাংলা-টু-ইংলিশ লাইভ অনুবাদ।</p>
        <p class="muted" style="margin-top:8px;font-size:14px"><strong data-mobile-downloads>17+</strong> টি মোবাইল ডাউনলোড</p>
      </div>
      <div class="os-cards" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
        <article class="os-card" id="android">
          <h3>Android <span class="tag" style="margin-left:8px;background:#8A2BE2;color:white">v0.2.0</span></h3>
          <p>Wispr Flow ফ্লোটিং বাবল + ভয়েস কিবোর্ড + ফ্রি অফলাইন মোড। Android 8 বা নতুন।</p>
          <ul style="display:flex;gap:8px;flex-wrap:wrap;list-style:none;padding:0;margin:6px 0">
            <li><a class="btn btn-primary btn-sm" style="display:inline-flex;width:auto;padding:10px 18px" href="https://github.com/Kothalipi/kothalipi-mobile/releases/download/v0.2.0/Kothalipi-v0.2.0.apk">Android APK ডাউনলোড (v0.2.0)</a></li>
            <li><a class="btn btn-secondary btn-sm" style="display:inline-flex;width:auto;padding:10px 14px" href="/docs/android">সেটআপ গাইড</a></li>
          </ul>
          <ul class="muted" style="margin-top:12px;font-size:14px;list-style:disc;padding-left:18px">
            <li><strong>Multi-AI + অফলাইন:</strong> ফ্রি Gemini, Groq Whisper ও OpenAI অটো-ফলব্যাক + ১০০% ফ্রি অফলাইন মোড।</li>
            <li><strong>ফ্লোটিং বাবল ও স্ন্যাপেট:</strong> WhatsApp/Gmail-এ সরাসরি টাইপ, ভয়েস স্ন্যাপেট ও AI Voice Edit।</li>
            <li><strong>Hold-to-Talk ও Auto-Stop:</strong> চেপে ধরে বলা বা ২ সেকেন্ড চুপ থাকলে অটো স্টপ।</li>
          </ul>
        </article>

        <article class="os-card" id="ios">
          <h3>iPhone / iOS <span class="tag" style="margin-left:8px;background:#8A2BE2;color:white">v0.2.0</span></h3>
          <p>SwiftUI ডিকটেশন হাব + iOS ভয়েস কীবোর্ড + ফ্রি অফলাইন মোড। iOS 16.0 বা নতুন।</p>
          <ul style="display:flex;gap:8px;flex-wrap:wrap;list-style:none;padding:0;margin:6px 0">
            <li><a class="btn btn-primary btn-sm" style="display:inline-flex;width:auto;padding:10px 18px" href="https://github.com/Kothalipi/kothalipi-mobile/releases/download/v0.2.0/Kothalipi-v0.2.0.ipa">iOS IPA ডাউনলোড (v0.2.0)</a></li>
            <li><a class="btn btn-secondary btn-sm" style="display:inline-flex;width:auto;padding:10px 14px" href="/docs/ios">সেটআপ গাইড</a></li>
          </ul>
          <ul class="muted" style="margin-top:12px;font-size:14px;list-style:disc;padding-left:18px">
            <li><strong>iOS ভয়েস কীবোর্ড:</strong> আইফোনের যেকোনো ইনপুট ফিল্ডে সরাসরি ভয়েস টাইপিং।</li>
            <li><strong>Multi-AI + অফলাইন:</strong> ফ্রি Gemini, Groq Whisper, OpenAI এবং On-Device অফলাইন মোড।</li>
            <li><strong>অ্যাকশন বাটন ও Voice Edit:</strong> এক চাপে ডিক্টেশন, ভয়েস স্ন্যাপেট ও AI রিরাইট।</li>
          </ul>
        </article>
      </div>
    </section>"""
    cards = "".join(f'<article class="os-card"><h3>{n}</h3><p>{d}</p><ul data-files="{k}"></ul></article>' for (n, d), k in zip(os_h, ["mac", "windows", "linux"]))
    req_rows = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in req)
    body = f"""
    <section class="container dl-hero">
      <h1>{h1}</h1>
      <p class="lead center">{lead}</p>
      <div class="dl-main">
        <a class="btn btn-primary btn-lg" id="dl-button" data-dl data-labels='{labels}' data-soon="{esc(soon)}" href="{DESK}/releases/latest">{ICON["download"]}<span id="dl-label">{main_label}</span></a>
        <span class="dl-meta" id="dl-size">{loading}</span>
        <p class="muted center" style="margin-top:14px;font-size:14px">{ICON['check']} <strong data-desktop-downloads>265+</strong> {'desktop downloads' if en else 'টি ডেস্কটপ ডাউনলোড'}</p>
      </div>
    </section>
    <section class="container" style="padding-bottom:20px"><div class="os-cards">{cards}</div></section>
    {android_html}
    <section class="section">
      <div class="container">
        <div class="section-head"><h2>{term_h}</h2><p>{term_p}</p></div>
        <div class="doc" style="margin:0 auto">
          {code(INSTALL_SH, mac_l)}
          {code(INSTALL_PS, win_l)}
          <p class="muted">{'Read the scripts first if you like' if en else 'চাইলে আগে স্ক্রিপ্ট পড়ে নিন'}: <a href="/install.sh">install.sh</a> · <a href="/install.ps1">install.ps1</a></p>
          <div class="warn"><p>{unsigned}</p></div>
          <h2 style="font-size:26px;margin-top:40px">{req_h}</h2>
          <table class="table"><tbody>{req_rows}</tbody></table>
          <p>{after}</p>
        </div>
      </div>
    </section>"""
    schema = [
        {"@context": "https://schema.org", "@type": "WebPage", "name": title, "url": abs_url(path), "isPartOf": {"@type": "WebSite", "url": SITE + "/"}},
        app_schema(lang),
    ]
    alt = {"en": "/download", "bn": "/bn/download"}
    page(path, title, desc, body, lang=lang, current="download", alt=alt, schema=schema, priority="0.9", changefreq="weekly")
