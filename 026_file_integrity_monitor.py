# ==============================================================================
# FÁJL NÉV: 026_file_integrity_monitor.py
# SORSZÁM: 026
#
# LEÍRÁS ÉS FELADAT:
# Fájlintegritás-ellenőrző (FIM) modul. SHA-256 kriptográfiai hash-ek segítségével
# figyeli a kijelölt biztonsági könyvtárakat és konfigurációs fájlokat. 
# Automatikusan detektálja és naplózza, ha egy illetéktelen támadó módosította 
# a rendszer belső szkriptjeit.
# ==============================================================================

import hashlib
import os

def kiszamol_file_hash(fajl_utvonal):
    """Kiszámolja a megadott fájl SHA-256 ellenőrzőösszegét."""
    hasher = hashlib.sha256()
    try:
        with open(fajl_utvonal, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD MONITORING -> FILE INTEGRITY ENGINE     ")
    print("=========================================================")
    
    # Teszt környezet: Figyelni kívánt kritikus konfigurációs fájl szimulálása
    teszt_fajl = "system_config_baseline.tmp"
    
    # Létrehozunk egy alapfájlt a teszthez
    with open(teszt_fajl, "w") as f:
        f.write("allow_root_login=false\nfirewall_active=true")
        
    # 1. Lépés: Lementjük az eredeti biztonságos állapot hash értékét (Baseline)
    eredeti_hash = kiszamol_file_hash(teszt_fajl)
    print(f"[*] Baseline SHA-256 registered: {eredeti_hash}")
    print("-" * 57)
    
    # 2. Lépés: Szimulálunk egy illetéktelen módosítást (Támadás)
    print("[!] Modifying file signature (simulating unauthorized modification)...")
    with open(teszt_fajl, "w") as f:
        f.write("allow_root_login=true\nfirewall_active=false")
        
    # 3. Lépés: Újra ellenőrizzük a fájlt, és összehasonlítjuk a hash-eket
    aktualis_hash = kiszamol_file_hash(teszt_fajl)
    
    if eredeti_hash != aktualis_hash:
        print(f"\n[🚨 SECURITY ALERT] File integrity VIOLATED!")
        print(f"  [-] Expected: {eredeti_hash}")
        print(f"  [!] Detected: {aktualis_hash}")
    else:
        print("\n[🟢 COMPLIANT] File integrity verified. No modifications detected.")
        
    # Takarítás a teszt után
    if os.path.exists(teszt_fajl):
        os.remove(teszt_fajl)
        
    print("=========================================================")
