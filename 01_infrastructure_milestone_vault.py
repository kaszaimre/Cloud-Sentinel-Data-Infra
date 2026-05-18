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
ALLOWED_SYSTEM_USERS = ["root", "ubuntu", "cloud_admin", "service_worker"]
MALICIOUS_SIGNATURES = ["xmrig", "cryptonight", "reverse_shell", "/bin/bash -i"]

# Logfájl abszolút elérési útja a frissen létrehozott mappádban
LOG_FILE_PATH = "./cyber_borsod_core/security/sentinel_events.log"

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

def riaszto_email_kuldes(pid, felhasznalo, cpu, parancs, indok):
    msg = MIMEMultipart()
    msg['From'] = KULDO_EMAIL
    msg['To'] = FOGADO_EMAIL
    msg['Subject'] = f"🚨 [SEC-ALERT] Incidens észlelve - PID: {pid}"

    body = f"""
=================================================================
   INFRASTRUCTURE SECURITY INCIDENT REPORT – ALERT PIPELINE
=================================================================
Időpont: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Szervercsomópont: Local-Sandbox-VM (5TB Storage Ready)
-----------------------------------------------------------------
[!] ANOMÁLIA DETEKTÁLVA ÉS ELHÁRÍTVA!
Kiváltó ok: {indok}

Folyamat részletei:
  - PID: {pid} | Felhasználó: {felhasznalo} | CPU Terhelés: {cpu}%
  - Futtatott parancs: {parancs}

[🛡️ REAKCIÓ]: A védelmi motor a folyamatot SIGKILL (-9) paranccsal lezárta.
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
        nyers_adat = subprocess.check_output(["ps", "-eo", "user,pid,pcpu,pmem,args"]).decode("utf-8")
        sorok = nyers_adat.strip().split("\n")[1:]
        
        for sor in sorok:
            elemek = sor.split(None, 4)
            if len(elemek) < 5: continue
                
            felhasznalo, pid, cpu, mem, parancs = elemek
            try:
                pid = int(pid)
                cpu_hasznalat = float(cpu)
            except ValueError: continue

            if pid == os.getpid(): continue

            incidens = False
            indok = ""

            if cpu_hasznalat > MAX_CPU_LIMIT:
                incidens = True
                indok = f"Magas CPU: {cpu_hasznalat}%"

            for kifejezes in MALICIOUS_SIGNATURES:
                if kifejezes in parancs.lower():
                    incidens = True
                    indok = f"Feketelistás kulcsszó: '{kifejezes}'"

            if incidens:
                try:
                    os.kill(pid, signal.SIGKILL)
                    alert_msg = f"KILL -9 élesítve -> PID: {pid} | Felhasználó: {felhasznalo} | Ok: {indok}"
                    print(f"  [🟢 MITIGATED] {alert_msg}")
                    log_event(alert_msg)  # Beírás a helyi logba
                    riaszto_email_kuldes(pid, felhasznalo, cpu_hasznalat, parancs, indok)
                except Exception: pass
    except Exception: pass

if __name__ == "__main__":
    print("[*] Cloud Sentinel daemon elindult a 'cyber_borsod_core' mappában...")
    log_event("SYSTEM_START: A védelmi Sentinel motor elindult.")
    while True:
        folyamat_ellenorzes()
        time.sleep(5)
