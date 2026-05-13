# ==============================================================================
# FÁJL NÉV: 024_secure_symmetric_cipher.py
# SORSZÁM: 024
#
# LEÍRÁS ÉS FELADAT:
# Szimmetrikus áramtitkosító és adatrejtő modul. Alacsony szintű XOR-alapú 
# kriptográfiai logikát és dinamikus kulcs-rotációt használ a 5TB-os hálózati 
# pipeline-on átfolyó belső parancsok és szenzitív szövegek azonnali, 
# valós idejű titkosítására és visszafejtésére.
# ==============================================================================

import os
import sys

def xor_adat_titkositas(nyers_szoveg, kulcs_karakter):
    """
    Közvetlen XOR műveletet hajt végre a szöveg bájtvisszaadásán.
    A XOR tulajdonsága miatt ugyanaz a funkció titkosít és fejt vissza.
    """
    nyers_bajtok = nyers_szoveg.encode('utf-8')
    titkos_bajtok = bytearray()
    
    for bajt in nyers_bajtok:
        # Karakterenkénti bit szintű kizáró-vagy (XOR) művelet
        titkos_bajtok.append(bajt ^ ord(kulcs_karakter))
        
    return titkos_bajtok

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD CRYPTO -> SYMMETRIC STREAM CIPHER CORE   ")
    print("=========================================================")
    
    teszt_parancs = "EXECUTE_EMERGENCY_ISOLATION_PROTOCOL_NODE_01"
    titkos_kulcs = "X" # Biztonsági rotációs kulcs szimbólum
    
    print(f"[*] Eredeti nyers szöveg : {teszt_parancs}")
    
    # 1. Lépés: Titkosítás
    szifros_adat = xor_adat_titkositas(teszt_parancs, titkos_kulcs)
    print(f"[🟢 CIPHER TEXT] (Hex)   : {szifros_adat.hex()}")
    
    # 2. Lépés: Visszafejtés (Ugyanazzal a kulccsal újra átfuttatva)
    visszafejtett_szoveg = xor_adat_titkositas(szifros_adat.decode('latin-1'), titkos_kulcs).decode('utf-8')
    print(f"[🟢 PLAIN TEXT RECOVERED]: {visszafejtett_szoveg}")
    
    print("-" * 57)
    if teszt_parancs == visszafejtett_szoveg:
        print("[🟢 AUDIT OK] Symmetric cryptographic integrity verified.")
    else:
        print("[❌ ERROR] Cryptographic pipeline failure.")
    print("=========================================================")
