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

  /* home: OS-aware hero button label */
  const heroBtn = $("#hero-download");
  if (heroBtn) {
    const os = detectOs();
    const labels = JSON.parse(heroBtn.dataset.labels || "{}");
    if (os && labels[os]) $("#hero-download-label").textContent = labels[os];
  }

  /* download: real file links from the latest release */
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
  const mb = (n) => `${Math.round(n / 1048576)} MB`;
  const dlButton = $("#dl-button");
  if (dlButton) {
    const os = detectOs();
    const labels = JSON.parse(dlButton.dataset.labels || "{}");
    const isArm = async () => {
      try {
        const v = await navigator.userAgentData.getHighEntropyValues(["architecture"]);
        return v.architecture === "arm";
      } catch (_) { return true; }
    };
    fetch(`https://api.github.com/repos/${REPO}/releases/latest`)
      .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
      .then(async (release) => {
        const assets = release.assets || [];
        const find = (re) => assets.find((a) => re.test(a.name));
        $$("[data-version]").forEach((el) => (el.textContent = release.tag_name));
        FILES.forEach((f) => {
          const a = find(f.match);
          const list = $(`[data-files="${f.os}"]`);
          if (!a || !list) return;
          const li = document.createElement("li");
          const link = document.createElement("a");
          link.href = a.browser_download_url;
          link.textContent = f.label;
          const size = document.createElement("span");
          size.textContent = mb(a.size);
          link.appendChild(size);
          li.appendChild(link);
          list.appendChild(li);
        });
        let primary = null;
        if (os === "mac") primary = find((await isArm()) ? /_aarch64\.dmg$/ : /_x64\.dmg$/);
        if (os === "windows") primary = find(/_x64-setup\.exe$/);
        if (os === "linux") primary = find(/_amd64\.AppImage$/) || find(/_amd64\.deb$/);
        if (primary) {
          dlButton.href = primary.browser_download_url;
          if (labels[os]) $("#dl-label").textContent = labels[os];
          $("#dl-size").textContent = `${release.tag_name} · ${mb(primary.size)}`;
        }
      })
      .catch(() => {
        $$("[data-files]").forEach((l) => {
          l.innerHTML = `<li><a href="https://github.com/${REPO}/releases">All downloads on GitHub<span>→</span></a></li>`;
        });
        const size = $("#dl-size");
        if (size) size.textContent = dlButton.dataset.soon || "The first release is on its way.";
      });
  }
})();
