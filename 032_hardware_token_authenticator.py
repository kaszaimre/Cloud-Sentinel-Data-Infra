# ==============================================================================
# FÁJL NÉV: 032_hardware_token_authenticator.py
# SORSZÁM: 032
#
# LEÍRÁS ÉS FELADAT:
# Hardveres Token Alapú Hitelesítési (Hardware Token Authenticator) modul.
# Időalapú egyszeri jelszavak (TOTP) generálását és ellenőrzését szimulálja 
# a 5TB-os hálózati pipeline és a SOC központ védelmére. HMAC-SHA256 alapú 
# kriptográfiával biztosítja, hogy csak az léphessen be az infrastruktúrába, 
# aki rendelkezik a fizikai biztonsági kulccsal.
# ==============================================================================

import hmac
import hashlib
import time
import struct

class HardwareTokenAuthenticator:
    def __init__(self, shared_secret_key="BORSOD_SECRET_HARDWARE_KEY_XYZ"):
        """
        shared_secret_key: A hardveres token és a szerver között előre egyeztetett titkos kulcs.
        """
        self.secret = shared_secret_key.encode('utf-8')
        self.interval = 30  # A token 30 másodpercenként változik

    def general_aktualis_token(self):
        """Generál egy 6 jegyű biztonsági kódot az aktuális időbélyeg alapján."""
        # Megnézzük, hányadik 30 másodperces ablakban vagyunk az Unix epoch óta
        idogep = int(time.time() // self.interval)
        
        # Átalakítjuk a számlálót 8 bájtos bináris adattá
        msg = struct.pack(">Q", idogep)
        
        # HMAC-SHA256 hash előállítása a titkos kulccsal
        hmac_hash = hmac.new(self.secret, msg, hashlib.sha256).digest()
        
        # Dinamikus csonkolás (Dynamic Truncation) az utolsó bájtból vett eltolással
        offset = hmac_hash[-1] & 0x0F
        kod_resz = struct.unpack(">I", hmac_hash[offset:offset+4])[0] & 0x7FFFFFFF
        
        # 6 jegyűvé alakítjuk a kódot
        token = kod_resz % 1000000
        return f"{token:06d}"

    def verify_hardware_token(self, user_provided_token):
        """Validálja a felhasználó által beírt kódot."""
        helyes_token = self.general_aktualis_token()
        
        # Időalapú támadások elleni biztonságos string összehasonlítás (hmac.compare_digest)
        if hmac.compare_digest(helyes_token, str(user_provided_token)):
            print(f"  [🟢 AUTH SUCCESS] Hardware MFA token verified. Secure tunnel opened.")
            return True
        else:
            print(f"  [❌ AUTH FAILED] Invalid token signature. Access denied.")
            return False

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD SECURITY -> HARDWARE TOKEN AUTH ENGINE  ")
    print("=========================================================")
    
    auth_system = HardwareTokenAuthenticator()
    
    # 1. Lépés: Lekérjük az aktuális hardveres kódot
    current_mfa = auth_system.general_aktualis_token()
    print(f"[*] Physical Token Display showing: {current_mfa}")
    print("-" * 57)
    
    # 2. Lépés: Belépési tesztek szimulációja
    print("[!] Attempting login with incorrect token...")
    auth_system.verify_hardware_token("111111")
    
    print("\n[!] Attempting login with correct hardware token...")
    auth_system.verify_hardware_token(current_mfa)
    print("=========================================================")
