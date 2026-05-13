# ==============================================================================
# FÁJL NÉV: 040_secure_session_token_generator.py
# SORSZÁM: 040
#
# LEÍRÁS ÉS FELADAT:
# Kriptográfiailag Biztonságos Munkamenet-Token Generáló (Secure Session Token) 
# modul. A 5TB-os hálózati pipeline és API hívások hitelesítéséhez készít 
# hamisíthatatlan, magas entrópiájú munkamenet-azonosítókat. A Python beépített 
# 'secrets' modulját használja, ami az operációs rendszer saját hardveres 
# véletlenszám-generátorából (CSPRNG) dolgozik, így a tokenek kiszámíthatatlanok.
# ==============================================================================

import secrets
import hashlib
import sys

class SecureSessionEngine:
    def __init__(self, token_length_bytes=32):
        self.token_bytes = token_length_bytes

    def generate_admin_session_token(self, node_id="NODE-BORSOD-01"):
        """Generál egy magas entrópiájú, kriptográfiailag biztonságos session tokent."""
        print("=========================================================")
        print(f"   CYBER-BORSOD AUTH -> SECURE CSPRNG TOKEN PIPELINE: {node_id}")
        print("=========================================================")
        
        # 1. Lépés: Biztonságos nyers bájtok generálása az operációs rendszer kerneléből
        raw_random_bytes = secrets.token_bytes(self.token_bytes)
        
        # 2. Lépés: URL-biztonságos Base64 karakterlánccá alakítás
        session_token = secrets.token_urlsafe(self.token_bytes)
        
        # 3. Lépés: Belső szerveroldali ellenőrző aláírás (Signature Hash) készítése
        token_signature = hashlib.sha256(raw_random_bytes).hexdigest()
        
        print(f"  [🟢 SUCCESS] Cryptographically secure random tokens generated.")
        print(f"    [-] Public Session Token : {session_token}")
        print(f"    [-] Server-Side Signature: {token_signature}")
        print("=========================================================")
        return session_token

if __name__ == "__main__":
    engine = SecureSessionEngine()
    engine.generate_admin_session_token()
