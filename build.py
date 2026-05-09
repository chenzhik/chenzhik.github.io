"""
build.py — entry point
Run: python build.py

To update content, edit files in data/:
  data/about.py    ← name, bio, contacts
  data/avatar.py   ← Avatar greeting message
  data/archive.py  ← Archive entries

To change the page design, edit render.py.
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from data.about   import NAME, TITLE, BIO, AVATAR, GITHUB, EMAIL
from data.avatar  import GREETING
from data.archive import ARCHIVE
from render       import render_page

SITE = {
    "name":   NAME,
    "title":  TITLE,
    "bio":    BIO,
    "avatar": AVATAR,
    "github": GITHUB,
    "email":  EMAIL,
}

if __name__ == "__main__":
    html = render_page(SITE, GREETING, ARCHIVE)
    out  = os.path.join(os.path.dirname(__file__), "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("Built index.html successfully.")
