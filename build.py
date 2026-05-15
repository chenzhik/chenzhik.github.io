"""
Build entry point.

Run: python build.py

To update content, edit files in data/:
  data/about.py    - name, bio, contacts
  data/avatar.py   - avatar greeting message
  data/archive.py  - archive entries

To change the page design, edit render.py.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from data.about import AVATAR, BIO, EMAIL, GITHUB, NAME, TITLE
from data.archive import ARCHIVE
from data.avatar import GREETING
from render import render_page

SITE = {
    "name": NAME,
    "title": TITLE,
    "bio": BIO,
    "avatar": AVATAR,
    "github": GITHUB,
    "email": EMAIL,
}

if __name__ == "__main__":
    html = render_page(SITE, GREETING, ARCHIVE)
    out = os.path.join(os.path.dirname(__file__), "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("Built index.html successfully.")
