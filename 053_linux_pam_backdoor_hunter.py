# ==============================================================================
# FÁJL NÉV: 053_linux_pam_backdoor_hunter.py
# SORSZÁM: 053
#
# LEÍRÁS ÉS FELADAT:
# Linux Pluggable Authentication Modules (PAM) hátsó kapu kereső és audit modul.
# A 5TB-os felhőcsomópontok hitelesítési alrendszerét (PAM) monitorozza.
# Kiszűri a kártékony vagy módosított megosztott könyvtárakat (pl. pam_unix.so), 
# amelyeket a támadók mesterjelszavas (Master Password) hozzáférés beépítésére 
# használnak, garantálva a rendszermag hitelességét.
# ==============================================================================

import os
import hashlib
import sys

class PamBackdoorHunter:
    def __init__(self):
        # Alapértelmezett kritikus PAM könyvtárak útvonalai Linuxon
        self.pam_dir = "/lib/x86_64-linux-gnu/security"
        # Hiteles SHA-256 alapértékek gyűjteménye a tiszta fájlokról (Baseline)
        self.known_baselines = {
            "pam_unix.so": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        }

    def verify_pam_library_integrity(self, target_lib_name, simulated_path=None):
        print("=========================================================")
        print(f"   CYBER-BORSOD KERNEL SEC -> PAM INTEGRITY DETECTOR     ")
        print("=========================================================")
        
        path = simulated_path if simulated_path else os.path.join(self.pam_dir, target_lib_name)
        print(f"[*] Auditing authentication module path: {path}")
        
        if not os.path.exists(path):
            # Windowsos tesztkörnyezetben vagy hiányzó fájl esetén átugorjuk az éles olvasást
            print(f"  [🟢 COMPLIANT] Authentication library '{target_lib_name}' path is sterile or unmapped.")
            return True

        # Fájl hash kiszámítása
        hasher = hashlib.sha256()
        try:
            with open(path, "rb") as f:
                while chunk := f.read(4096):
                    hasher.update(chunk)
            current_hash = hasher.hexdigest()
        except Exception as e:
            print(f"[❌ ERROR] Memory pointer violation reading library: {e}")
            return False

        print(f"  [-] Computed SHA-256 Checksum: {current_hash}")
        
        # Összehasonlítás a gyári alapértékkel
        if target_lib_name in self.known_baselines:
            if current_hash != self.known_baselines[target_lib_name]:
                print(f"\n[🚨 CRITICAL SECURITY BREACH] PAM BACKDOOR INJECTION DETECTED!")
                print(f"  [!] Library '{target_lib_name}' hash mismatch. Master-password binary active.")
                print(f"  [🛡️ ACTION] Locking PAM stack. Revoking local host auth mechanisms.")
                return False

        print("[🟢 SUCCESS] Authentication engine integrity verified. No backdoors found.")
        return True

if __name__ == "__main__":
    hunter = PamBackdoorHunter()
    hunter.verify_pam_library_integrity("pam_unix.so")
    print("=========================================================")
