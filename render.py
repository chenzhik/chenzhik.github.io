# ── render.py ─────────────────────────────────────────────────────────────────
# HTML / CSS templates. Edit this file only when changing the page design.

def _avatar_img(avatar, name):
    initial = name[0].upper() if name else "?"
    if avatar:
        return (
            f'<img src="{avatar}" alt="{name}" '
            f'onerror="this.style.display=\'none\';'
            f'this.nextElementSibling.style.display=\'flex\';" />'
            f'<div class="avatar-circle" style="display:none;">{initial}</div>'
        )
    return f'<div class="avatar-circle">{initial}</div>'


def _archive_rows(entries):
    rows = []
    for e in entries:
        rows.append(f"""
        <div class="archive-item">
          <span class="archive-date">{e['date']}</span>
          <div class="archive-body">
            <a href="{e['link']}" class="archive-title">{e['title']}</a>
            <p class="archive-desc">{e['desc']}</p>
          </div>
        </div>""")
    return "\n".join(rows)


# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:          #0f1117;
      --surface:     #1a1d27;
      --surface2:    #12141e;
      --border:      #2a2d3a;
      --accent:      #7c6af7;
      --accent-dim:  rgba(124, 106, 247, 0.15);
      --accent-soft: rgba(124, 106, 247, 0.25);
      --text:        #e2e4f0;
      --text-muted:  #7a7f9a;
      --text-link:   #a09bf8;
      --radius:      16px;
      --shadow:      0 4px 32px rgba(0,0,0,0.35);
      --font:        'Inter', 'Segoe UI', system-ui, sans-serif;
      --mono:        'JetBrains Mono', 'Fira Code', monospace;
    }

    html { scroll-behavior: smooth; }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--font);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 48px 20px 80px;
      line-height: 1.65;
    }

    .page {
      width: 100%;
      max-width: 680px;
      display: flex;
      flex-direction: column;
      gap: 28px;
    }

    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      box-shadow: var(--shadow);
    }

    .section-label {
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--text-muted);
      font-weight: 600;
      margin-bottom: 20px;
    }

    /* Nav */
    .navbar { display: flex; justify-content: center; gap: 10px; }

    .nav-btn {
      padding: 7px 22px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 999px;
      color: var(--text-muted);
      font-family: var(--mono);
      font-size: 0.82rem;
      text-decoration: none;
      transition: color 0.2s, border-color 0.2s, background 0.2s;
    }

    .nav-btn:hover {
      color: var(--text);
      border-color: var(--accent);
      background: var(--accent-dim);
    }

    /* About */
    .about-header { display: flex; align-items: center; gap: 20px; margin-bottom: 20px; }

    .about-avatar img,
    .avatar-circle {
      width: 80px; height: 80px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid var(--accent);
      box-shadow: 0 0 0 4px var(--accent-dim);
      display: flex; align-items: center; justify-content: center;
    }

    .avatar-circle {
      background: var(--accent-dim);
      font-size: 2rem; font-weight: 700; color: var(--accent);
    }

    .about-meta h1 { font-size: 1.45rem; font-weight: 700; letter-spacing: -0.01em; }

    .about-meta .title-tag {
      display: inline-block; margin-top: 5px;
      padding: 2px 10px;
      background: var(--accent-dim);
      border: 1px solid var(--accent-soft);
      border-radius: 999px;
      color: var(--accent);
      font-family: var(--mono); font-size: 0.78rem;
    }

    .about-divider { border: none; border-top: 1px solid var(--border); margin: 18px 0; }

    .bio { color: var(--text); font-size: 0.96rem; margin-bottom: 20px; }

    .contacts { display: flex; flex-wrap: wrap; gap: 10px; }

    .contact-chip {
      display: inline-flex; align-items: center; gap: 6px;
      padding: 6px 14px;
      background: var(--accent-dim);
      border: 1px solid rgba(124,106,247,0.3);
      border-radius: 999px;
      color: var(--text-link);
      font-size: 0.83rem; text-decoration: none;
      font-family: var(--mono);
      transition: background 0.2s, border-color 0.2s;
    }

    .contact-chip:hover { background: var(--accent-soft); border-color: var(--accent); }
    .contact-chip svg { width: 13px; height: 13px; flex-shrink: 0; fill: currentColor; }

    /* Chat */
    .chat-card { padding: 0; overflow: hidden; display: flex; flex-direction: column; }

    .chat-header {
      display: flex; align-items: center; gap: 10px;
      padding: 14px 20px;
      border-bottom: 1px solid var(--border);
      background: var(--surface2);
    }

    .chat-header-dot {
      width: 8px; height: 8px; border-radius: 50%;
      background: var(--accent); box-shadow: 0 0 6px var(--accent);
      animation: pulse 2.4s ease-in-out infinite;
    }

    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.35; } }

    .chat-header-title {
      font-size: 0.72rem; font-weight: 600;
      text-transform: uppercase; letter-spacing: 0.12em;
      color: var(--text-muted);
    }
    .chat-header-sub {
      font-size: 0.75rem; color: var(--text-muted);
      font-family: var(--mono); margin-left: auto;
    }

    .chat-messages {
      padding: 20px;
      display: flex; flex-direction: column; gap: 14px;
      min-height: 280px; max-height: 420px;
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
      background: var(--accent-dim); border: 1px solid var(--accent-soft);
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0; color: var(--accent);
    }
    .chat-icon svg { width: 13px; height: 13px; }

    .chat-bubble {
      max-width: 78%; padding: 10px 14px;
      border-radius: 14px; font-size: 0.9rem; line-height: 1.55;
    }

    .chat-bubble--ai {
      background: var(--surface2); border: 1px solid var(--border);
      color: var(--text); border-bottom-left-radius: 4px;
    }

    .chat-bubble--user {
      background: var(--accent-dim); border: 1px solid var(--accent-soft);
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
      background: var(--surface2);
    }

    .chat-input-wrap {
      flex: 1; position: relative;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 999px;
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
      background: var(--accent-dim); border: 1px solid var(--accent-soft);
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0; color: var(--accent);
      cursor: pointer;
      transition: background 0.2s, border-color 0.2s;
    }

    .chat-send-btn:hover { background: var(--accent-soft); border-color: var(--accent); }
    .chat-send-btn svg { width: 15px; height: 15px; fill: currentColor; }

    /* Archive */
    .archive-item {
      display: flex; align-items: flex-start; gap: 18px;
      padding: 16px 0; border-bottom: 1px solid var(--border);
    }
    .archive-item:last-child  { border-bottom: none; padding-bottom: 0; }
    .archive-item:first-child { padding-top: 0; }

    .archive-date {
      font-family: var(--mono); font-size: 0.78rem;
      color: var(--text-muted); white-space: nowrap;
      margin-top: 3px; min-width: 64px;
    }

    .archive-title {
      color: var(--text); text-decoration: none;
      font-size: 0.96rem; font-weight: 500; transition: color 0.2s;
    }
    .archive-title:hover { color: var(--text-link); }

    .archive-desc { color: var(--text-muted); font-size: 0.85rem; margin-top: 3px; }

    /* Footer */
    .footer { text-align: center; font-size: 0.78rem; color: var(--text-muted); font-family: var(--mono); }

    /* Responsive */
    @media (max-width: 480px) {
      .about-header { flex-direction: column; text-align: center; }
      .contacts     { justify-content: center; }
      .navbar       { gap: 6px; }
      .nav-btn      { padding: 6px 14px; }
      .chat-bubble  { max-width: 90%; }
    }
"""

# ── Chat JS ───────────────────────────────────────────────────────────────────

CHAT_JS = """
  const messages  = document.getElementById('chatMessages');
  const input     = document.getElementById('chatInput');
  const sendBtn   = document.getElementById('chatSend');

  // Simple keyword-based replies — edit as you like
  const REPLIES = [
    [/hello|hi|hey/i,           "Hey! Great to meet you. Ask me anything about this site's owner."],
    [/who|name|yourself/i,      "I'm the AI avatar on this page. I can tell you about the person behind this site — a developer passionate about clean code and open source."],
    [/work|project|build/i,     "They work on a range of projects — from developer tools to writing about things they learn. Check the Archive section for details!"],
    [/skill|language|tech/i,    "Python is a favourite, but they're comfortable across the stack. Always learning something new."],
    [/contact|email|reach/i,    "You can reach them via the links in the About section — GitHub and email are both there."],
    [/archive|post|blog/i,      "The Archive section below has posts and projects. Give it a scroll!"],
    [/thank/i,                  "You're welcome! Feel free to ask anything else."],
  ];

  const FALLBACK = "That's a great question! For more details, check the About section or reach out directly.";

  function getReply(text) {
    for (const [pattern, reply] of REPLIES) {
      if (pattern.test(text)) return reply;
    }
    return FALLBACK;
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
        <div class="chat-bubble chat-bubble--ai">${text}</div>`;
    } else {
      row.innerHTML = `<div class="chat-bubble chat-bubble--user">${text}</div>`;
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
    input.value = '';
    addBubble('user', text);
    showTyping();
    const delay = 600 + Math.random() * 600;
    setTimeout(() => {
      removeTyping();
      addBubble('ai', getReply(text));
    }, delay);
  }

  sendBtn.addEventListener('click', send);
  input.addEventListener('keydown', e => { if (e.key === 'Enter') send(); });
"""


# ── Page assembly ─────────────────────────────────────────────────────────────

def render_page(site, greeting, archive):
    avatar_img   = _avatar_img(site["avatar"], site["name"])
    archive_html = _archive_rows(archive)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{site['name']}</title>
  <style>{CSS}</style>
</head>
<body>
  <main class="page">

    <!-- Nav -->
    <nav class="navbar">
      <a class="nav-btn" href="#about">About</a>
      <a class="nav-btn" href="#archive">Archive</a>
      <a class="nav-btn" href="#avatar">Avatar</a>
    </nav>

    <!-- About -->
    <div id="about" class="card">
      <div class="section-label">About</div>
      <div class="about-header">
        <div class="about-avatar">{avatar_img}</div>
        <div class="about-meta">
          <h1>{site['name']}</h1>
          <span class="title-tag">{site['title']}</span>
        </div>
      </div>
      <hr class="about-divider" />
      <p class="bio">{site['bio']}</p>
      <div class="contacts">
        <a href="{site['github']}" class="contact-chip" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 .3C5.4.3 0 5.7 0 12.3c0 5.3 3.4 9.8 8.2 11.4.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.5-1.4-1.3-1.8-1.3-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17 4.7 18 5 18 5c.6 1.7.2 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6C20.6 22.1 24 17.6 24 12.3 24 5.7 18.6.3 12 .3z"/>
          </svg>
          {site['github'].replace('https://', '')}
        </a>
        <a href="mailto:{site['email']}" class="contact-chip">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 4H4C2.9 4 2 4.9 2 6v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/>
          </svg>
          {site['email']}
        </a>
      </div>
    </div>

    <!-- Archive -->
    <div id="archive" class="card">
      <div class="section-label">Archive</div>
      <div class="archive-list">
        {archive_html}
      </div>
    </div>

    <!-- Avatar: interactive AI chat -->
    <div id="avatar" class="card chat-card">
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
          <div class="chat-bubble chat-bubble--ai">{greeting}</div>
        </div>
      </div>

      <div class="chat-input-bar">
        <div class="chat-input-wrap">
          <input
            id="chatInput"
            class="chat-input-real"
            type="text"
            placeholder="Ask me anything…"
            autocomplete="off"
          />
        </div>
        <button class="chat-send-btn" id="chatSend" aria-label="Send">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M2 21l21-9L2 3v7l15 2-15 2v7z"/>
          </svg>
        </button>
      </div>
    </div>

    <footer class="footer">
      built with python &middot; hosted on github pages
    </footer>

  </main>
  <script>{CHAT_JS}</script>
</body>
</html>
"""
