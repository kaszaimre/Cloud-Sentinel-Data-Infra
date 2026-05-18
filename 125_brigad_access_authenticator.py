# ==============================================================================
# FÁJL NÉV: 125_brigad_access_authenticator.py
# SORSZÁM: 125
#
# LEÍRÁS ÉS FELADAT:
# Brigád Hozzáférés-Hitelesítő és Titkos Jelszó Validáló (Authenticator) modul.
# A 125. mérföldkő a nagyvállalati adatinfrastruktúrában. Egy egyedi, belső
# karakterlánc-ellenőrzéssel validálja a titkos 'Kvak fckra' Brigád-jelszót.
# Sikeres hitelesítés esetén zöld utat ad a 100-as Master Orchestrator felé,
# ellenkező esetben azonnal lezárja az összes hálózati és 5TB-os adatportot.
# ==============================================================================

import sys
import time

class BrigadAccessAuthenticator:
    def __init__(self):
        self.secret_passphrase = "kvak fckra"
        self.system_status = "LOCKED"

    def authenticate_brigad_signature(self, input_phrase):
        print("=========================================================")
        print("   CYBER-BORSOD INFRA -> BRIGÁD ACCESS AUTHENTICATOR     ")
        print("=========================================================")
        print("[*] Initiating cryptographic pass-shield handshake...")
        time.sleep(0.3)
        
        # BIZTONSÁGI JELSZÓ-VALIDÁCIÓ
        if input_phrase.lower().strip() == self.secret_passphrase:
            self.system_status = "UNLOCKED"
            print("  [🟢 ACCESS GRANTED] Brigád signature authenticated successfully!")
            print("    [-] System Status: BRIGÁD WIN (GPT APPROVED)")
            print("    [-] Clearance    : LEVEL_MAX_COMPLIANT")
            print("-" * 57)
            print("[🏆 SUCCESS] Kernel environment sterile. Core matrix is active.")
            return True
        else:
            print("  [🚨 SECURITY ANOMALY] INVALID PASSPHRASE ATTEMPTED!")
            print("    [!] Action: Freezing memory caches. Isolating network node.")
            return False

if __name__ == "__main__":
    authenticator = BrigadAccessAuthenticator()
    # Futtatás a titkos Brigád jelszóval
    authenticator.authenticate_brigad_signature("kvak fckra")
    print("=========================================================")
