import os
import json
import sqlite3
import threading
import time
from flask import Flask, render_template_string, request, jsonify
import praw
from google import genai

# ==========================================
# 1. KONFIGURÁCIÓ (Töltsd ki a saját kulcsaiddal)
# ==========================================
REDDIT_CLIENT_ID = "IDE_A_CLIENT_ID"
REDDIT_CLIENT_SECRET = "IDE_A_CLIENT_SECRET"
REDDIT_USERNAME = "IDE_A_REDDIT_FELHASZNALONEVED"
REDDIT_PASSWORD = "IDE_A_REDDIT_JELSZAVAD"
REDDIT_USER_AGENT = "OverlordCyberSOCAssistant/1.0 by u/" + REDDIT_USERNAME

GEMINI_API_KEY = "IDE_A_GEMINI_API_KULCSOD"

# A DDoS műhelyed rövid szakmai leírása, hogy az AI tűpontosan válaszoljon
PROJECT_CONTEXT = """
Project: CyberSOC Edition - Interactive Browser-Based DDoS & BGP RTBH Simulator.
Tech stack: Zero-dependency pure web architecture, real-time packet flow visualization,
Red Team attack vectors (DNS Reflection, HTTP GET Flood, SYN Flood) vs. Blue Team mitigations
(BGP RTBH Blackhole, WAF/Scrubbing, Rate Limiting, SYN Cookies), live PPS metrics, Wireshark PDU sniffer & Cisco IOS CLI simulation.
Tone: Concise, senior network/security engineer, helpful, zero marketing fluff.
"""

DB_FILE = "reddit_queue.db"
app = Flask(__name__)

# ==========================================
# 2. ADATBÁZIS (Hogy ne duplikáljon kommenteket)
# ==========================================
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS comments (
        id TEXT PRIMARY KEY,
        post_title TEXT,
        author TEXT,
        body TEXT,
        permalink TEXT,
        draft_en TEXT,
        draft_hu TEXT,
        status TEXT DEFAULT 'pending'
    )''')
    conn.commit()
    conn.close()

init_db()

# ==========================================
# 3. AI VÁLASZGENERÁLÓ MOTOR
# ==========================================
ai_client = genai.Client(api_key=GEMINI_API_KEY)

def generate_reply_draft(post_title, comment_author, comment_body):
    prompt = f"""
    You are acting as a senior network & cybersecurity engineer replying to a Reddit comment on your project post.
    Project Context: {PROJECT_CONTEXT}
    Post Title: {post_title}
    Comment by u/{comment_author}: "{comment_body}"

    Task:
    1. Write a sharp, technically accurate, friendly English reply (2-4 sentences max, no hype, pure engineering).
    2. Provide a short Hungarian translation/summary of your reply so the owner can review it in 2 seconds.

    Return ONLY valid JSON with keys: "en" and "hu".
    """
    try:
        response = ai_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={"response_mime_type": "application/json"}
        )
        data = json.loads(response.text)
        return data.get("en", ""), data.get("hu", "")
    except Exception as e:
        return f"Thanks for the feedback! ({e})", "Hiba a generáláskor."

# ==========================================
# 4. HÁTTÉRBEN FUTÓ REDDIT FIGYELŐ
# ==========================================
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent=REDDIT_USER_AGENT
)

def poll_reddit_inbox():
    while True:
        try:
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            for item in reddit.inbox.unread(limit=15):
                if isinstance(item, praw.models.Comment):
                    c.execute("SELECT id FROM comments WHERE id = ?", (item.id,))
                    if not c.fetchone():
                        post_title = item.submission.title
                        draft_en, draft_hu = generate_reply_draft(post_title, str(item.author), item.body)
                        c.execute(
                            "INSERT INTO comments (id, post_title, author, body, permalink, draft_en, draft_hu) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (item.id, post_title, str(item.author), item.body, f"https://reddit.com{item.permalink}", draft_en, draft_hu)
                        )
                        conn.commit()
                        item.mark_read()
            conn.close()
        except Exception as e:
            print(f"[FIGYELŐ HIBA]: {e}")
        time.sleep(60) # 60 másodpercenként néz rá az új kommentekre

# ==========================================
# 5. LOKÁLIS OVERLORD IRÁNYÍTÓPULT (UI)
# ==========================================
HTML_UI = """
<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="UTF-8">
<title>Overlord Reddit Asszisztens</title>
<style>
  body { background: #0b111a; color: #e2e8f0; font-family: system-ui, sans-serif; margin: 0; padding: 24px; }
  h1 { color: #38bdf8; font-size: 20px; border-bottom: 1px solid #1e293b; padding-bottom: 12px; }
  .card { background: #111827; border: 1px solid #1e293b; border-radius: 8px; padding: 16px; margin-bottom: 16px; }
  .meta { font-size: 12px; color: #94a3b8; margin-bottom: 8px; }
  .incoming { background: #0f172a; padding: 10px; border-left: 3px solid #f59e0b; margin-bottom: 12px; font-size: 14px; }
  textarea { width: 100%; height: 80px; background: #090d16; color: #34d399; border: 1px solid #334155; border-radius: 6px; padding: 8px; font-family: monospace; font-size: 13px; box-sizing: border-box; }
  .hu { font-size: 12px; color: #94a3b8; margin: 6px 0 12px 0; font-style: italic; }
  button { padding: 8px 16px; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; margin-right: 8px; }
  .send { background: #10b981; color: #052e16; }
  .regen { background: #3b82f6; color: white; }
  .drop { background: #ef4444; color: white; }
</style>
</head>
<body>
  <h1>⚡ OVERLORD REDDIT FÉLAUTOMATA KEZELŐPULT (Jóváhagyásra váró kommentek)</h1>
  <div id="list"></div>
<script>
async function load() {
  const res = await fetch('/api/pending');
  const items = await res.json();
  const list = document.getElementById('list');
  if (!items.length) { list.innerHTML = '<p style="color:#64748b">Nincs új függőben lévő komment. A figyelő 60 mp-enként frissít.</p>'; return; }
  list.innerHTML = items.map(i => `
    <div class="card" id="c-${i.id}">
      <div class="meta">Poszt: <b>${i.post_title}</b> | Kérdező: <b>u/${i.author}</b> | <a href="${i.permalink}" target="_blank" style="color:#38bdf8">Megnyitás</a></div>
      <div class="incoming">${i.body}</div>
      <textarea id="txt-${i.id}">${i.draft_en}</textarea>
      <div class="hu">🇭🇺 Jelentése: ${i.draft_hu}</div>
      <button class="send" onclick="sendReply('${i.id}')">✔ Jóváhagyás és Küldés</button>
      <button class="drop" onclick="ignoreItem('${i.id}')">✖ Elvetés</button>
    </div>
  `).join('');
}
async function sendReply(id) {
  const text = document.getElementById('txt-' + id).value;
  await fetch('/api/send', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({id, text}) });
  load();
}
async function ignoreItem(id) {
  await fetch('/api/ignore', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({id}) });
  load();
}
load();
setInterval(load, 15000);
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_UI)

@app.route("/api/pending")
def get_pending():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id, post_title, author, body, permalink, draft_en, draft_hu FROM comments WHERE status = 'pending'")
    rows = [{"id": r[0], "post_title": r[1], "author": r[2], "body": r[3], "permalink": r[4], "draft_en": r[5], "draft_hu": r[6]} for r in c.fetchall()]
    conn.close()
    return jsonify(rows)

@app.route("/api/send", methods=["POST"])
def send_reply():
    data = request.json
    comment = reddit.comment(id=data["id"])
    comment.reply(data["text"])
    conn = sqlite3.connect(DB_FILE)
    conn.execute("UPDATE comments SET status = 'sent' WHERE id = ?", (data["id"],))
    conn.commit()
    conn.close()
    return jsonify({"ok": True})

@app.route("/api/ignore", methods=["POST"])
def ignore_item():
    data = request.json
    conn = sqlite3.connect(DB_FILE)
    conn.execute("UPDATE comments SET status = 'ignored' WHERE id = ?", (data["id"],))
    conn.commit()
    conn.close()
    return jsonify({"ok": True})

if __name__ == "__main__":
    threading.Thread(target=poll_reddit_inbox, daemon=True).start()
    app.run(port=5050)
