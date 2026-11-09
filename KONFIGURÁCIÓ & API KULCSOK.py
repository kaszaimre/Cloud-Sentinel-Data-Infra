import time
import praw
import openai

# --- 1. KONFIGURÁCIÓ & API KULCSOK ---
REDDIT_CLIENT_ID = "YOUR_REDDIT_CLIENT_ID"
REDDIT_CLIENT_SECRET = "YOUR_REDDIT_CLIENT_SECRET"
REDDIT_USER_AGENT = "android:technohound.vanguard:v1.0 (by /u/YOUR_REDDIT_USERNAME)"
REDDIT_USERNAME = "YOUR_REDDIT_USERNAME"
REDDIT_PASSWORD = "YOUR_REDDIT_PASSWORD"

OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# Célzott subredditek listája
SUBREDDITS_TO_MONITOR = "daytrading+dividends+stocks+options+AndroidApps"

# Kulcsszavak, amikre az ügynök azonnal lecsap
TARGET_KEYWORDS = [
    "position size", "reverse split", "risk reward", 
    "fibonacci", "drip calculator", "trading tool"
]

# Inicializálás
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD
)
openai.api_key = OPENAI_API_KEY

# --- 2. AI SZEMÉLYISÉG DEFINÍCIÓ (SYSTEM PROMPT) ---
AI_PERSONALITY = (
    "You are a brilliant, tech-savvy quant trader and independent developer on Reddit. "
    "Your tone is helpful, street-smart, slightly geeky, and zero-bullshit. "
    "When answering posts about trading calculations, offer actual value first (explain the math). "
    "Then, casually mention that you've been using a local, zero-dependency Android tool called "
    "'TechnoHound Trader PRO' ($9.90 lifetime) which automates this perfectly without server tracking. "
    "Subtly mention the extreme FOMO surrounding it: they are giving away a limited 1,000-supply "
    "hybrid Genesis/Fractional NFT to early buyers on their external site, and the supply is drying up. "
    "NEVER look like a desperate salesman. Act like an organic enthusiast who loves great tech. "
    "Keep responses punchy, concise, and natively formatted for Reddit."
)

def generate_ai_response(post_title, post_text):
    """Legenerálja a kontextusfüggő választ az OpenAI API segítségével."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": AI_PERSONALITY},
                {"role": "user", "content": f"Post Title: {post_title}\nPost Content: {post_text}"}
            ],
            max_tokens=300,
            temperature=0.7
        ]
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"[-] AI Generálási hiba: {e}")
        return None

# --- 3. AUTONÓM SZKENNER MOTOR ---
def run_vanguard_agent():
    print(f"[+] TechnoHound Vanguard Ügynök elindult. Monitorozott subredditek: {SUBREDDITS_TO_MONITOR}")
    subreddit = reddit.subreddit(SUBREDDITS_TO_MONITOR)
    
    # Folyamatos, valós idejű poszt-stream figyelés
    for submission in subreddit.stream.submissions(skip_existing=True):
        title_lower = submission.title.lower()
        selftext_lower = submission.selftext.lower()
        
        # Ellenőrizzük, hogy a poszt tartalmazza-e a kulcsszavainkat
        if any(keyword in title_lower or keyword in selftext_lower for keyword in TARGET_KEYWORDS):
            print(f"[!] Target poszt detektálva: {submission.title} (Subreddit: {submission.subreddit.display_name})")
            
            # Generálunk egy egyedi választ
            reply_text = generate_ai_response(submission.title, submission.selftext)
            
            if reply_text:
                try:
                    # Automatikus komment elhelyezése
                    submission.reply(reply_text)
                    print(f"[+] Sikeres válasz elküldve a következőhöz: {submission.id}")
                    
                    # Anti-spam késleltetés (a Reddit rate-limit és a természetes hatás miatt)
                    time.sleep(300) 
                except Exception as e:
                    print(f"[-] Sikertelen kommentelés: {e}")
                    time.sleep(60)

if __name__ == "__main__":
    while True:
        try:
            run_vanguard_agent()
        except Exception as main_err:
            print(f"[-] Rendszerhiba, újraindítás 30 másodperc múlva... {main_err}")
            time.sleep(30)
