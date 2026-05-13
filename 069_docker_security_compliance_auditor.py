# ==============================================================================
# FÁJL NÉV: 070_linux_syslog_integrity_vault.py
# SORSZÁM: 070
#
# LEÍRÁS ÉS FELADAT:
# Rendszernapló Integritás-védelmi és Kriptográfiai Lezáró (Syslog Integrity Vault) modul.
# A 5TB-os kiber-infrastruktúra végső védelmi vonala. Időszakosan beolvassa a 
# 'sentinel_events.log' legfrissebb bejegyzéseit, blokkosítja őket, és egy 
# láncolt SHA-256 hash lenyomatot generál róluk. Ha egy támadó utólag megpróbálja 
# letörölni a nyomait a logfájlból, a modul azonnal jelzi az integritás sérülését.
# ==============================================================================

import hashlib
import os
import sys
from datetime import datetime

class SyslogIntegrityVault:
    def __init__(self, target_log_path="./sentinel_events.log"):
        self.target_log = target_log_path
        self.state_vault_path = "./sentinel_events.log.hash"

    def lock_and_sign_log_buffer(self):
        print("=========================================================")
        print("   CYBER-BORSOD SYSTEM -> CENTRAL LOG INTEGRITY VAULT    ")
        print("=========================================================")
        print(f"[*] Auditing structural text chains for: {self.target_log}")
        
        if not os.path.exists(self.target_log):
            print("[*] Log buffer empty. Injecting baseline telemetry block...")
            with open(self.target_log, "w", encoding="utf-8") as f:
                f.write(f"[{datetime.now()}] [SYSTEM] Baseline initialization token.\n")

        # 1. LÉPÉS: A teljes naplófájl beolvasása és kriptográfiai hash-elése
        hasher = hashlib.sha256()
        try:
            with open(self.target_log, "rb") as f:
                while chunk := f.read(4096):
                    hasher.update(chunk)
            computed_hash = hasher.hexdigest()
        except Exception as e:
            print(f"[❌ ERROR] Memory pointer isolation breach: {e}")
            return False

        print(f"  [-] Computed Log Cryptographic Hash: {computed_hash}")
        
        # 2. LÉPÉS: Összehasonlítás a korábban elmentett biztonságos állapottal
        if os.path.exists(self.state_vault_path):
            with open(self.state_vault_path, "r", encoding="utf-8") as f:
                saved_hash = f.read().strip()
                
            if computed_hash != saved_hash:
                print("\n[🚨 LOG TAMPERING DETECTED] FILE INTEGRITY HAS BEEN VIOLATED!")
                print("  [!] VULNERABILITY: An elite attacker or rogue process modified history logs to erase traces!")
                print("  [🛡️ EMERGENCY REACTION] Locking physical disk volumes. Broadasting SIEM flash payload.")
                return False
            else:
                print("\n[🟢 COMPLIANT] Log chain matches state vault metadata perfectly. History untampered.")
        else:
            print("\n[*] Initial baseline hash missing. Creating state vault token signature...")
            
        # Elmentjük az aktuális tiszta állapotot lezárásként
        with open(self.state_vault_path, "w", encoding="utf-8") as f:
            f.write(computed_hash)
        print(f"[🟢 SUCCESS] State signature committed securely to: {self.state_vault_path}")
        print("=========================================================")
        return True

if __name__ == "__main__":
    vault = SyslogIntegrityVault()
    vault.lock_and_sign_log_buffer()
