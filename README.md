# Homepage

A personal homepage for GitHub Pages, generated from pure Python.

## Quick Start

```bash
python build.py
```

This produces `index.html`. Open it in a browser to preview, or push it to GitHub Pages to publish.

---

## File Structure

```text
homepage/
├── build.py          # Entry point: run this to regenerate index.html
├── render.py         # Page design: HTML structure, CSS, and chat behavior
├── data/
│   ├── about.py      # Name, bio, avatar, and contact links
│   ├── avatar.py     # Avatar section opening message
│   └── archive.py    # Archive section posts and projects list
└── index.html        # Generated output: commit this to GitHub Pages
```

---

## Customization

### About: `data/about.py`

```python
NAME   = "Your Name"
TITLE  = "Your Role"          # shown as a tag below your name
BIO    = "A sentence or two about yourself."

AVATAR = "avatar.jpg"         # path to a local image, a URL, or "" for a letter placeholder
GITHUB = "https://github.com/yourusername"
EMAIL  = "you@example.com"
```

To use a profile photo, place `avatar.jpg` in the project root and set `AVATAR = "avatar.jpg"`.

### Archive: `data/archive.py`

Add, remove, or reorder entries in the `ARCHIVE` list:

```python
ARCHIVE = [
    {
        "date":  "2025-06",
        "title": "My Post Title",
        "desc":  "A one-line description.",
        "link":  "https://example.com/my-post",  # or "#" as a placeholder
    },
]
```

Entries are displayed in the order listed.

### Avatar Chat: `data/avatar.py`

Edit the `GREETING` string to change the opening message:

```python
GREETING = "Hi! Ask me anything."
```

Keyword-based replies are defined in `render.py` inside the `CHAT_JS` string.

### Design: `render.py`

CSS variables at the top of the `CSS` string control the color scheme:

```css
--bg:      #0f1117;  /* page background */
--surface: #1a1d27;  /* card background */
--accent:  #7c6af7;  /* highlight color */
--text:    #e2e4f0;  /* primary text */
```

Change these to retheme the page without touching the HTML structure.

---

## Deployment to GitHub Pages

1. Create a repository named `<yourusername>.github.io` on GitHub.
2. Run `python build.py` to generate the latest `index.html`.
3. Push `index.html` and `avatar.jpg` if used to the `main` branch.

```bash
git init
git add index.html avatar.jpg
git commit -m "deploy homepage"
git branch -M main
git remote add origin https://github.com/yourusername/yourusername.github.io.git
git push -u origin main
```

For subsequent updates, regenerate and push:

```bash
python build.py
git add index.html
git commit -m "update"
git push
```
