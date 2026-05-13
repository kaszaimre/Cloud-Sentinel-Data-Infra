import struct
import hashlib
import sys

def general_biztonsagos_csomag(payload_szoveg, szekvencia_szam=1):
    """
    Összeállít egy egyéni Cyber-Borsod hálózati csomagot.
    Struktúra: [Mágikus Szám (2B)][Szekvencia (4B)][Adathossz (2B)][SHA256 Ellenőrzőösszeg (32B)][Adat (Változó)]
    """
    print(f"[*] Csomagolás indítása... Payload: '{payload_szoveg}'")
    
    # Adat átalakítása bájtokká
    payload_bytes = payload_szoveg.encode('utf-8')
    adat_hossz = len(payload_bytes)
    magikus_szam = 0xCBCC  # Cyber-Borsod Core egyedi azonosító szignatúra
    
    # 1. Lépés: Kiszámoljuk az adat SHA256 ellenőrző összegét (Integrity Check)
    sha256_hash = hashlib.sha256(payload_bytes).digest()
    
    # 2. Lépés: Bináris csomag fejlécének összeállítása struct segítségével
    # H: unsigned short (2B), I: unsigned int (4B), 32s: 32 bájtos hash
    fejlec_formatum = f"!H I H 32s"
    fejlec_binaris = struct.pack(fejlec_formatum, magikus_szam, szekvencia_szam, adat_hossz, sha256_hash)
    
    # Teljes hálózati csomag összefűzése
    teljes_csomag = fejlec_binaris + payload_bytes
    print(f"[🟢 SUCCESS] Csomag legenerálva. Teljes bináris méret: {len(teljes_csomag)} bájt.")
    return teljes_csomag

def csomag_dekodolas_es_ellenorzes(csomag_binaris):
    """Szétbontja a kapott hálózati csomagot és ellenőrzi annak sértetlenségét."""
    try:
        fejlec_meret = struct.calcsize("!H I H 32s")
        if len(csomag_binaris) < fejlec_meret:
            print("[❌ ERROR] A kapott csomag mérete kisebb, mint a minimális fejléc!")
            return False
            
        # Fejléc kicsomagolása
        fejlec_adat = csomag_binaris[:fejlec_meret]
        magikus_szam, seq, hossz, kapott_hash = struct.unpack("!H I H 32s", fejlec_adat)
        
        # Adatrész kinyerése
        adat_bájtok = csomag_binaris[fejlec_meret:fejlec_meret+hossz]
        
        # Biztonsági ellenőrzés #1: Mágikus szám egyezik?
        if magikus_szam != 0xCBCC:
            print(f"[❌ SECURITY ALERT] Hibás mágikus szám szignatúra: {hex(magikus_szam)}!")
            return False
            
        # Biztonsági ellenőrzés #2: Adatintegritás (Hash ellenőrzés)
        szamitott_hash = hashlib.sha256(adat_bájtok).digest()
        if szamitott_hash != kapott_hash:
            print("[❌ CORRUPTION ALERT] Az adat módosult vagy megsérült a hálózaton! Hash mismatch.")
            return False
            
        print(f"[🟢 AUDIT OK] Csomag validálva. Seq: {seq} | Adat: {adat_bájtok.decode('utf-8')}")
        return True
    except Exception as e:
        print(f"[❌ ERROR] Csomagbontási hiba: {e}")
        return False

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD NETWORK -> PACKETIZER & INTEGRITY CORE   ")
    print("=========================================================")
    
    # Teszt: Csomag összeállítás és azonnali visszabontás ellenőrzése
    teszt_adat = "INTELLIGENCE_DATA_STREAM_NODE_01"
    raw_packet = general_biztonsagos_csomag(teszt_adat, szekvencia_szam=101)
    
    print("-" * 57)
    csomag_dekodolas_es_ellenorzes(raw_packet)
    print("=========================================================")
