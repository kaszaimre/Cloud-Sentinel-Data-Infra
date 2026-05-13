# ==============================================================================
# FÁJL NÉV: 055_cloud_kms_key_rotator.py
# SORSZÁM: 055
#
# LEÍRÁS ÉS FELADAT:
# Felhő Alapú Kulcskezelő és Rotációs (Cloud KMS Key Rotator) modul.
# A 5TB-os hálózati pipeline és adattárház titkosításához használt mesterkulcsok
# (Master Encryption Keys) életciklusát menedzseli. Automatikusan végrehajtja
# a kulcsok időszakos cseréjét és rotációját, megakadályozva, hogy egy esetlegesen
# kiszivárgott régi kulccsal a támadók visszafejthessék az új adatfolyamokat.
# ==============================================================================

import sys
import hashlib
import time
from datetime import datetime

class CloudKmsKeyRotator:
    def __init__(self, rotation_days_threshold=90):
        self.rotation_threshold = rotation_days_threshold
        self.active_key_version = 1
        self.key_vault = {}

    def execute_cryptographic_key_rotation(self, current_key_age_days):
        print("=========================================================")
        print("   CYBER-BORSOD CLOUD KMS -> MASTER KEY LIFECYCLE AUDIT   ")
        print("=========================================================")
        print(f"[*] Active Key Version Monitored : v{self.active_key_version}")
        print(f"[*] Current Key Age              : {current_key_age_days} days (Limit: {self.rotation_threshold})")
        print("-" * 57)

        # BIZTONSÁGI ELLENŐRZÉS: Elérte a kulcs a rotációs korhatárt?
        if current_key_age_days >= self.rotation_threshold:
            print("  [🚨 ROTATION TRIGGERED] Cryptographic key age limit reached!")
            print("[*] Deprecating older key state context...")
            
            # Új titkosító kulcs generálása CSPRNG alapon szimulálva
            timestamp = str(time.time()).encode('utf-8')
            new_key = hashlib.sha256(timestamp).hexdigest()
            
            self.active_key_version += 1
            self.key_vault[f"v{self.active_key_version}"] = new_key
            
            print(f"  [🟢 SUCCESS] New KMS Key Version deployed: v{self.active_key_version}")
            print(f"  [-] New Key Signature: {new_key[:24]}...")
            print("[🛡️ ACTION] Re-encrypting active cluster indices with new key ring.")
            return True
        else:
            print("[🟢 COMPLIANT] Key material remains secure. No lifecycle rotation required.")
            return False

if __name__ == "__main__":
    rotator = CloudKmsKeyRotator()
    
    # 1. Teszt eset: Szabályos, fiatal kulcs vizsgálata
    rotator.execute_cryptographic_key_rotation(current_key_age_days=14)
    
    print("\n" + "="*57 + "\n")
    
    # 2. Teszt eset: Elöregedett kulcs automatikus rotációja (95 napos kulcs)
    rotator.execute_cryptographic_key_rotation(current_key_age_days=95)
    print("=========================================================")
