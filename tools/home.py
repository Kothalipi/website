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
    ("Can Kothalipi translate Bangla voice to English text?", "Yes! With our AI Post-Processing feature (v0.1.6), you can speak naturally in Bangla and Kothalipi translates your speech in real time into fluent, grammatically polished English before pasting it into any app. It works seamlessly using Google Gemini (free tier) or your preferred OpenAI/Anthropic Claude key."),
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
    ("কথালিপি কি মুখে বলা বাংলা সরাসরি ইংরেজিতে অনুবাদ করতে পারে?", "হ্যাঁ! কথালিপির নতুন এআই পোস্ট-প্রসেসিং (v0.1.6) ফিচারের মাধ্যমে আপনি বাংলায় স্বাভাবিকভাবে কথা বললে কথালিপি তাৎক্ষণিকভাবে তা অত্যন্ত সাবলীল ও ব্যাকরণগতভাবে নিখুঁত ইংরেজিতে অনুবাদ করে আপনার অ্যাপে টাইপ করে দেয়। এটি Google Gemini-এর ফ্রি টায়ার বা আপনার নিজস্ব OpenAI/Claude কি দিয়ে সহজেই চলে।"),
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
    dl_trust = f"<li>{ICON['check']}<strong data-total-downloads>150+</strong> {'downloads' if en else 'ডাউনলোড'}</li>"
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
        '<a class="new-badge" href="#features"><b>v0.1.6</b> ✨ Real-time Bangla to English Voice Translation</a><br>'
        if en
        else '<a class="new-badge" href="#features"><b>v0.1.6</b> ✨ সরাসরি বাংলা থেকে ইংরেজি ভয়েস অনুবাদ</a><br>'
    )

    if en:
        bento = f"""
      <div class="bento">
        <article class="tile translation-tile s4"><span class="tag">✨ New · AI Translation</span><h3>Speak Bangla, type in fluent English</h3>
          <p>Talk naturally in everyday Bangla, and Kothalipi translates your thoughts into polished, grammatically correct English in real time using Google Gemini AI. Perfect for official emails, international client conversations, and documents.</p>
          <div class="flow" role="img" aria-label="Bangla speech translates to English"><span class="chip chip-spoken">🗣️ "আমি কালকে মিটিংয়ে জয়েন করব"</span><span class="arrow">→</span><span class="chip chip-translated">✍️ "I will join the meeting tomorrow"</span></div></article>
        <article class="tile accent s4"><span class="tag">Offline or cloud</span><h3>Free and private, or the most accurate. You choose.</h3>
          <p>Offline runs a Bangla model on your computer. Cloud uses your own Gemini or ChatGPT key. If a key runs out or you lose internet, Kothalipi moves to the next engine, so it never stops typing.</p>
          <div class="flow" role="img" aria-label="Fallback order: Gemini, then ChatGPT, then offline"><span class="chip">Gemini</span><span class="arrow">→</span><span class="chip">ChatGPT</span><span class="arrow">→</span><span class="chip">Offline</span></div></article>
        <article class="tile s2"><span class="tag">Two languages</span><h3>One key for each</h3><p>The key decides the language and the model for that recording.</p>
          <div class="keys-row"><span class="keycap">Right ⌘ <small class="muted">বাংলা</small></span><span class="keycap fn">fn <small class="muted">English</small></span></div></article>
        <article class="tile s2"><span class="tag">Smart setup</span><h3>Models for your computer</h3><p>Setup reads your memory and chip and picks the best fit.</p>
          <div class="devcard"><b>Apple M2 · 16 GB</b><span class="ok">Best for this computer</span><br>Qwen3-ASR 0.6B Bangla · Parakeet 0.6B</div></article>
        <article class="tile s2"><span class="tag">Guided</span><h3>Setup that explains itself</h3><p>Permissions, API keys with a Get a free key button, model downloads and key conflicts, in one calm flow.</p></article>
        <article class="tile s2"><span class="tag">Private</span><h3>No account, no tracking</h3><p>Offline audio never leaves your computer. Kothalipi has no servers and no analytics.</p></article>
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
        <article class="tile translation-tile s4"><span class="tag">✨ নতুন · এআই ভয়েস ট্রান্সলেশন</span><h3>বাংলায় বলুন, সাথে সাথে নিখুঁত ইংরেজিতে লেখা হবে</h3>
          <p>বাংলায় আপনার স্বাভাবিক ভাষায় কথা বলুন। কথালিপি Google Gemini এআই-এর সাহায্যে রিয়েল-টাইমে তা অত্যন্ত সাবলীল ও শুদ্ধ ইংরেজিতে রূপান্তর করে সক্রিয় অ্যাপে টাইপ করে দেয়। অফিশিয়াল ইমেইল, মেসেজ বা ক্লায়েন্ট চ্যাটের জন্য অসাধারণ সুবিধা।</p>
          <div class="flow" role="img" aria-label="বাংলা কথা সরাসরি ইংরেজিতে অনুবাদ"><span class="chip chip-spoken">🗣️ "আমি কালকে মিটিংয়ে জয়েন করব"</span><span class="arrow">→</span><span class="chip chip-translated">✍️ "I will join the meeting tomorrow"</span></div></article>
        <article class="tile accent s4"><span class="tag">অফলাইন বা ক্লাউড</span><h3>ফ্রি ও প্রাইভেট, অথবা সবচেয়ে নির্ভুল। আপনিই বেছে নিন।</h3>
          <p>অফলাইনে বাংলা মডেল আপনার কম্পিউটারেই চলে। ক্লাউডে আপনার নিজের Gemini বা ChatGPT কি ব্যবহার হয়। কোনো কি-এর সীমা শেষ হলে বা ইন্টারনেট গেলে কথালিপি পরের ইঞ্জিনে চলে যায়, তাই লেখা কখনো থামে না।</p>
          <div class="flow" role="img" aria-label="ক্রম: Gemini, তারপর ChatGPT, তারপর অফলাইন"><span class="chip">Gemini</span><span class="arrow">→</span><span class="chip">ChatGPT</span><span class="arrow">→</span><span class="chip">অফলাইন</span></div></article>
        <article class="tile s2"><span class="tag">দুই ভাষা</span><h3>প্রতি ভাষায় একটা কি</h3><p>কি-ই ঠিক করে ওই রেকর্ডিংয়ের ভাষা ও মডেল।</p>
          <div class="keys-row"><span class="keycap">Right ⌘ <small class="muted">বাংলা</small></span><span class="keycap fn">fn <small class="muted">English</small></span></div></article>
        <article class="tile s2"><span class="tag">স্মার্ট সেটআপ</span><h3>আপনার কম্পিউটারের মডেল</h3><p>সেটআপ আপনার মেমরি ও চিপ দেখে সবচেয়ে মানানসই মডেল বাছে।</p>
          <div class="devcard"><b>Apple M2 · 16 GB</b><span class="ok">এই কম্পিউটারের জন্য সেরা</span><br>Qwen3-ASR 0.6B Bangla · Parakeet 0.6B</div></article>
        <article class="tile s2"><span class="tag">গাইডেড</span><h3>নিজেই বুঝিয়ে দেওয়া সেটআপ</h3><p>অনুমতি, “ফ্রি কি নিন” বোতামসহ API কি, মডেল ডাউনলোড ও কি-এর সমস্যা, সব একটা শান্ত ধাপে।</p></article>
        <article class="tile s2"><span class="tag">প্রাইভেট</span><h3>অ্যাকাউন্ট নেই, ট্র্যাকিং নেই</h3><p>অফলাইনে অডিও কম্পিউটার ছেড়ে যায় না। কথালিপির কোনো সার্ভার বা অ্যানালিটিক্স নেই।</p></article>
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
      </div>
      <div class="os-cards" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
        <article class="os-card" id="android">
          <h3>Android <span class="tag" style="margin-left:8px;background:#8A2BE2;color:white">v0.1.0</span></h3>
          <p>Wispr Flow floating bubble + Voice keyboard for Bangla & English. Android 8 or later.</p>
          <ul style="display:flex;gap:8px;flex-wrap:wrap;list-style:none;padding:0;margin:6px 0">
            <li><a class="btn btn-primary btn-sm" style="display:inline-flex;width:auto;padding:10px 18px" href="https://github.com/Kothalipi/kothalipi-mobile/releases/download/v0.1.0/Kothalipi-v0.1.0.apk">Download Android APK (v0.1.0)</a></li>
            <li><a class="btn btn-secondary btn-sm" style="display:inline-flex;width:auto;padding:10px 14px" href="/docs/android">Setup Guide</a></li>
          </ul>
          <ul class="muted" style="margin-top:12px;font-size:14px;list-style:disc;padding-left:18px">
            <li><strong>Floating Bubble:</strong> Speak over WhatsApp, Facebook, or Notes without switching keyboards.</li>
            <li><strong>Bangla ➔ English:</strong> Speak in Bangla, automatically types fluent English.</li>
            <li><strong>AI Smart Polish:</strong> Strips stutters and fixes punctuation with Google Gemini.</li>
          </ul>
        </article>

        <article class="os-card" id="ios">
          <h3>iPhone / iOS <span class="tag" style="margin-left:8px;background:#8A2BE2;color:white">v0.1.0</span></h3>
          <p>SwiftUI Voice Hub + iOS Keyboard Extension. iOS 16.0 or later.</p>
          <ul style="display:flex;gap:8px;flex-wrap:wrap;list-style:none;padding:0;margin:6px 0">
            <li><a class="btn btn-primary btn-sm" style="display:inline-flex;width:auto;padding:10px 18px" href="https://github.com/Kothalipi/kothalipi-mobile/releases/download/v0.1.0/Kothalipi-v0.1.0.ipa">Download iOS IPA (v0.1.0)</a></li>
            <li><a class="btn btn-secondary btn-sm" style="display:inline-flex;width:auto;padding:10px 14px" href="/docs/ios">Setup Guide</a></li>
          </ul>
          <ul class="muted" style="margin-top:12px;font-size:14px;list-style:disc;padding-left:18px">
            <li><strong>iOS Voice Keyboard:</strong> Hands-free voice typing directly in any iOS text field.</li>
            <li><strong>Action Button & Siri:</strong> Trigger instant voice dictation with 1 press.</li>
            <li><strong>Haptic Waves:</strong> Real-time audio waveform and fluent translations.</li>
          </ul>
        </article>
      </div>
    </section>""" if en else """
    <section class="container" id="mobile" style="padding-bottom:30px">
      <div class="section-head" style="margin-bottom:24px">
        <h2>কথালিপি মোবাইল (Android ও iOS)</h2>
        <p>এআই ভয়েস ডিকটেশন, Wispr Flow স্টাইল ফ্লোটিং বাবল এবং সরাসরি বাংলা থেকে ইংরেজি লাইভ অনুবাদ।</p>
      </div>
      <div class="os-cards" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
        <article class="os-card" id="android">
          <h3>Android <span class="tag" style="margin-left:8px;background:#8A2BE2;color:white">v0.1.0</span></h3>
          <p>Wispr Flow ফ্লোটিং বাবল + বাংলা ও ইংরেজির ভয়েস কিবোর্ড। Android 8 বা নতুন।</p>
          <ul style="display:flex;gap:8px;flex-wrap:wrap;list-style:none;padding:0;margin:6px 0">
            <li><a class="btn btn-primary btn-sm" style="display:inline-flex;width:auto;padding:10px 18px" href="https://github.com/Kothalipi/kothalipi-mobile/releases/download/v0.1.0/Kothalipi-v0.1.0.apk">Android APK ডাউনলোড (v0.1.0)</a></li>
            <li><a class="btn btn-secondary btn-sm" style="display:inline-flex;width:auto;padding:10px 14px" href="/docs/android">সেটআপ গাইড</a></li>
          </ul>
          <ul class="muted" style="margin-top:12px;font-size:14px;list-style:disc;padding-left:18px">
            <li><strong>ফ্লোটিং বাবল:</strong> কীবোর্ড না বদলেই WhatsApp, Facebook বা Notes-এর ওপর ডিকটেশন করুন।</li>
            <li><strong>বাংলা ➔ ইংরেজি:</strong> মুখে বাংলায় বললেই সরাসরি প্রফেশনাল ইংরেজিতে টাইপ হবে।</li>
            <li><strong>স্মার্ট পলিশ:</strong> তোতলানো ফিল্টার ও বিরামচিহ্ন ঠিক করে প্রফেশনাল টেক্সট দেয়।</li>
          </ul>
        </article>

        <article class="os-card" id="ios">
          <h3>iPhone / iOS <span class="tag" style="margin-left:8px;background:#8A2BE2;color:white">v0.1.0</span></h3>
          <p>SwiftUI ডিকটেশন হাব + iOS কীবোর্ড এক্সটেনশন। iOS 16.0 বা নতুন।</p>
          <ul style="display:flex;gap:8px;flex-wrap:wrap;list-style:none;padding:0;margin:6px 0">
            <li><a class="btn btn-primary btn-sm" style="display:inline-flex;width:auto;padding:10px 18px" href="https://github.com/Kothalipi/kothalipi-mobile/releases/download/v0.1.0/Kothalipi-v0.1.0.ipa">iOS IPA ডাউনলোড (v0.1.0)</a></li>
            <li><a class="btn btn-secondary btn-sm" style="display:inline-flex;width:auto;padding:10px 14px" href="/docs/ios">সেটআপ গাইড</a></li>
          </ul>
          <ul class="muted" style="margin-top:12px;font-size:14px;list-style:disc;padding-left:18px">
            <li><strong>iOS ভয়েস কীবোর্ড:</strong> আইফোনের যেকোনো ইনপুট ফিল্ডে সরাসরি ভয়েস টাইপিং।</li>
            <li><strong>অ্যাকশন বাটন ও সিরি:</strong> এক ক্লিকেই ভয়েস টাইপিং চালু করুন।</li>
            <li><strong>হ্যাপটিক ওয়েভস:</strong> রিয়েল-টাইম অডিও সাউন্ডওয়েভ ও ফ্লুয়েন্ট অনুবাদ।</li>
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
        <p class="muted center" style="margin-top:14px;font-size:14px">{ICON['check']} <strong data-total-downloads>150+</strong> {'downloads across all platforms' if en else 'টি মোট ডাউনলোড'}</p>
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
