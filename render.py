# render.py
# HTML / CSS templates. Edit this file only when changing the page design.
from html import escape


def _text(value):
    return escape(str(value), quote=False)


def _attr(value):
    return escape(str(value), quote=True)

def _avatar_img(avatar, name):
    initial = next((char.upper() for char in name if char.isalnum()), "?") if name else "?"
    if avatar:
        avatar_src = _attr(avatar)
        avatar_alt = _attr(name)
        initial_text = _text(initial)
        return (
            f'<img src="{avatar_src}" alt="{avatar_alt}" '
            f'onerror="this.style.display=\'none\';'
            f'this.nextElementSibling.style.display=\'flex\';" />'
            f'<div class="avatar-circle" style="display:none;">{initial_text}</div>'
        )
    return f'<div class="avatar-circle">{_text(initial)}</div>'


def _archive_rows(entries):
    rows = []
    for e in entries:
        rows.append(f"""
        <div class="archive-item">
          <span class="archive-date">{_text(e['date'])}</span>
          <div class="archive-body">
            <a href="{_attr(e['link'])}" class="archive-title">{_text(e['title'])}</a>
            <p class="archive-desc">{_text(e['desc'])}</p>
          </div>
        </div>""")
    return "\n".join(rows)


# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:          #f6f7fb;
      --surface:     #ffffff;
      --surface2:    #f1f5f9;
      --border:      #d9e0ea;
      --accent:      #0f766e;
      --accent-dim:  rgba(15, 118, 110, 0.10);
      --accent-soft: rgba(15, 118, 110, 0.20);
      --text:        #172033;
      --text-muted:  #667085;
      --text-link:   #1d4ed8;
      --radius:      8px;
      --shadow:      0 18px 50px rgba(23, 32, 51, 0.08);
      --font:        'Segoe UI', 'Inter', system-ui, -apple-system, sans-serif;
      --mono:        'SFMono-Regular', 'Cascadia Mono', 'JetBrains Mono', monospace;
    }

    html { scroll-behavior: smooth; }

    body {
      background:
        linear-gradient(180deg, #ffffff 0, var(--bg) 320px);
      color: var(--text);
      font-family: var(--font);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 32px 20px 64px;
      line-height: 1.6;
    }

    .page {
      width: 100%;
      max-width: 1040px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    .content-grid {
      display: grid;
      grid-template-columns: minmax(340px, 1fr) minmax(0, 1.35fr);
      gap: 18px;
      align-items: start;
    }

    .main-column { min-width: 0; }

    .archive-card {
      grid-column: 1 / -1;
    }

    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 26px;
      box-shadow: var(--shadow);
    }

    .section-label {
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      font-weight: 700;
      margin-bottom: 18px;
    }

    /* Nav */
    .navbar {
      display: flex;
      justify-content: flex-end;
      gap: 6px;
      padding: 3px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: 0 8px 30px rgba(23, 32, 51, 0.05);
      width: fit-content;
      align-self: flex-end;
    }

    .nav-btn {
      padding: 7px 14px;
      border-radius: 6px;
      color: var(--text-muted);
      font-family: var(--mono);
      font-size: 0.78rem;
      text-decoration: none;
      transition: color 0.2s, background 0.2s;
    }

    .nav-btn:hover {
      color: var(--text);
      background: var(--accent-dim);
    }

    /* About */
    .about-card { position: static; }

    .about-header {
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      gap: 18px;
      margin-bottom: 22px;
    }

    .about-avatar img,
    .avatar-circle {
      width: 86px; height: 86px;
      border-radius: 18px;
      object-fit: cover;
      border: 1px solid var(--border);
      box-shadow: inset 0 0 0 1px rgba(255,255,255,0.7);
      display: flex; align-items: center; justify-content: center;
    }

    .avatar-circle {
      background:
        linear-gradient(135deg, var(--accent-dim), rgba(29, 78, 216, 0.10)),
        var(--surface2);
      font-size: 2.25rem; font-weight: 750; color: var(--accent);
    }

    .about-meta h1 {
      font-size: clamp(1.55rem, 2.4vw, 2.1rem);
      line-height: 1.08;
      font-weight: 760;
      letter-spacing: 0;
      white-space: nowrap;
    }

    .about-meta .title-tag {
      display: inline-block; margin-top: 12px;
      padding: 4px 10px;
      background: var(--accent-dim);
      border: 1px solid var(--accent-soft);
      border-radius: 6px;
      color: var(--accent);
      font-family: var(--mono); font-size: 0.76rem;
      font-weight: 650;
    }

    .about-divider { border: none; border-top: 1px solid var(--border); margin: 18px 0; }

    .bio { color: var(--text); font-size: 0.98rem; margin-bottom: 20px; }

    .contacts { display: flex; flex-wrap: wrap; gap: 10px; }

    .contact-chip {
      display: inline-flex; align-items: center; gap: 6px;
      padding: 7px 10px;
      background: var(--surface2);
      border: 1px solid var(--border);
      border-radius: 6px;
      color: var(--text-link);
      font-size: 0.78rem; text-decoration: none;
      font-family: var(--mono);
      transition: background 0.2s, border-color 0.2s;
    }

    .contact-chip:hover { background: #eef6ff; border-color: #bfdbfe; }
    .contact-chip svg { width: 13px; height: 13px; flex-shrink: 0; fill: currentColor; }

    /* Chat */
    .chat-card { padding: 0; overflow: hidden; display: flex; flex-direction: column; }

    .chat-header {
      display: flex; align-items: center; gap: 10px;
      padding: 13px 18px;
      border-bottom: 1px solid var(--border);
      background: var(--surface2);
    }

    .chat-header-dot {
      width: 8px; height: 8px; border-radius: 50%;
      background: #f59e0b; box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.16);
      animation: pulse 2.4s ease-in-out infinite;
    }

    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.35; } }

    .chat-header-title {
      font-size: 0.72rem; font-weight: 600;
      text-transform: uppercase; letter-spacing: 0.12em;
      color: var(--text);
    }
    .chat-header-sub {
      font-size: 0.75rem; color: var(--text-muted);
      font-family: var(--mono); margin-left: auto;
    }

    .chat-messages {
      padding: 20px;
      display: flex; flex-direction: column; gap: 14px;
      flex: 1;
      min-height: 0;
      overflow-y: auto;
    }

    /* Scrollbar */
    .chat-messages::-webkit-scrollbar { width: 4px; }
    .chat-messages::-webkit-scrollbar-track { background: transparent; }
    .chat-messages::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }

    .chat-row       { display: flex; align-items: flex-end; gap: 10px; }
    .chat-row--user { flex-direction: row-reverse; }

    .chat-icon {
      width: 28px; height: 28px; border-radius: 50%;
      background: var(--surface2); border: 1px solid var(--border);
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0; color: var(--accent);
    }
    .chat-icon svg { width: 13px; height: 13px; }

    .chat-bubble {
      max-width: 78%; padding: 10px 13px;
      border-radius: 8px; font-size: 0.9rem; line-height: 1.55;
    }

    .chat-bubble--ai {
      background: var(--surface2); border: 1px solid var(--border);
      color: var(--text); border-bottom-left-radius: 4px;
    }

    .chat-bubble--user {
      background: #ecfdf5; border: 1px solid #bbf7d0;
      color: var(--text); border-bottom-right-radius: 4px;
    }

    /* Typing indicator */
    .typing-dot {
      display: inline-block;
      width: 6px; height: 6px; border-radius: 50%;
      background: var(--text-muted); margin: 0 2px;
      animation: typing-bounce 1.2s ease-in-out infinite;
    }
    .typing-dot:nth-child(2) { animation-delay: 0.2s; }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; }

    @keyframes typing-bounce {
      0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
      30%            { transform: translateY(-5px); opacity: 1; }
    }

    /* Input bar */
    .chat-input-bar {
      display: flex; align-items: center; gap: 10px;
      padding: 12px 16px;
      border-top: 1px solid var(--border);
      background: var(--surface);
    }

    .chat-input-wrap {
      flex: 1; position: relative;
      background: var(--surface2);
      border: 1px solid var(--border);
      border-radius: 8px;
      transition: border-color 0.2s;
    }

    .chat-input-wrap:focus-within {
      border-color: var(--accent);
      box-shadow: 0 0 0 3px var(--accent-dim);
    }

    .chat-input-real {
      width: 100%;
      background: transparent;
      border: none; outline: none;
      padding: 9px 16px;
      color: var(--text);
      font-family: var(--font); font-size: 0.87rem;
      caret-color: var(--accent);
    }

    .chat-input-real::placeholder { color: var(--text-muted); }

    .chat-send-btn {
      width: 34px; height: 34px; border-radius: 50%;
      background: var(--accent); border: 1px solid var(--accent);
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0; color: #ffffff;
      cursor: pointer;
      transition: background 0.2s, transform 0.2s;
    }

    .chat-send-btn:hover { background: #115e59; transform: translateY(-1px); }
    .chat-send-btn:disabled { cursor: not-allowed; opacity: 0.55; transform: none; }
    .chat-send-btn svg { width: 15px; height: 15px; fill: currentColor; }

    /* Archive */
    .archive-item {
      display: flex; align-items: flex-start; gap: 18px;
      padding: 17px 0; border-bottom: 1px solid var(--border);
    }
    .archive-item:last-child  { border-bottom: none; padding-bottom: 0; }
    .archive-item:first-child { padding-top: 0; }

    .archive-date {
      font-family: var(--mono); font-size: 0.78rem;
      color: var(--text-muted); white-space: nowrap;
      margin-top: 3px; min-width: 72px;
    }

    .archive-title {
      color: var(--text); text-decoration: none;
      font-size: 1rem; font-weight: 650; transition: color 0.2s;
    }
    .archive-title:hover { color: var(--text-link); }

    .archive-desc { color: var(--text-muted); font-size: 0.9rem; margin-top: 3px; }

    /* Footer */
    .footer { text-align: right; font-size: 0.76rem; color: var(--text-muted); font-family: var(--mono); }

    /* Responsive */
    @media (max-width: 760px) {
      body          { padding: 20px 14px 48px; }
      .content-grid { grid-template-columns: 1fr; }
      .about-card   { position: static; }
      .chat-card    { height: auto !important; }
      .about-header { align-items: center; }
      .navbar       { width: 100%; justify-content: space-between; align-self: stretch; }
      .nav-btn      { flex: 1; text-align: center; padding: 7px 8px; }
      .card         { padding: 22px; }
      .about-meta h1 { white-space: normal; }
      .chat-bubble  { max-width: 90%; }
      .footer       { text-align: center; }
    }

    @media (max-width: 460px) {
      .archive-item { display: block; }
      .archive-date { display: block; margin: 0 0 4px; }
      .chat-header-sub { display: none; }
    }
"""

# ── Chat JS ───────────────────────────────────────────────────────────────────

CHAT_JS = """
  const messages  = document.getElementById('chatMessages');
  const input     = document.getElementById('chatInput');
  const sendBtn   = document.getElementById('chatSend');
  const aboutCard = document.getElementById('about');
  const avatarPanel = document.getElementById('avatar');
  const MAX_TURNS = 3;
  const FIXED_REPLY = 'self evolving now...';
  let turnCount = 0;

  // Simple keyword-based replies - edit as you like.
  const REPLIES = [
    [/hello|hi|hey/i,           "Hey! Great to meet you. Ask me anything about this site's owner."],
    [/who|name|yourself/i,      "I'm the AI avatar on this page. I can tell you about the person behind this site - a developer passionate about clean code and open source."],
    [/work|project|build/i,     "They work on a range of projects - from developer tools to writing about things they learn. Check the Archive section for details!"],
    [/skill|language|tech/i,    "Python is a favourite, but they're comfortable across the stack. Always learning something new."],
    [/contact|email|reach/i,    "You can reach them via the links in the About section - GitHub and email are both there."],
    [/archive|post|blog/i,      "The Archive section below has posts and projects. Give it a scroll!"],
    [/thank/i,                  "You're welcome! Feel free to ask anything else."],
  ];

  const FALLBACK = "That's a great question! For more details, check the About section or reach out directly.";

  function getReply(text) {
    return FIXED_REPLY;
  }

  function escapeHTML(text) {
    const node = document.createElement('div');
    node.textContent = text;
    return node.innerHTML;
  }

  function addBubble(role, text) {
    const row = document.createElement('div');
    row.className = 'chat-row chat-row--' + (role === 'ai' ? 'ai' : 'user');

    if (role === 'ai') {
      row.innerHTML = `
        <div class="chat-icon">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2L13.09 8.26L19 7L14.74 11.74L21 13L14.74 14.26L19 19L13.09 15.74L12 22L10.91 15.74L5 19L9.26 14.26L3 13L9.26 11.74L5 7L10.91 8.26L12 2Z" fill="currentColor"/>
          </svg>
        </div>
        <div class="chat-bubble chat-bubble--ai">${escapeHTML(text)}</div>`;
    } else {
      row.innerHTML = `<div class="chat-bubble chat-bubble--user">${escapeHTML(text)}</div>`;
    }

    messages.appendChild(row);
    messages.scrollTop = messages.scrollHeight;
    return row;
  }

  function showTyping() {
    const row = document.createElement('div');
    row.className = 'chat-row chat-row--ai';
    row.id = 'typingIndicator';
    row.innerHTML = `
      <div class="chat-icon">
        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 2L13.09 8.26L19 7L14.74 11.74L21 13L14.74 14.26L19 19L13.09 15.74L12 22L10.91 15.74L5 19L9.26 14.26L3 13L9.26 11.74L5 7L10.91 8.26L12 2Z" fill="currentColor"/>
        </svg>
      </div>
      <div class="chat-bubble chat-bubble--ai" style="padding: 12px 16px;">
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
      </div>`;
    messages.appendChild(row);
    messages.scrollTop = messages.scrollHeight;
  }

  function removeTyping() {
    const el = document.getElementById('typingIndicator');
    if (el) el.remove();
  }

  function send() {
    const text = input.value.trim();
    if (!text) return;
    if (turnCount >= MAX_TURNS) return;

    turnCount += 1;
    input.value = '';
    addBubble('user', text);
    showTyping();
    const delay = 600 + Math.random() * 600;
    setTimeout(() => {
      removeTyping();
      addBubble('ai', getReply(text));
      if (turnCount >= MAX_TURNS) {
        input.disabled = true;
        sendBtn.disabled = true;
        input.placeholder = 'self evolving now...';
      }
    }, delay);
  }

  function syncAvatarHeight() {
    if (!aboutCard || !avatarPanel) return;

    if (window.matchMedia('(max-width: 760px)').matches) {
      avatarPanel.style.height = '';
      return;
    }

    avatarPanel.style.height = aboutCard.offsetHeight + 'px';
  }

  sendBtn.addEventListener('click', send);
  input.addEventListener('keydown', e => { if (e.key === 'Enter') send(); });
  window.addEventListener('resize', syncAvatarHeight);
  window.addEventListener('load', syncAvatarHeight);
  syncAvatarHeight();
"""


# ── Page assembly ─────────────────────────────────────────────────────────────

def render_page(site, greeting, archive):
    avatar_img   = _avatar_img(site["avatar"], site["name"])
    archive_html = _archive_rows(archive)
    name = _text(site["name"])
    title = _text(site["title"])
    bio = _text(site["bio"])
    github_url = _attr(site["github"])
    github_label = _text(site["github"].replace("https://", ""))
    email = _text(site["email"])
    email_href = _attr(site["email"])
    greeting_text = _text(greeting)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{name}</title>
  <style>{CSS}</style>
</head>
<body>
  <main class="page">

    <!-- Nav -->
    <nav class="navbar">
      <a class="nav-btn" href="#about">About</a>
      <a class="nav-btn" href="#avatar">Avatar</a>
      <a class="nav-btn" href="#archive">Archive</a>
    </nav>

    <div class="content-grid">
      <!-- About -->
      <aside id="about" class="card about-card">
        <div class="section-label">About</div>
        <div class="about-header">
          <div class="about-avatar">{avatar_img}</div>
          <div class="about-meta">
            <h1>{name}</h1>
            <span class="title-tag">{title}</span>
          </div>
        </div>
        <hr class="about-divider" />
        <p class="bio">{bio}</p>
        <div class="contacts">
          <a href="{github_url}" class="contact-chip" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 .3C5.4.3 0 5.7 0 12.3c0 5.3 3.4 9.8 8.2 11.4.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.5-1.4-1.3-1.8-1.3-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17 4.7 18 5 18 5c.6 1.7.2 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6C20.6 22.1 24 17.6 24 12.3 24 5.7 18.6.3 12 .3z"/>
            </svg>
            {github_label}
          </a>
          <a href="mailto:{email_href}" class="contact-chip">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M20 4H4C2.9 4 2 4.9 2 6v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/>
            </svg>
            {email}
          </a>
        </div>
      </aside>

      <div class="main-column">
        <!-- Avatar: interactive AI chat -->
        <section id="avatar" class="card chat-card">
      <div class="chat-header">
        <div class="chat-header-dot"></div>
        <span class="chat-header-title">AVATAR</span>
        <span class="chat-header-sub">always online</span>
      </div>

      <div class="chat-messages" id="chatMessages">
        <!-- greeting -->
        <div class="chat-row chat-row--ai">
          <div class="chat-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2L13.09 8.26L19 7L14.74 11.74L21 13L14.74 14.26L19 19L13.09 15.74L12 22L10.91 15.74L5 19L9.26 14.26L3 13L9.26 11.74L5 7L10.91 8.26L12 2Z" fill="currentColor"/>
            </svg>
          </div>
          <div class="chat-bubble chat-bubble--ai">{greeting_text}</div>
        </div>
      </div>

      <div class="chat-input-bar">
        <div class="chat-input-wrap">
          <input
            id="chatInput"
            class="chat-input-real"
            type="text"
            placeholder="Ask me anything..."
            autocomplete="off"
          />
        </div>
        <button class="chat-send-btn" id="chatSend" aria-label="Send">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M2 21l21-9L2 3v7l15 2-15 2v7z"/>
          </svg>
        </button>
      </div>
        </section>
      </div>

      <!-- Archive -->
      <section id="archive" class="card archive-card">
        <div class="section-label">Archive</div>
        <div class="archive-list">
          {archive_html}
        </div>
      </section>
    </div>

    <footer class="footer">
      built with python &middot; hosted on github pages
    </footer>

  </main>
  <script>{CHAT_JS}</script>
</body>
</html>
"""
