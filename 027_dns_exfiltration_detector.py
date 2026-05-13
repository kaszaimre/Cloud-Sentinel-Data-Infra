# ==============================================================================
# FÁJL NÉV: 027_dns_exfiltration_detector.py
# SORSZÁM: 027
#
# LEÍRÁS ÉS FELADAT:
# DNS alapú adatszivárgás-detektáló (DNS Exfiltration Detector) modul. 
# Heurisztikus elemzéssel vizsgálja a lekérdezett aldomainek hosszát és entrópiáját.
# Ha egy hosztnév túl hosszú vagy gyanúsan kódolt karakterláncot tartalmaz, a modul
# riasztást ad, mert a támadók titkosított adatokat próbálnak kicsempészni a hálózatból.
# ==============================================================================

import re
import math

def kiszamol_entropia(szoveg):
    """Kiszámolja a szöveg Shannon-entrópiáját a gyanús kódolás kiszűrésére."""
    if not szoveg:
        return 0
    szamlalo = {}
    for karakter in szoveg:
        szamlalo[karakter] = szamlalo.get(karakter, 0) + 1
    
    entropia = 0
    for karakter, darab in szamlalo.items():
        p = darab / len(szoveg)
        entropia -= p * math.log2(p)
    return round(entropia, 2)

def dns_adatkimenet_szures(domain_nev):
    """Heurisztikus elemzést futtat a megadott domain néven."""
    # Kiszedjük az aldomain részt az elemzéshez
    reszek = domain_nev.split('.')
    if len(reszek) < 3:
        return True # Túl rövid, valószínűleg legitim
        
    aldomain = "".join(reszek[:-2])
    entropia = kiszamol_entropia(aldomain)
    hossz = len(aldomain)
    
    # Kiberbiztonsági küszöbértékek: 60 karakternél hosszabb vagy 4.2 feletti entrópia (pl. Base64 kódolás)
    if hossz > 60 or entropia > 4.2:
        print(f"  [🚨 ANOMÁLY DETECTED] High entropy/length signature on DNS query!")
        print(f"    [-] Target Subdomain: {aldomain[:30]}...")
        print(f"    [-] Subdomain Length: {hossz} bytes (Threshold: 60)")
        print(f"    [-] Shannon Entropy : {entropia} (Threshold: 4.2)")
        return False
        
    return True

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD NETSEC -> DNS EXFILTRATION DETECTOR     ")
    print("=========================================================")
    
    # Teszt esetek: egy normál céges kérés és egy gyanús, titkosított adatszivárgás
    teszt_domainek = [
        "internal-update.server.cyberborsod.local",
        "attack-cnc-server.com"
    ]
    
    for dm in teszt_domainek:
        print(f"[*] Auditing DNS Query: {dm}")
        if dns_adatkimenet_szures(dm):
            print("  [🟢 COMPLIANT] Traffic cleared by heuristic guard.")
        else:
            print("  [❌ EXFILTRATION ALERT] Malicious encapsulation blocked.")
        print("-" * 57)
        
    print("=========================================================")
