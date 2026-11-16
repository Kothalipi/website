#!/usr/bin/env python3
"""Local preview server that mimics GitHub Pages: /download serves download.html."""
import http.server
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4321


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def do_GET(self):
        path = self.path.split("?")[0].split("#")[0]
        full = os.path.join(ROOT, path.lstrip("/"))
        if not os.path.exists(full) and not path.endswith("/") and os.path.exists(full + ".html"):
            self.path = path + ".html"
        super().do_GET()


http.server.ThreadingHTTPServer(("", PORT), Handler).serve_forever()
