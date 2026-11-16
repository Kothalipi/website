#!/usr/bin/env python3
"""SEO and integrity checks for the built site. Exits 1 on any problem."""
import glob
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://kothalipi.tashanto.com"
problems = []


def fail(page, msg):
    problems.append(f"{page}: {msg}")


def file_for(path):
    path = path.split("#")[0].split("?")[0]
    if path.endswith("/"):
        return os.path.join(ROOT, path.lstrip("/"), "index.html")
    cand = os.path.join(ROOT, path.lstrip("/"))
    if os.path.isfile(cand):
        return cand
    return cand + ".html"


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0; self.links = []; self.imgs = []; self.title = ""; self._t = False
        self.meta = {}; self.canon = None; self.alts = {}; self.ld = []; self._ld = False; self.ids = set(); self.lang = None
    def handle_starttag(self, tag, a):
        a = dict(a)
        if "id" in a: self.ids.add(a["id"])
        if tag == "html": self.lang = a.get("lang")
        if tag == "h1": self.h1 += 1
        if tag == "title": self._t = True
        if tag == "a" and a.get("href"): self.links.append(a["href"])
        if tag == "img": self.imgs.append(a)
        if tag == "meta" and a.get("name"): self.meta[a["name"]] = a.get("content", "")
        if tag == "meta" and a.get("property"): self.meta[a["property"]] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical": self.canon = a.get("href")
        if tag == "link" and a.get("rel") == "alternate" and a.get("hreflang"): self.alts[a["hreflang"]] = a.get("href")
        if tag == "script" and a.get("type") == "application/ld+json": self._ld = True; self.ld.append("")
    def handle_endtag(self, tag):
        if tag == "title": self._t = False
        if tag == "script": self._ld = False
    def handle_data(self, d):
        if self._t: self.title += d
        if self._ld: self.ld[-1] += d


pages = [p for p in glob.glob(ROOT + "/**/*.html", recursive=True) if "/tools/" not in p and "/node_modules/" not in p]
parsed = {}
for f in pages:
    rel = os.path.relpath(f, ROOT)
    pr = P(); pr.feed(open(f, encoding="utf-8").read()); parsed[rel] = pr
for rel, pr in parsed.items():
    if rel == "404.html":
        continue
    if pr.h1 != 1: fail(rel, f"{pr.h1} h1 tags")
    if not (15 <= len(pr.title) <= 72): fail(rel, f"title length {len(pr.title)}: {pr.title}")
    d = pr.meta.get("description", "")
    if not (70 <= len(d) <= 175): fail(rel, f"description length {len(d)}")
    if not pr.canon or not pr.canon.startswith(SITE): fail(rel, "bad canonical")
    if not pr.meta.get("og:image") or not pr.meta.get("twitter:card"): fail(rel, "missing og/twitter")
    if pr.alts and "x-default" not in pr.alts: fail(rel, "hreflang without x-default")
    for i in pr.imgs:
        if "alt" not in i: fail(rel, f"img without alt: {i.get('src')}")
        if not i.get("width") or not i.get("height"): fail(rel, f"img without size: {i.get('src')}")
    for j in pr.ld:
        try: json.loads(j)
        except Exception as e: fail(rel, f"bad JSON-LD: {e}")
    for href in pr.links:
        if href.startswith(("http", "mailto:", "#")): continue
        if not href.startswith("/"): fail(rel, f"relative link {href}"); continue
        target = file_for(href)
        if not os.path.isfile(target): fail(rel, f"broken link {href}"); continue
        if "#" in href:
            frag = href.split("#")[1]; trel = os.path.relpath(target, ROOT)
            if trel in parsed and frag not in parsed[trel].ids: fail(rel, f"missing anchor {href}")
# sitemap
sm = open(os.path.join(ROOT, "sitemap.xml")).read()
locs = re.findall(r"<loc>([^<]+)</loc>", sm)
for loc in locs:
    if not os.path.isfile(file_for(loc[len(SITE):] or "/")): fail("sitemap", f"{loc} has no file")
if len(set(locs)) != len(locs): fail("sitemap", "duplicate urls")
titles = {}
for rel, pr in parsed.items():
    titles.setdefault(pr.title, []).append(rel)
for t, rels in titles.items():
    if len(rels) > 1 and t: fail(",".join(rels), "duplicate title")
print(f"checked {len(parsed)} pages, {len(locs)} sitemap urls")
if problems:
    print("\n".join(problems)); sys.exit(1)
print("all checks passed")
