// Kothalipi website: shared behaviour for every page.
const REPO = "Kothalipi/kothalipi-desktop";
const RELEASES = `https://github.com/${REPO}/releases`;

/* ---------- header shadow on scroll ---------- */
const nav = document.querySelector(".nav");
const onScroll = () => nav?.classList.toggle("scrolled", window.scrollY > 4);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

/* ---------- copy buttons on code blocks ---------- */
document.querySelectorAll(".code").forEach((block) => {
  const button = document.createElement("button");
  button.className = "copy";
  button.type = "button";
  button.textContent = "Copy";
  button.addEventListener("click", async () => {
    const text = block.querySelector("pre").innerText.trim();
    try {
      await navigator.clipboard.writeText(text);
      button.textContent = "Copied";
    } catch (_) {
      button.textContent = "Select & copy";
    }
    setTimeout(() => (button.textContent = "Copy"), 1600);
  });
  block.appendChild(button);
});

/* ---------- which OS is this? ---------- */
const detectOs = () => {
  const p = (navigator.userAgentData?.platform || navigator.platform || navigator.userAgent).toLowerCase();
  if (p.includes("mac")) return "mac";
  if (p.includes("win")) return "windows";
  if (p.includes("linux") || p.includes("x11")) return "linux";
  return null;
};

/* ---------- home: language toggle (English / বাংলা) ---------- */
const BN = {
  "nav.download": "ডাউনলোড",
  "nav.docs": "গাইড",
  "hero.status": "ফ্রি · ওপেন সোর্স · অফলাইন",
  "hero.title": "বলুন।<br>লেখা হয়ে যাবে।",
  "hero.lead": "বাংলা আর ইংরেজিতে ভয়েস টাইপিং, যেকোনো অ্যাপে। একটা কি চেপে ধরে কথা বলুন, ছেড়ে দিন, লেখা চলে আসবে। ইন্টারনেট ছাড়াই চলে, চাইলে ক্লাউডও।",
  "hero.download": "ফ্রি ডাউনলোড",
  "hero.github": "GitHub-এ দেখুন",
  "demo.app": "মেসেজ",
  "demo.hold": "চেপে ধরে বলুন",
  "demo.note": "এটা শুধু প্রিভিউ। অ্যাপে কি চেপে ধরলে আপনার আসল কথা লেখা হবে।",
  "keys.title": "প্রতিটা ভাষার জন্য একটা কি",
  "keys.sub": "কি চেপে ধরুন, বলুন, ছেড়ে দিন। বাংলা-ইংরেজি মিশিয়ে বলাও চলবে।",
  "keys.bn": "বাংলা লিপিতে শুদ্ধ বাংলা, দাঁড়ি আর যতিচিহ্নসহ।",
  "keys.en": "ইমেইল আর মেসেজের জন্য পরিষ্কার ইংরেজি।",
  "keys.change": "Windows-এ Right Alt আর Right Ctrl। যেকোনো কি বদলাতে পারবেন।",
  "listen.title": "ফ্রি অফলাইন, নাকি ক্লাউড",
  "listen.sub": "যখন খুশি বদলাতে পারবেন।",
  "listen.offTitle": "অফলাইন · ফ্রি",
  "listen.off": "ইন্টারনেট লাগে না। আপনার কণ্ঠ কম্পিউটার থেকে বের হয় না। বাংলা মডেল একবার ডাউনলোড করতে হয়।",
  "listen.cloudTitle": "ক্লাউড · সবচেয়ে নির্ভুল",
  "listen.cloud": "নিজের ফ্রি Google Gemini কি, অথবা ChatGPT। বাংলা-ইংরেজি মেশানো কথায় সবচেয়ে ভালো।",
  "fallback.title": "কখনো থেমে যায় না",
  "fallback.sub": "একটা কি-এর লিমিট শেষ হলে পরেরটায় যায়, ইন্টারনেট না থাকলে অফলাইনে।",
  "why.title": "কেন কথালিপি",
  "why.f1": "বাংলার জন্য বানানো",
  "why.f1p": "বাংলা কথায় ট্রেইন করা মডেল, স্বাভাবিক ভয়েস টাইপিং টুলের চেয়ে অনেক কম ভুল।",
  "why.f2": "প্রাইভেট",
  "why.f2p": "অফলাইন মোডে সব কাজ আপনার কম্পিউটারেই। কোনো অ্যাকাউন্ট নেই।",
  "why.f3": "হালকা আর দ্রুত",
  "why.f3p": "Rust দিয়ে বানানো। অল্প RAM, ব্যাকগ্রাউন্ডে চুপচাপ থাকে।",
  "why.f4": "পুরোপুরি ওপেন সোর্স",
  "why.f4p": "MIT লাইসেন্স। সব কোড GitHub-এ।",
  "plat.title": "সব কম্পিউটারে",
  "band.title": "আজই বলে লেখা শুরু করুন",
  "band.sub": "দুই মিনিটে সেটআপ। পুরোপুরি ফ্রি।",
  "band.download": "ডাউনলোড",
  "band.guide": "সেটআপ গাইড",
  "faq.title": "প্রশ্ন",
  "faq.q1": "এটা কি সত্যিই ফ্রি?",
  "faq.a1": "হ্যাঁ। কোনো অ্যাকাউন্ট, ট্রায়াল বা কার্ড লাগে না। অফলাইন মোড চালাতে কোনো খরচ নেই। ক্লাউড মোডে আপনার নিজের কি ব্যবহার হয়; Google Gemini-র ফ্রি লিমিট আছে।",
  "faq.q2": "আমার রেকর্ডিং কোথায় যায়?",
  "faq.a2": "অফলাইন মোডে কোথাও না। ক্লাউড মোডে শুধু আপনার বেছে নেওয়া প্রোভাইডারের (Google বা OpenAI) কাছে যায়, আমাদের কাছে কখনো না।",
  "faq.q3": "কোন কম্পিউটারে চলে?",
  "faq.a3": "macOS (Apple Silicon ও Intel), Windows 10/11 আর Linux। Android ও iOS আসছে।",
  "faq.q4": "সব অ্যাপে কাজ করে?",
  "faq.a4": "যেখানে টাইপ করা যায় সেখানেই: চ্যাট, ইমেইল, ব্রাউজার, ডক, কোড এডিটর।",
  "faq.q5": "কি বদলানো যায়?",
  "faq.a5": "হ্যাঁ, অ্যাপের Settings → General থেকে।",
  "foot.made": "ওপেন সোর্স, বাংলাদেশে বানানো 🇧🇩",
};

const nodes = document.querySelectorAll("[data-i18n]");
const langButton = document.getElementById("lang");
if (nodes.length && langButton) {
  const en = {};
  nodes.forEach((el) => (en[el.dataset.i18n] = el.innerHTML));
  const setLang = (lang) => {
    const dict = lang === "bn" ? BN : en;
    nodes.forEach((el) => {
      const v = dict[el.dataset.i18n];
      if (v !== undefined) el.innerHTML = v;
    });
    document.documentElement.lang = lang;
    document.body.classList.toggle("bn", lang === "bn");
    langButton.textContent = lang === "bn" ? "English" : "বাংলা";
    try { localStorage.setItem("lang", lang); } catch (_) { /* blocked */ }
  };
  let lang = "";
  try { lang = localStorage.getItem("lang") || ""; } catch (_) { lang = ""; }
  if (!lang) lang = (navigator.language || "").toLowerCase().startsWith("bn") ? "bn" : "en";
  setLang(lang);
  langButton.addEventListener("click", () => {
    lang = lang === "bn" ? "en" : "bn";
    setLang(lang);
  });
}

/* ---------- home: hold-to-speak preview ---------- */
const typed = document.getElementById("typed");
const hold = document.getElementById("hold");
if (typed && hold) {
  const SAMPLES = {
    bn: "আজকে বিকেলে কি দেখা হবে? আমি পাঁচটার পর ফ্রি আছি।",
    en: "Can we meet this afternoon? I'm free after five.",
  };
  const KEYS = { bn: "Right ⌘", en: "fn" };
  const tabs = document.querySelectorAll(".demo-tabs button");
  const keyLabel = document.getElementById("hold-key");
  let mode = "bn";
  let timer = null;
  const render = (text) => {
    typed.textContent = text;
    const c = document.createElement("span");
    c.className = "cursor";
    typed.appendChild(c);
  };
  const type = () => {
    const chars = Array.from(SAMPLES[mode]);
    let i = 0;
    clearInterval(timer);
    render("");
    timer = setInterval(() => {
      i += 1;
      render(chars.slice(0, i).join(""));
      if (i >= chars.length) clearInterval(timer);
    }, mode === "bn" ? 50 : 35);
  };
  const start = (e) => { e.preventDefault(); hold.classList.add("active"); clearInterval(timer); render(""); };
  const stop = () => { if (!hold.classList.contains("active")) return; hold.classList.remove("active"); type(); };
  hold.addEventListener("pointerdown", start);
  window.addEventListener("pointerup", stop);
  hold.addEventListener("pointercancel", stop);
  hold.addEventListener("keydown", (e) => { if ((e.key === " " || e.key === "Enter") && !e.repeat) start(e); });
  hold.addEventListener("keyup", (e) => { if (e.key === " " || e.key === "Enter") stop(); });
  tabs.forEach((t) => t.addEventListener("click", () => {
    tabs.forEach((x) => x.classList.toggle("on", x === t));
    mode = t.dataset.mode;
    if (keyLabel) keyLabel.textContent = KEYS[mode];
    type();
  }));
  type();
}

/* ---------- download page: real file links from the latest release ---------- */
const FILES = [
  { os: "mac", label: "Apple Silicon (M1 or newer)", match: /_aarch64\.dmg$/ },
  { os: "mac", label: "Intel Mac", match: /_x64\.dmg$/ },
  { os: "windows", label: "Windows 10/11 · 64-bit", match: /_x64-setup\.exe$/ },
  { os: "windows", label: "Windows on ARM", match: /_arm64-setup\.exe$/ },
  { os: "linux", label: "Debian / Ubuntu (.deb)", match: /_amd64\.deb$/ },
  { os: "linux", label: "Fedora / openSUSE (.rpm)", match: /\.x86_64\.rpm$/ },
  { os: "linux", label: "AppImage (any distro)", match: /_amd64\.AppImage$/ },
  { os: "linux", label: "ARM64 .deb", match: /_arm64\.deb$/ },
];
const mb = (bytes) => `${Math.round(bytes / 1048576)} MB`;

const dlMain = document.getElementById("dl-main");
if (dlMain) {
  const os = detectOs();
  const isArmMac = async () => {
    try {
      const v = await navigator.userAgentData?.getHighEntropyValues(["architecture"]);
      return v ? v.architecture === "arm" : true;
    } catch (_) { return true; }
  };
  fetch(`https://api.github.com/repos/${REPO}/releases/latest`)
    .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
    .then(async (release) => {
      const assets = release.assets || [];
      const find = (re) => assets.find((a) => re.test(a.name));
      document.querySelectorAll("[data-version]").forEach((el) => (el.textContent = release.tag_name));
      for (const f of FILES) {
        const a = find(f.match);
        const list = document.querySelector(`[data-files="${f.os}"]`);
        if (!a || !list) continue;
        const li = document.createElement("li");
        li.innerHTML = `<a href="${a.browser_download_url}">${f.label}<span>${mb(a.size)}</span></a>`;
        list.appendChild(li);
      }
      let primary = null;
      if (os === "mac") primary = find((await isArmMac()) ? /_aarch64\.dmg$/ : /_x64\.dmg$/);
      if (os === "windows") primary = find(/_x64-setup\.exe$/);
      if (os === "linux") primary = find(/_amd64\.AppImage$/) || find(/_amd64\.deb$/);
      const button = document.getElementById("dl-button");
      if (primary && button) {
        button.href = primary.browser_download_url;
        document.getElementById("dl-label").textContent =
          { mac: "Download for Mac", windows: "Download for Windows", linux: "Download for Linux" }[os];
        document.getElementById("dl-size").textContent = `${release.tag_name} · ${mb(primary.size)}`;
      }
    })
    .catch(() => {
      document.querySelectorAll("[data-files]").forEach((list) => {
        list.innerHTML = `<li><a href="${RELEASES}">All downloads on GitHub<span>→</span></a></li>`;
      });
      const size = document.getElementById("dl-size");
      if (size) size.textContent = "The first release is on its way. Watch GitHub to get it.";
    });
  if (os) document.querySelectorAll(`[data-os-show]`).forEach((el) => {
    el.hidden = el.dataset.osShow !== os;
  });
}
