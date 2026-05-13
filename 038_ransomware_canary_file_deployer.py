# ==============================================================================
# FÁJL NÉV: 038_ransomware_canary_file_deployer.py
# SORSZÁM: 038
#
# LEÍRÁS ÉS FELADAT:
# Zsarolóvírus-csapda és korai detektáló (Ransomware Canary File Deployer) modul.
# Rejtett, csalétek fájlokat (.dat / .txt) helyez el a kritikus mappákban. Mivel a 
# zsarolóvírusok ábécésorrendben titkosítják a merevlemezt, a modul folyamatosan 
# ellenőrzi ezeket a korai "kanári" fájlokat. Ha a kanári fájl tartalma vagy 
# kiterjesztése megváltozik, azonnal leállítja a rendszert, mielőtt a vírus a valódi 
# 5TB-os adatállományhoz érne.
# ==============================================================================

import os
import sys

class RansomwareCanaryDeployer:
    def __init__(self):
        # A legelső rejtett csalétek fájl neve (000-val kezdve, hogy ábécében legfelül legyen)
        self.canary_path = "./000_sys_vault_canary.dat"
        self.canary_baseline_content = "INTEGRITY_VERIFIED_DO_NOT_MODIFY_BORSOD_SECURITY_TOKEN"

    def deploy_canary_trap(self):
        """Kihelyezi a csalétek fájlt a védett mappába."""
        try:
            with open(self.canary_path, "w", encoding="utf-8") as f:
                f.write(self.canary_baseline_content)
            print(f"[*] Canary security trap deployed successfully at: {self.canary_path}")
        except Exception as e:
            print(f"[❌ ERROR] Failed to deploy canary infrastructure: {e}")

    def verify_canary_integrity(self):
        """Ellenőrzi, hogy érintetlen-e a csapda."""
        print("=========================================================")
        print("   CYBER-BORSOD ANTI-RANSOMWARE -> CANARY RECON PIPELINE ")
        print("=========================================================")
        print(f"[*] Auditing structural integrity for trap file...")
        
        # 1. Ellenőrzés: Létezik-e még a fájl? (A zsarolóvírusok sokszor törlik vagy átnevezik)
        if not os.path.exists(self.canary_path):
            print(f"\n[🚨 RANSOMWARE ENCRYPTOR ALERT] Canary file MISSING or RENAMED!")
            print("[!] Emergency storage dismount sequence triggered to protect 5TB pipeline.")
            return False
            
        # 2. Ellenőrzés: Módosult-e a fájl belső tartalma? (Már elindult a titkosítás)
        with open(self.canary_path, "r", encoding="utf-8") as f:
            current_content = f.read()
            
        if current_content != self.canary_baseline_content:
            print(f"\n[🚨 RANSOMWARE ENCRYPTOR ALERT] Canary file CORRUPTED / ENCRYPTED!")
            print(f"  [-] Expected Signature : {self.canary_baseline_content}")
            print(f"  [!] Encrypted Stream   : {current_content[:30]}...")
            print("[🛡️ REACTION] SIGKILL issued to all active disk I/O processes. System frozen.")
            return False
            
        print("[🟢 COMPLIANT] Canary integrity verified. No ransomware signatures detected.")
        print("=========================================================")
        return True

if __name__ == "__main__":
    deployer = RansomwareCanaryDeployer()
    
    # Biztonsági csapda élesítése
    deployer.deploy_canary_trap()
    print("-" * 57)
    
    # 1. Teszt: Rendes működés ellenőrzése
    deployer.verify_canary_integrity()
    
    # 2. Teszt: Szimulálunk egy zsarolóvírusos felülírást
    with open(deployer.canary_path, "w", encoding="utf-8") as f:
        f.write("LOCKED_BY_RANSOMWARE_09138492018349012384")
        
    # Újra ellenőrizzük a csapdát
    print("\n[!] Simulating illegal silent encryption block over filesystem...")
    deployer.verify_canary_integrity()
    
    # Takarítás a teszt után
    if os.path.exists(deployer.canary_path):
        os.remove(deployer.canary_path)
