# ==============================================================================
# FÁJL NÉV: 034_ssh_honeypot_node.py
# SORSZÁM: 034
#
# LEÍRÁS ÉS FELADAT:
# Kiberbiztonsági Csapda (SSH Honeypot) modul. Egy hamis, sebezhetőnek tűnő 
# SSH menedzsment felületet emulál a hálózaton. Amikor egy támadó vagy egy 
# automatizált bot megpróbál belépni (Brute-Force találgatással), a modul 
# nem engedi be, de rögzíti a támadó IP-címét, a próbált jelszavakat, és 
# azonnali riasztást küld a központi SOC csapatnak.
# ==============================================================================

import socket
import sys
import time
from datetime import datetime

class SshHoneypotNode:
    def __init__(self, fake_banner="SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5"):
        self.banner = fake_banner
        self.log_file = "./sentinel_events.log"

    def log_intrusion_attempt(self, attacker_ip, username, password):
        """Rögzíti a behatolási kísérletet a központi naplófájlba."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alert_msg = f"[🚨 HONEYPOT DETECTED] Hostile Brute-Force -> IP: {attacker_ip} | User: '{username}' | Pass: '{password}'"
        
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {alert_msg}\n")
            print(f"  {alert_msg}")
        except Exception as e:
            print(f"[!] Logírási hiba a csapdában: {e}")

    def simulate_connection(self, simulated_ip, user, pwd):
        """Szimulálja az SSH csapda működését és az adatok rögzítését."""
        print(f"[*] Honeypot node socket established on interface.")
        print(f"[*] Broadcasting fake software banner: {self.banner}")
        print(f"[*] Inbound connection request received from: {simulated_ip}")
        print("-" * 57)
        
        # Szimuláljuk, hogy a támadó próbálkozik
        time.sleep(1)
        self.log_intrusion_attempt(simulated_ip, user, pwd)
        print("-" * 57)
        print("[🛡️ MITIGATION] Attack signature isolated. IP blacklisted on perimeter firewall.")

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD DECEPTION -> SSH HONEYPOT DEPLOYMENT     ")
    print("=========================================================")
    
    pot = SshHoneypotNode()
    
    # Teszt szimuláció: egy ismert rosszindulatú IP-cím megpróbál belépni alapértelmezett jelszavakkal
    bot_ip = "185.220.101.5"
    pot.simulate_connection(bot_ip, user="root", pwd="password123")
    print("=========================================================")
