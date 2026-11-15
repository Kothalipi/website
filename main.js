// Kothalipi website: language toggle + hold-to-speak preview.

const BN = {
  "nav.how": "কীভাবে কাজ করে",
  "nav.modes": "মোড",
  "nav.why": "কেন কথালিপি",
  "nav.faq": "প্রশ্ন",
  "hero.status": "তৈরি হচ্ছে · ওপেন সোর্স",
  "hero.title": "বলুন।<br>লেখা হয়ে যাবে।",
  "hero.lead": "বাংলা, ইংরেজি আর বাংলিশে ভয়েস টাইপিং। একটা কি চেপে ধরে কথা বলুন, যেকোনো অ্যাপে লেখা চলে আসবে। ফ্রি, ওপেন সোর্স, আর ইন্টারনেট ছাড়াই চলে।",
  "hero.star": "★ GitHub-এ স্টার দিন",
  "hero.watch": "রিলিজ হলে জানুন",
  "demo.app": "মেসেজ",
  "demo.hold": "চেপে ধরে বলুন",
  "demo.note": "এটা শুধু প্রিভিউ অ্যানিমেশন। অ্যাপে হটকি চেপে ধরলে আপনার আসল কথা লেখা হবে।",
  "how.title": "চাপুন। বলুন। ছাড়ুন।",
  "how.s1": "হটকি চেপে ধরুন",
  "how.s1p": "বাংলার জন্য একটা কি, ইংরেজির জন্য একটা, বাংলিশের জন্য একটা। যখন খুশি বদলাতে পারবেন।",
  "how.s2": "স্বাভাবিকভাবে বলুন",
  "how.s2p": "যেভাবে কথা বলেন সেভাবেই বলুন। এক বাক্যে বাংলা-ইংরেজি মিশিয়ে বলা স্বাভাবিক, কথালিপি সেটার জন্যই বানানো।",
  "how.s3": "ছেড়ে দিন",
  "how.s3p": "কার্সর যেখানে, লেখা সেখানে: চ্যাট, ইমেইল, ডক, কোড এডিটর।",
  "modes.title": "লেখার তিন উপায়",
  "modes.say": "আপনি বললেন",
  "modes.bn": "দাঁড়ি (।) আর যতিচিহ্নসহ শুদ্ধ বাংলা লিপি।",
  "modes.en": "ইমেইল আর মেসেজের জন্য পরিষ্কার ইংরেজি।",
  "modes.bl": "বাংলায় বলুন, পাবেন রোমান হরফে লেখা, ঠিক যেভাবে চ্যাটে লেখেন।",
  "why.title": "কেন কথালিপি",
  "why.f1": "বাংলার জন্য বানানো",
  "why.f1p": "বেশিরভাগ ভয়েস টাইপিং টুল যে মডেল চালায় সেগুলো বাংলায় দুর্বল। কথালিপি বাংলা কথায় ট্রেইন করা মডেল ব্যবহার করে, আর সেগুলোর ফলাফল আমরা একটা পাবলিক বেঞ্চমার্কে যাচাই করি, যেটা যে কেউ দেখতে পারে।",
  "why.f2": "আপনার কণ্ঠ আপনার কাছেই",
  "why.f2p": "স্পিচ রিকগনিশন চলে আপনার কম্পিউটারেই। নিজের কি দিয়ে ক্লাউড ইঞ্জিন চালু না করলে আপনার কণ্ঠ কোথাও যায় না।",
  "why.f3": "পুরোপুরি ওপেন সোর্স",
  "why.f3p": "প্রতিটা লাইন কোড MIT লাইসেন্সে উন্মুক্ত। কোনো অ্যাকাউন্ট নেই, ট্রায়াল নেই, লুকানো ডেটা সংগ্রহ নেই।",
  "why.f4": "সব প্ল্যাটফর্মে",
  "why.f4p": "প্রথমে macOS, Windows আর Linux, তারপর Android আর iOS কিবোর্ড।",
  "plat.title": "আমরা কোথায় আছি",
  "plat.wip": "তৈরি হচ্ছে",
  "plat.plan": "পরিকল্পনায়",
  "plat.roadmap": "পুরো রোডম্যাপ দেখুন →",
  "help.title": "সাথে বানান",
  "help.lead": "কথালিপি বানাচ্ছে এর কমিউনিটি। কোড না জানলেও সাহায্য করতে পারেন।",
  "help.h1": "বাংলা ভয়েস স্যাম্পল দিন",
  "help.h2": "বাংলিশ বানান ঠিক করুন",
  "help.h3": "স্পিচ মডেল টেস্ট করুন",
  "help.h4": "আপনার ভাষা যোগ করুন",
  "faq.title": "প্রশ্ন",
  "faq.q1": "এটা কি ফ্রি?",
  "faq.a1": "হ্যাঁ। কথালিপি MIT লাইসেন্সে ওপেন সোর্স। অফলাইন মোড চালাতে কোনো খরচ নেই। ক্লাউড ইঞ্জিন বেছে নিলে সেই প্রোভাইডারের সাথে নিজের API কি ব্যবহার করবেন।",
  "faq.q2": "কবে ডাউনলোড করা যাবে?",
  "faq.a2": "প্রথম ডেস্কটপ ভার্সন এখন বানানো হচ্ছে। প্রথম রিলিজের খবর পেতে GitHub রিপো Watch করুন।",
  "faq.q3": "আমার রেকর্ডিং কোথায় যায়?",
  "faq.a3": "কোথাও না। অফলাইন মোডে অডিও আপনার ডিভাইসেই প্রসেস হয়ে মুছে যায়। ক্লাউড মোড ঐচ্ছিক, আর শুরুতে সবসময় বন্ধ থাকে।",
  "faq.q4": "বাংলা-ইংরেজি মেশানো কথা বুঝবে?",
  "faq.a4": "এটাই আমাদের মূল লক্ষ্যগুলোর একটা। প্রথম দিন থেকেই মেশানো কথা আমাদের টেস্ট সেটে আছে, আর প্রতিটা মডেল কেমন করে তা আমরা প্রকাশ করি।",
  "faq.q5": "অন্য ভাষা আসবে?",
  "faq.a5": "হ্যাঁ। বাংলা প্রথম, আর প্রজেক্টটা এমনভাবে বানানো যাতে যেকোনো কমিউনিটি নিজের ভাষা যোগ করতে পারে, Hinglish বা Arabizi-র মতো রোমান রূপসহ।",
  "foot.made": "ওপেন সোর্স, বাংলাদেশে বানানো 🇧🇩 সবার জন্য।",
  "foot.talk": "আলোচনা",
};

const SAMPLES = {
  bn: "আজকে বিকেলে কি দেখা হবে?",
  en: "Can we meet this afternoon?",
  bl: "ajke bikele ki dekha hobe?",
};

const en = {};
const nodes = document.querySelectorAll("[data-i18n]");
nodes.forEach((el) => (en[el.dataset.i18n] = el.innerHTML));

function setLang(lang) {
  const dict = lang === "bn" ? BN : en;
  nodes.forEach((el) => {
    const v = dict[el.dataset.i18n];
    if (v !== undefined) el.innerHTML = v;
  });
  document.documentElement.lang = lang;
  document.body.classList.toggle("bn", lang === "bn");
  document.getElementById("lang").textContent = lang === "bn" ? "English" : "বাংলা";
  try { localStorage.setItem("lang", lang); } catch (_) { /* storage blocked */ }
}

let lang = "en";
try { lang = localStorage.getItem("lang") || ""; } catch (_) { lang = ""; }
if (!lang) lang = (navigator.language || "").toLowerCase().startsWith("bn") ? "bn" : "en";
setLang(lang);
document.getElementById("lang").addEventListener("click", () => {
  lang = lang === "bn" ? "en" : "bn";
  setLang(lang);
});

// Hold-to-speak preview
const typed = document.getElementById("typed");
const hold = document.getElementById("hold");
const tabs = document.querySelectorAll(".demo-tabs button");
let mode = "bn";
let timer = null;

function render(text) {
  typed.textContent = text;
  const c = document.createElement("span");
  c.className = "cursor";
  typed.appendChild(c);
}

function type() {
  const chars = Array.from(SAMPLES[mode]);
  let i = 0;
  clearInterval(timer);
  render("");
  timer = setInterval(() => {
    i += 1;
    render(chars.slice(0, i).join(""));
    if (i >= chars.length) clearInterval(timer);
  }, mode === "bn" ? 55 : 40);
}

function start(e) {
  e.preventDefault();
  hold.classList.add("active");
  render("");
}
function stop() {
  if (!hold.classList.contains("active")) return;
  hold.classList.remove("active");
  type();
}

hold.addEventListener("pointerdown", start);
window.addEventListener("pointerup", stop);
hold.addEventListener("pointercancel", stop);
hold.addEventListener("keydown", (e) => { if ((e.key === " " || e.key === "Enter") && !e.repeat) start(e); });
hold.addEventListener("keyup", (e) => { if (e.key === " " || e.key === "Enter") stop(); });

tabs.forEach((t) =>
  t.addEventListener("click", () => {
    tabs.forEach((x) => x.classList.toggle("on", x === t));
    mode = t.dataset.mode;
    type();
  })
);

type();
