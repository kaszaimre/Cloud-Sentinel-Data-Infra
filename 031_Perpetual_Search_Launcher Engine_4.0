#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================================
#   CYBER-BORSOD SECURITY CORE - PERPETUAL SEARCH LAUNCHER ENGINE v4.0
#   
#   LEÍRÁS (HU):
#   Ez a modul a kilövőállomás végleges, rekurzív változata (v4.0). Egy belső főciklus
#   segítségével lehetővé teszi, hogy egy program lefutása után a felhasználó azonnal
#   visszatérjen a keresőhöz/listához egy újabb fájl kiválasztásához. Az Örök Stealth 
#   Altatás csak akkor aktiválódik, ha a felhasználó végleg befejezi a munkát (n gomb).
#   
#   DESCRIPTION (EN):
#   This module is the definitive, recursive version of the launcher station (v4.0).
#   Utilizing a main background loop, it allows the user to immediately return to the
#   search/list view after a script finishes to select another file. The Perpetual 
#   Stealth Sleep only triggers when the user explicitly finishes the session (n key).
# ======================================================================================

import os
import sys
import time

def cyber_borsod_perpetual_sleep():
    """Örök altatás a reklámok ellen / Infinite background sleep against ads"""
    print("\n" + "=" * 55)
    print("[SECURITY] MINDEN MŰVELET BEFEJEZŐDÖTT. AZ ALTATÓ PAJZS AKTÍV!")
    print("[MOTTÓ] 'A borsodi nem lép ki, a borsodi elaltat.'")
    print("[INFO] Söpörd ki az appot a háttérből a tiszta visszatéréshez!")
    print("=" * 55 + "\n")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print("\n[SYSTEM] Ébredés.")

def main_perpetual_launcher():
    while True:
        print("\n" + "=" * 55)
        print("  [🚀] CYBER-BORSOD PERPETUAL SEARCH LAUNCHER v4.0  ")
        print("=" * 55)
        
        # Kigyűjtjük az összes .py fájlt a mappából
        # Scanning directory for all .py files, excluding this script
        aktualis_fajl = os.path.basename(__file__)
        osszes_fajl = sorted([f for f in os.listdir('.') if f.endswith('.py') and f != aktualis_fajl])

        if not osszes_fajl:
            print("\n[WARN] Nem található más .py fájl ebben a mappában!")
            print("-" * 55)
            cyber_borsod_perpetual_sleep()
            return

        print(f"[INFO] Sikeresen beolvasva: {len(osszes_fajl)} darab Python fájl.")
        
        # KERESÉSI/SZŰRÉSI FÁZIS
        kereses = input("\n🔍 Írj be egy kulcsszót a szűréshez (vagy Enter a teljes listához): ").strip().lower()
        
        if kereses:
            szurt_fajlok = [f for f in osszes_fajl if kereses in f.lower()]
        else:
            szurt_fajlok = osszes_fajl

        if not szurt_fajlok:
            print(f"\n[WARN] Nincs találat erre a kulcsszóra: '{kereses}'")
            input("\nNyomj Enter-t az újrakísérléshez...")
            continue

        # Kijelzés sorszámozva
        print(f"\n[📂] REKLÁMMENTES TALÁLATOK ({len(szurt_fajlok)}/{len(osszes_fajl)}):")
        print("-" * 55)
        for idx, fajl_nev in enumerate(szurt_fajlok, 1):
            print(f"  [{idx}] {fajl_nev}")
        print("-" * 55)

        # Választás bekérése
        try:
            valasztas = input("Válaszd ki a futtatni kívánt program sorszámát: ").strip()
            fajl_idx = int(valasztas) - 1
            
            if 0 <= fajl_idx < len(szurt_fajlok):
                cel_fajl = szurt_fajlok[fajl_idx]
                print(f"\n[EXECUTE] {cel_fajl} indítása tiszta környezetben...\n" + "—" * 55)
                time.sleep(0.5)
                
                # Beolvasás és dinamikus futtatás
                with open(cel_fajl, "r", encoding="utf-8") as f:
                    kod_tartalom = f.read()
                
                exec(kod_tartalom, globals())
                print("—" * 55)
                
            else:
                print("\n[WARN] Hibás sorszám! A futtatás megszakítva.")
        except ValueError:
            print("\n[WARN] Hibás karakter! Csak számot írj be.")
        except Exception as e:
            print(f"\n[ERROR] Hiba a kód futtatása közben: {e}")

        # ÚJRAINDÍTÁSI ELÁGAZÁS / RECURSIVE PROMPT
        valasz = input("\n🔄 Akarsz másik programot futtatni? (i/n): ").strip().lower()
        if valasz != 'i':
            break  # Kilépünk a főciklusból, és rácsapjuk az altatót!

    # Ha a felhasználó n-t nyomott, vagy befejezte, élesedik az örök védelem
    cyber_borsod_perpetual_sleep()

if __name__ == "__main__":
    main_perpetual_launcher()
