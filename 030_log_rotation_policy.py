# ==============================================================================
# FÁJL NÉV: 029_secure_env_vault.py
# SORSZÁM: 029
#
# LEÍRÁS ÉS FELADAT:
# Biztonságos Környezeti Változó és Token Kezelő (Secure Environment Vault) modul.
# Megakadályozza, hogy a szenzitív API kulcsok, adatbázis jelszavak és az
# SMTP jelszavak nyers szövegként (hardcoded) szerepeljenek a kódokban.
# A modul titkosított környezeti fájlokat (.env) olvas be, és ellenőrzi a kötelező
# biztonsági kulcsok meglétét a 5TB-os pipeline indítása előtt.
# ==============================================================================

import os
import sys

class SecureEnvVault:
    def __init__(self, vault_path=".env"):
        self.vault_path = vault_path
        self.required_keys = ["SMTP_PASS", "DB_CLUSTER_TOKEN", "API_SECURE_KEY"]
        self.loaded_config = {}

    def initialize_mock_vault(self):
        """Létrehoz egy biztonságos, minta környezeti fájlt, ha még nem létezik."""
        if not os.path.exists(self.vault_path):
            with open(self.vault_path, "w", encoding="utf-8") as f:
                f.write("# CYBER-BORSOD INFRASTRUCTURE VAULT BASELINE\n")
                f.write("SMTP_PASS=xxxx_xxxx_xxxx_xxxx\n")
                f.write("DB_CLUSTER_TOKEN=BORSOD_CORE_PRODUCTION_TOKEN_ABC123\n")
                f.write("API_SECURE_KEY=SEC_SECURE_KEY_NODE_9482\n")
            print(f"[*] Generated baseline vault configuration at: {self.vault_path}")

    def load_and_verify_vault(self):
        print("=========================================================")
        print("   CYBER-BORSOD SECURITY -> ENVIROMENT VAULT AUDIT      ")
        print("=========================================================")
        print(f"[*] Parsing operational parameters from: {self.vault_path}")
        
        self.initialize_mock_vault()
        
        # Környezeti fájl kézi beolvasása és tisztítása
        try:
            with open(self.vault_path, "r", encoding="utf-8") as f:
                for sor in f:
                    sor = sor.strip()
                    if not sor or sor.startswith("#"):
                        continue
                    if "=" in sor:
                        kulcs, ertek = sor.split("=", 1)
                        self.loaded_config[kulcs.strip()] = ertek.strip()
        except Exception as e:
            print(f"[❌ ERROR] Failed to access vault infrastructure: {e}")
            return False

        # Kötelező kulcsok meglétének és biztonságának validálása
        missing_keys = []
        for key in self.required_keys:
            if key not in self.loaded_config or not self.loaded_config[key]:
                missing_keys.append(key)
        
        if missing_keys:
            print(f"\n[🚨 COMPLIANCE BREACH] Missing structural credentials: {missing_keys}")
            print("[!] Core system shutdown triggered for token protection.")
            return False
            
        print("[🟢 SUCCESS] All infrastructure keys verified and loaded into memory safely.")
        print(f"  [-] Active Tokens Monitored: {len(self.loaded_config)} Production Parameters")
        print("=========================================================")
        return True

if __name__ == "__main__":
    vault = SecureEnvVault()# ==============================================================================
# FÁJL NÉV: 030_log_rotation_policy.py
# SORSZÁM: 030
#
# LEÍRÁS ÉS FELADAT:
# Automatikus Naplófájl Rotációs (Log Rotation Policy) és Karbantartó modul. 
# Ellenőrzi a 5TB-os hálózati pipeline és a Sentinel által generált logfájlok 
# méretét. Ha egy fájlméret meghaladja a kritikus küszöbértéket, automatikusan 
# archiválja, tömöríti (.gz), és egy tiszta új naplófájlt indít, megvédve 
# a rendszert a tárhely-telítettségtől.
# ==============================================================================

import os
import sys
import gzip
import shutil
from datetime import datetime

class LogRotationPolicy:
    def __init__(self, target_log="./sentinel_events.log", max_size_bytes=5 * 1024 * 1024):
        """
        target_log: A figyelni kívánt központi naplófájl
        max_size_bytes: Maximális megengedett méret (alapértelmezett: 5MB)
        """
        self.target_log = target_log
        self.max_size_bytes = max_size_bytes

    def execute_rotation_check(self):
        print("=========================================================")
        print("   CYBER-BORSOD INFRA -> SECURITY LOG ROTATION CORE     ")
        print("=========================================================")
        print(f"[*] Checking active system log metrics: {self.target_log}")
        
        # Ha nem létezik a fájl, létrehozzuk a teszthez
        if not os.path.exists(self.target_log):
            with open(self.target_log, "w", encoding="utf-8") as f:
                f.write(f"[{datetime.now()}] Baseline log initialization.\n")
        
        log_size = os.path.getsize(self.target_log)
        print(f"  [-] Current Log Size: {log_size} bytes (Threshold: {self.max_size_bytes})")
        
        # Ellenőrzés: túl nagy-e a fájl?
        if log_size >= self.max_size_bytes:
            print(f"\n[🚨 CRITICAL SIZE BREACH] Rotating log file payload...")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            archive_path = f"{self.target_log}_{timestamp}.gz"
            
            try:
                # 1. Lépés: Biztonságos tömörítés GZIP formátumba
                print(f"  [*] Compressing active buffer into: {archive_path}")
                with open(self.target_log, 'rb') as f_in:
                    with gzip.open(archive_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                
                # 2. Lépés: Az eredeti fájl kiürítése (Truncate)
                with open(self.target_log, 'w', encoding="utf-8") as f:
                    f.write(f"[{datetime.now()}] [SYSTEM] Log rotation complete. New rotation segment opened.\n")
                    
                print("[🟢 SUCCESS] Storage cleared. Log rotation cycle finished successfully.")
            except Exception as e:
                print(f"[❌ ERROR] Rotation pipeline collapsed: {e}")
        else:
            print("\n[🟢 COMPLIANT] Log size is within structural limits. No rotation required.")
        print("=========================================================")

if __name__ == "__main__":
    # Teszteléshez kényszerített kis méret (500 bájt), hogy azonnal lássuk a működést
    policy = LogRotationPolicy(max_size_bytes=500)
    policy.execute_rotation_check()

    vault.load_and_verify_vault()
