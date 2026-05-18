cat << 'EOF' > cyber_sentinel.py
import os
import sys
import time
import subprocess
import signal
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# --- KÖZPONTI INFRASTRUKTÚRA BEÁLLÍTÁSOK ---
MAX_CPU_LIMIT = 85.0
MALICIOUS_SIGNATURES = ["xmrig", "cryptonight", "reverse_shell", "cmd.exe /c"]

# A logfájl közvetlenül a jelenlegi mappába kerül
LOG_FILE_PATH = "./sentinel_events.log"

SMTP_SERVER = "gmail.com"
SMTP_PORT = 587
KULDO_EMAIL = "a_te_google_emailed@gmail.com"
ALKALMAZAS_JELSZO = "xxxx xxxx xxxx xxxx"  # Google App Password 🔒
FOGADO_EMAIL = "don_mernok_the_brain@gmail.com"

def log_event(message):
    """Események beírása a helyi biztonsági logfájlba."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_FILE_PATH, "a") as f:
            f.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"[!] Logírási hiba: {e}")

def riaszto_email_kuldes(pid, cpu, parancs, indok):
    msg = MIMEMultipart()
    msg['From'] = KULDO_EMAIL
    msg['To'] = FOGADO_EMAIL
    msg['Subject'] = f"🚨 [SEC-ALERT] Incidens észlelve - PID: {pid}"

    body = f"""
=================================================================
   INFRASTRUCTURE SECURITY INCIDENT REPORT – ALERT PIPELINE
=================================================================
Időpont: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Szervercsomópont: Windows-Sandbox-PC
-----------------------------------------------------------------
[!] ANOMÁLIA DETEKTÁLVA ÉS ELHÁRÍTVA!
Kiváltó ok: {indok}

Folyamat részletei:
  - PID: {pid}
  - Futtatott parancs/Image: {parancs}

[🛡️ REAKCIÓ]: A védelmi motor a folyamatot lezárta.
A hálózati biztonsági log frissítve.
=================================================================
    """
    msg.attach(MIMEText(body, 'plain'))
    try:
        szerver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        szerver.starttls()
        szerver.login(KULDO_EMAIL, ALKALMAZAS_JELSZO)
        szerver.sendmail(KULDO_EMAIL, FOGADO_EMAIL, msg.as_string())
        szerver.quit()
        print(f"  [🟢 ALERT SENT] Riasztás elküldve.")
    except Exception as e:
        print(f"  [❌ SMTP ERROR] Sikertelen küldés: {e}")

def folyamat_ellenorzes():
    try:
        # JAVÍTVA: Windows tasklist parancs használata a Linux ps helyett
        nyers_adat = subprocess.check_output(["tasklist", "/FO", "CSV", "/NH"], stderr=subprocess.DEVNULL).decode("cp1250", errors="ignore")
        sorok = nyers_adat.strip().split("\n")
        
        for sor in sorok:
            if not sor: continue
            # A tasklist CSV kimenete: "Image Name","PID","Session Name","Session#","Mem Usage"
            elemek = [e.strip('"') for e in sor.split(',')]
            if len(elemek) < 2: continue
                
            process_name = elemek[0]
            try:
                pid = int(elemek[1])
            except ValueError: continue

            if pid == os.getpid(): continue

            incidens = False
            indok = ""

            # Ellenőrzés gyanús folyamatnevekre
            for kifejezes in MALICIOUS_SIGNATURES:
                if kifejezes in process_name.lower():
                    incidens = True
                    indok = f"Feketelistás folyamat: '{process_name}'"

            if incidens:
                try:
                    # Windowsos folyamatleállítás taskkill segítségével
                    subprocess.call(["taskkill", "/F", "/PID", str(pid)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    alert_msg = f"TASKKILL /F élesítve -> PID: {pid} | Név: {process_name} | Ok: {indok}"
                    log_event(alert_msg)
                    riaszto_email_kuldes(pid, 0, process_name, indok)
                except Exception: pass
    except Exception: pass

if __name__ == "__main__":
    log_event("SYSTEM_START: A védelmi Sentinel motor elindult Windows környezetben.")
    while True:
        folyamat_ellenorzes()
        time.sleep(5)
EOF
