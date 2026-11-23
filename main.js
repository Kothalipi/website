// Kothalipi website: small progressive enhancements. Every page works without this file.
(() => {
  const REPO = "Kothalipi/kothalipi-desktop";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  document.documentElement.classList.add("js");

  function detectOs() {
    const p = ((navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || navigator.userAgent || "").toLowerCase();
    if (p.includes("mac")) return "mac";
    if (p.includes("win")) return "windows";
    if (p.includes("linux") || p.includes("x11")) return "linux";
    return null;
  }

  /* header: shadow on scroll, mobile menu */
  const nav = $(".nav");
  const onScroll = () => nav && nav.classList.toggle("scrolled", window.scrollY > 4);
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  const menu = $(".menu-btn");
  if (menu && nav) {
    menu.addEventListener("click", () => {
      const open = nav.classList.toggle("nav-open");
      menu.setAttribute("aria-expanded", String(open));
    });
  }

  /* theme toggle (light / dark) */
  const getTheme = () => {
    return document.documentElement.getAttribute("data-theme") || 
      (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  };
  const setTheme = (theme) => {
    document.documentElement.setAttribute("data-theme", theme);
    try { localStorage.setItem("kothalipi_theme", theme); } catch (_) {}
  };
  $$(".theme-toggle").forEach((btn) => {
    btn.addEventListener("click", () => {
      const current = getTheme();
      const next = current === "dark" ? "light" : "dark";
      setTheme(next);
    });
  });
  if (window.matchMedia) {
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", (e) => {
      try {
        if (!localStorage.getItem("kothalipi_theme")) {
          document.documentElement.setAttribute("data-theme", e.matches ? "dark" : "light");
        }
      } catch (_) {}
    });
  }

  /* copy buttons on code blocks */
  $$(".code").forEach((block) => {
    const b = document.createElement("button");
    b.className = "copy";
    b.type = "button";
    b.textContent = "Copy";
    b.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText($("pre", block).innerText.trim());
        b.textContent = "Copied";
      } catch (_) {
        b.textContent = "Select & copy";
      }
      setTimeout(() => (b.textContent = "Copy"), 1600);
    });
    block.appendChild(b);
  });

  /* tabs (install commands) */
  $$(".tabs").forEach((tabs) => {
    const buttons = $$('[role="tab"]', tabs);
    const panels = $$('[role="tabpanel"]', tabs);
    const select = (id) => {
      buttons.forEach((b) => b.setAttribute("aria-selected", String(b.dataset.tab === id)));
      panels.forEach((p) => (p.hidden = p.dataset.panel !== id));
    };
    buttons.forEach((b) => b.addEventListener("click", () => select(b.dataset.tab)));
    const os = detectOs();
    select(os === "windows" ? "windows" : os === "linux" ? "linux" : os === "mac" ? "mac" : buttons[0].dataset.tab);
  });

  /* home: hold-to-speak demo */
  const typed = $("#typed");
  const hold = $("#hold");
  if (typed && hold) {
    const SAMPLES = {
      bn: "আজকে বিকেলে কি দেখা হবে? আমি পাঁচটার পর ফ্রি আছি।",
      en: "Can we meet this afternoon? I'm free after five.",
    };
    const KEYS = { bn: "Right ⌘", en: "fn" };
    const tabs = $$(".demo-tabs button");
    const key = $("#hold-key");
    const pill = $("#pill");
    const pillLang = $("#pill-lang");
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
      }, mode === "bn" ? 48 : 34);
    };
    const start = (e) => {
      e.preventDefault();
      hold.classList.add("active");
      if (pill) pill.classList.add("on");
      clearInterval(timer);
      render("");
    };
    const stop = () => {
      if (!hold.classList.contains("active")) return;
      hold.classList.remove("active");
      if (pill) pill.classList.remove("on");
      type();
    };
    hold.addEventListener("pointerdown", start);
    window.addEventListener("pointerup", stop);
    hold.addEventListener("pointercancel", stop);
    hold.addEventListener("keydown", (e) => { if ((e.key === " " || e.key === "Enter") && !e.repeat) start(e); });
    hold.addEventListener("keyup", (e) => { if (e.key === " " || e.key === "Enter") stop(); });
    tabs.forEach((t) => t.addEventListener("click", () => {
      tabs.forEach((x) => { x.classList.toggle("on", x === t); x.setAttribute("aria-selected", String(x === t)); });
      mode = t.dataset.mode;
      if (key) key.textContent = KEYS[mode];
      if (pillLang) pillLang.textContent = mode === "bn" ? "BN" : "EN";
      type();
    }));
    type();
  }

  /* ---------- releases: direct downloads from our own site ---------- */
  const BN = document.documentElement.lang === "bn";
  const T = BN
    ? { started: "ডাউনলোড শুরু হয়েছে", started2: "ফাইলটি খুলে ইনস্টল করুন।", soon: "প্রথম রিলিজ আসছে", next: "এরপর", steps: ["ডাউনলোড হওয়া ফাইলটি খুলুন", "মাইক্রোফোনের অনুমতি দিন (Mac-এ Accessibility-ও)", "অফলাইন বা ক্লাউড বাছুন, তারপর কি চেপে বলুন"], guide: "ধাপে ধাপে গাইড →", missing: "এই কম্পিউটারের জন্য সরাসরি ফাইল পাওয়া যায়নি।", all: "সব ডাউনলোড" }
    : { started: "Download started", started2: "Open the file to install.", soon: "The first release is on its way", next: "Next", steps: ["Open the downloaded file", "Allow the microphone (and Accessibility on Mac)", "Pick Offline or Cloud, then hold a key and speak"], guide: "Step-by-step guide →", missing: "No direct file for this computer yet.", all: "All downloads" };
  const API = `https://api.github.com/repos/${REPO}/releases/latest`;
  const mb = (n) => `${Math.round(n / 1048576)} MB`;
  const isArm = async () => {
    try { const v = await navigator.userAgentData.getHighEntropyValues(["architecture"]); return v.architecture === "arm"; }
    catch (_) { return true; }
  };
  let relP = null;
  const getRelease = () => {
    if (relP) return relP;
    relP = (async () => {
      try {
        const c = JSON.parse(sessionStorage.getItem("kl-rel") || "null");
        if (c && Date.now() - c.t < 600000) return c.r;
      } catch (_) {}
      let r = await fetch("/latest.json", { cache: "no-cache" }).catch(() => null);
      if (!r || !r.ok) r = await fetch(API);
      if (!r.ok) throw new Error(String(r.status));
      const j = await r.json();
      const slim = {
        tag: j.tag_name || (j.version ? `v${j.version}` : "v0.1.8"),
        totalDownloads: j.total_downloads,
        desktopDownloads: j.desktop_downloads,
        mobileDownloads: j.mobile_downloads,
        androidDownloads: j.android_downloads,
        iosDownloads: j.ios_downloads,
        releaseDownloads: j.release_downloads,
        assets: (j.assets || []).map((a) => ({ name: a.name, size: a.size, url: a.browser_download_url, downloads: a.download_count }))
      };
      try { sessionStorage.setItem("kl-rel", JSON.stringify({ t: Date.now(), r: slim })); } catch (_) {}
      return slim;
    })();
    return relP;
  };

  /* ---------- live download counters: Total, Desktop, Mobile, Android, and iOS ---------- */
  const totalEls = $$("[data-total-downloads]");
  const desktopEls = $$("[data-desktop-downloads]");
  const mobileEls = $$("[data-mobile-downloads]");
  const androidEls = $$("[data-android-downloads]");
  const iosEls = $$("[data-ios-downloads]");
  if (totalEls.length || desktopEls.length || mobileEls.length || androidEls.length || iosEls.length) {
    const renderCounts = ({ total, desktop, mobile, android, ios }) => {
      if (total > 0) totalEls.forEach((el) => (el.textContent = `${total.toLocaleString()}+`));
      if (desktop > 0) desktopEls.forEach((el) => (el.textContent = `${desktop.toLocaleString()}+`));
      if (mobile > 0) mobileEls.forEach((el) => (el.textContent = `${mobile.toLocaleString()}+`));
      if (android >= 0 && android !== undefined) androidEls.forEach((el) => (el.textContent = `${android.toLocaleString()}`));
      if (ios >= 0 && ios !== undefined) iosEls.forEach((el) => (el.textContent = `${ios.toLocaleString()}`));
    };
    const sumInstallers = (rels) => {
      if (!Array.isArray(rels)) return 0;
      let n = 0;
      for (const rel of rels) {
        for (const a of rel.assets || []) {
          if (a.name && !/\.(sig|json)$/i.test(a.name)) n += Number(a.download_count || 0);
        }
      }
      return n;
    };
    const sumByExt = (rels, ext) => {
      if (!Array.isArray(rels)) return 0;
      let n = 0;
      for (const rel of rels) {
        for (const a of rel.assets || []) {
          if (a.name && a.name.toLowerCase().endsWith(ext)) n += Number(a.download_count || 0);
        }
      }
      return n;
    };
    (async () => {
      try {
        const cached = JSON.parse(sessionStorage.getItem("kl-dl-counts-v2") || "null");
        if (cached && Date.now() - cached.t < 300000 && cached.total > 0) {
          renderCounts(cached);
          return;
        }
      } catch (_) {}
      // 1. Show fast fallback from /latest.json first
      getRelease().then((rel) => {
        renderCounts({
          total: rel.totalDownloads || 0,
          desktop: rel.desktopDownloads || 0,
          mobile: rel.mobileDownloads || 0,
          android: rel.androidDownloads,
          ios: rel.iosDownloads,
        });
      }).catch(() => {});
      // 2. Fetch live counts from GitHub API (Desktop + Mobile)
      try {
        const [deskRels, mobRels] = await Promise.all([
          fetch("https://api.github.com/repos/Kothalipi/kothalipi-desktop/releases?per_page=100").then((r) => (r.ok ? r.json() : [])).catch(() => []),
          fetch("https://api.github.com/repos/Kothalipi/kothalipi-mobile/releases?per_page=100").then((r) => (r.ok ? r.json() : [])).catch(() => []),
        ]);
        const desktop = sumInstallers(deskRels);
        const android = sumByExt(mobRels, ".apk");
        const ios = sumByExt(mobRels, ".ipa");
        const mobile = android + ios;
        const total = desktop + mobile;
        if (total > 0) {
          const counts = { t: Date.now(), total, desktop, mobile, android, ios };
          renderCounts(counts);
          try { sessionStorage.setItem("kl-dl-counts-v2", JSON.stringify(counts)); } catch (_) {}
        }
      } catch (_) {}
    })();
  }
  const pick = async (rel, os) => {
    const find = (re) => rel.assets.find((a) => re.test(a.name));
    if (os === "mac") return find((await isArm()) ? /_aarch64\.dmg$/ : /_x64\.dmg$/);
    if (os === "windows") return find(/_x64-setup\.exe$/);
    if (os === "linux") return find(/_amd64\.AppImage$/) || find(/_amd64\.deb$/);
    return null;
  };
  const OS_NAME = { mac: "macOS", windows: "Windows", linux: "Linux" };

  const toast = (title, sub) => {
    let t = $(".dl-toast");
    if (!t) {
      t = document.createElement("div");
      t.className = "dl-toast";
      t.setAttribute("role", "status");
      document.body.appendChild(t);
    }
    t.innerHTML = `<div class="tick"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></div><div><b></b><span></span></div>`;
    $("b", t).textContent = title;
    $("span", t).textContent = sub;
    setTimeout(() => t.classList.add("show"), 30);
    clearTimeout(t._h);
    t._h = setTimeout(() => t.classList.remove("show"), 5200);
  };

  /* every [data-dl] button becomes a direct download for this visitor's OS */
  const dlButtons = $$("[data-dl]");
  const os = detectOs();
  if (dlButtons.length && os) {
    getRelease().then(async (rel) => {
      $$("[data-version]").forEach((el) => (el.textContent = rel.tag));
      const asset = await pick(rel, os);
      if (!asset) return;
      const dlLabel = $("#dl-label"), dlb = $("#dl-button");
      if (dlLabel && dlb) { const L = JSON.parse(dlb.dataset.labels || "{}"); if (L[os]) dlLabel.textContent = L[os]; }
      dlButtons.forEach((b) => {
        b.href = asset.url;
        b.dataset.direct = "1";
        b.setAttribute("download", "");
        const meta = $(".dl-meta", b.parentElement) || (b.id === "dl-button" ? $("#dl-size") : null);
        if (meta) meta.textContent = `${rel.tag} · ${OS_NAME[os]} · ${mb(asset.size)}`;
        b.addEventListener("click", () => {
          toast(T.started, T.started2);
          const after = $("#after-dl");
          if (after) after.classList.add("show");
        });
      });
    }).catch(() => {});
  }
  const afterBox = $("#after-dl");
  if (afterBox) {
    const g = os ? `/docs/${os === "mac" ? "macos" : os}` : "/docs/";
    afterBox.innerHTML = `<b>${T.next}</b><ol>${T.steps.map((s) => `<li>${s}</li>`).join("")}</ol><p style="margin:10px 0 0"><a href="${g}">${T.guide}</a></p>`;
  }

  /* hero button label by OS */
  const heroBtn = $("#hero-download");
  if (heroBtn) {
    const labels = JSON.parse(heroBtn.dataset.labels || "{}");
    if (os && labels[os]) $("#hero-download-label").textContent = labels[os];
  }

  /* /get/<os>: shareable shortcut that starts the download */
  const getPage = $("[data-get]");
  if (getPage) {
    const want = getPage.dataset.get;
    const msg = $("#get-msg");
    getRelease().then(async (rel) => {
      const asset = await pick(rel, want);
      if (!asset) throw new Error("none");
      $(".spinner", getPage).hidden = true;
      msg.textContent = `${T.started} · ${rel.tag} · ${mb(asset.size)}`;
      $("#get-sub").textContent = T.started2;
      const link = $("#get-link");
      link.href = asset.url;
      link.hidden = false;
      setTimeout(() => { location.href = asset.url; }, 600);
    }).catch(() => {
      $(".spinner", getPage).hidden = true;
      msg.textContent = T.soon;
      $("#get-sub").innerHTML = `<a href="/download">${T.all}</a>`;
    });
  }

  /* download page: per-file lists */
  const FILES = [
    { os: "mac", label: "Apple Silicon (M1 or newer)", match: /_aarch64\.dmg$/ },
    { os: "mac", label: "Intel Mac", match: /_x64\.dmg$/ },
    { os: "windows", label: "Windows 10/11, 64-bit", match: /_x64-setup\.exe$/ },
    { os: "windows", label: "Windows on ARM", match: /_arm64-setup\.exe$/ },
    { os: "linux", label: "Debian / Ubuntu (.deb)", match: /_amd64\.deb$/ },
    { os: "linux", label: "Fedora / openSUSE (.rpm)", match: /\.x86_64\.rpm$/ },
    { os: "linux", label: "AppImage (any distro)", match: /_amd64\.AppImage$/ },
    { os: "linux", label: "ARM64 .deb", match: /_arm64\.deb$/ },
  ];
  if ($("[data-files]")) {
    getRelease().then((rel) => {
      FILES.forEach((f) => {
        const a = rel.assets.find((x) => f.match.test(x.name));
        const list = $(`[data-files="${f.os}"]`);
        if (!a || !list) return;
        list.insertAdjacentHTML("beforeend", `<li><a href="${a.url}">${f.label}<span>${mb(a.size)}</span></a></li>`);
      });
      const size = $("#dl-size");
      if (size && !os) size.textContent = rel.tag;
    }).catch(() => {
      const size = $("#dl-size");
      if (size) size.textContent = (dlButtons[0] && dlButtons[0].dataset.soon) || T.soon;
      $$("[data-files]").forEach((l) => { l.innerHTML = `<li><a href="https://github.com/${REPO}/releases">${T.all}<span>→</span></a></li>`; });
    });
  }

  /* keyboard shortcuts: D download, C copy the install command */
  document.addEventListener("keydown", (e) => {
    if (e.metaKey || e.ctrlKey || e.altKey || e.repeat) return;
    const tg = e.target;
    if (tg && (/^(input|textarea|select)$/i.test(tg.tagName) || tg.isContentEditable || tg.id === "hold")) return;
    if (e.key === "d" || e.key === "D") {
      const b = $("[data-dl]");
      if (b) b.click(); else location.href = BN ? "/bn/download" : "/download";
    } else if (e.key === "c" || e.key === "C") {
      const panel = $('[role="tabpanel"]:not([hidden]) .copy') || $(".code .copy");
      if (panel) { panel.click(); panel.scrollIntoView({ block: "center", behavior: "smooth" }); }
    }
  });

  /* ---------- motion ---------- */
  const calm = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const bar = document.createElement("div");
  bar.className = "progress";
  document.body.appendChild(bar);
  const prog = () => {
    const h = document.documentElement.scrollHeight - innerHeight;
    bar.style.transform = `scaleX(${h > 0 ? Math.min(1, scrollY / h) : 0})`;
  };
  addEventListener("scroll", prog, { passive: true });
  prog();

  if (!calm && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    const groups = [".section-head", ".steps > *", ".bento > *", ".shot", ".platforms > *", ".faq details", ".band", ".os-cards > *", ".doc > h2", ".models-grid > *", ".cards > *"];
    groups.forEach((sel) => {
      $$(sel).forEach((el, i) => {
        el.classList.add("reveal");
        el.style.setProperty("--d", `${(i % 4) * 90}ms`);
        io.observe(el);
      });
    });
  }

  /* gentle 3D tilt on the hero demo */
  const win = $(".stage .demo-win");
  if (win && !calm && matchMedia("(hover: hover)").matches) {
    const stage = $(".stage");
    stage.addEventListener("pointermove", (e) => {
      const r = stage.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - 0.5;
      const y = (e.clientY - r.top) / r.height - 0.5;
      win.style.setProperty("--ry", `${(x * 7).toFixed(2)}deg`);
      win.style.setProperty("--rx", `${(-y * 6).toFixed(2)}deg`);
    });
    stage.addEventListener("pointerleave", () => { win.style.setProperty("--ry", "0deg"); win.style.setProperty("--rx", "0deg"); });
  }
})();
