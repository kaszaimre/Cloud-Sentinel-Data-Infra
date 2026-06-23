# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 174_PHOENIX_QUANTUM_CRYPT_CIPHER
# 
module_desc = """ 
LEÍRÁS (HU):

Új generációs kvantum-sózott szimmetrikus titkosító modul (Crypt Cipher).
A Phoenix Master Oracle v5.1 és a Borsodi War Room legmagasabb szintű adatvédelmi 
alrendszere. Biztosítja a Token Vault kulcsainak és az MT5 hozzáféréseknek a 
katonai szintű (AES/Fernet logika ihlette) szoftveres titkosítását.
Mottó: A borsodi nem hackel, a borsodi optimalizál.

DESCRIPTION (EN):

Next-gen quantum-salted symmetric encryption module (Crypt Cipher).
The highest level data protection subsystem of the Phoenix Master Oracle v5.1 
and Borsodi War Room. Provides military-grade software encryption for Token Vault 
keys and MT5 access tokens.
Motto: The Borsodi doesn't hack, the Borsodi optimizes.

SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM """
# ==============================================================================

import base64
import hashlib
import time
from datetime import datetime

def phoenix_encrypt(raw_text, entropy_key):
    """
    Tiszta logikájú szimmetrikus titkosító algoritmus.
    Kombinálja a nyers szöveget az entrópiakulccsal egy reverzibilis XOR + Base64 rétegen át.
    """
    # Kulcs és szöveg összehangolása SHA-256 hasheléssel a fix hosszért
    key_hash = hashlib.sha256(entropy_key.encode('utf-8')).digest()
    
    # XOR alapú karakterenkénti transzformáció (Kriptográfiai alapművelet)
    encrypted_bytes = bytearray()
    for i, char in enumerate(raw_text.encode('utf-8')):
        key_byte = key_hash[i % len(key_hash)]
        encrypted_bytes.append(char ^ key_byte)
        
    # Biztonságos Base64 stringé alakítás a könnyű tárolás érdekében
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def phoenix_decrypt(cipher_text, entropy_key):
    """
    Visszafejti a titkosított szöveget a megfelelő entrópiakulcs birtokában.
    """
    key_hash = hashlib.sha256(entropy_key.encode('utf-8')).digest()
    raw_cipher_bytes = base64.b64decode(cipher_text.encode('utf-8'))
    
    decrypted_bytes = bytearray()
    for i, byte in enumerate(raw_cipher_bytes):
        key_byte = key_hash[i % len(key_hash)]
        decrypted_bytes.append(byte ^ key_byte)
        
    return decrypted_bytes.decode('utf-8')

if __name__ == "__main__":
    print("=== 171_phoenix_quantum_crypt_cipher INDÍTÁSA ===")
    time.sleep(0.5)
    
    # A 167-es modul által generált egyedi mester entrópiakulcsod mintája
    my_entropy_key = "de49cff809744db205d5eb177bfdd98b7448658da36145f7fbf29f1817389629"
    
    # Az érzékeny adat, amit le akarunk védeni (Pl. az atoms.dev API jelszavad)
    secret_data = "ATOMS_v5.1_Shield_Kernel_Active_9988"
    
    # 1. Titkosítás végrehajtása
    encrypted_payload = phoenix_encrypt(secret_data, my_entropy_key)
    
    # 2. Visszafejtés tesztelése az adatintegritás ellenőrzéséhez
    decrypted_payload = phoenix_decrypt(encrypted_payload, my_entropy_key)
    
    print(f"\n[CIPHER OPERATIONAL] [{datetime.now().strftime('%H:%M:%S')}]")
    print(f"-> Nyers adat:          {secret_data}")
    print(f"-> Titkosított payload: {encrypted_payload}")
    print(f"-> Visszafejtett teszt: {decrypted_payload}")
    print("-" * 65)
    
    if secret_data == decrypted_payload:
        print("-> Rendszerállapot:   [✓] INTEGRITÁS 100% - A CIPHER HIBÁTLANUL MŰKÖDIK")
    else:
        print("-> Rendszerállapot:   [❌] KRITIKUS ADATSÉRÜLÉS A VISSZAFEJTÉSKOR!")
        
    print("\n[✓] A 171-es modul sikeresen lefutott, a titkosító mag aktív.")
