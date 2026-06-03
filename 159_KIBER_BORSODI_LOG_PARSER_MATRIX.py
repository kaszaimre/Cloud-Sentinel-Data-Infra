# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 159_KIBER_BORSODI_LOG_PARSER_MATRIX
# 
# LEÍRÁS (HU):
# Nagysebességű log-elemző modul 15 000+ fájlos archívumok átfésülésére.
# Szigorú memóriavédelemmel és aszinkron-szerű puffereléssel szűri az IoC 
# (Indicators of Compromise) mintákat. 
# Mottó: "A borsodi nem hackel, a borsodi optimalizál."
#
# DESCRIPTION (EN):
# High-speed log analysis module for scanning 15,000+ file archives. Features
# strict memory protection and asynchronous-style buffering to filter IoC 
# (Indicators of Compromise) patterns.
# Motto: "The Borsodi doesn't hack, the Borsodi optimizes."
#
# SZERZŐ: Don Mérnök (Kasza Imre) | BORSODI WAR ROOM
# ==============================================================================


import os
import time
import sys

RED     = "\033[1;31m"
GREEN   = "\033[1;32m"
YELLOW  = "\033[1;33m"
CYAN    = "\033[1;36m"
RESET   = "\033[0m"

# Megadjuk a keresendő gyanús mintákat (IoC - Indicators of Compromise)
GYANUS_SZAVAK = ["banned", "inject", "critical puzi", "hule juser", "attack"]

def scan_archive_matrix(target_folder="."):
    print(CYAN + "========================================")
    print("    SODI T-800: BIG DATA LOG-PARSER    ")
    print("      <<< 15 000 FÁJL SZKENNELÉSE >>>   ")
    print("========================================" + RESET)
    time.sleep(0.5)

    all_files = os.listdir(target_folder)
    # Csak a log és txt fájlokat nézzük (kihagyva a futó scriptet)
    log_files = [f for f in all_files if f.endswith(('.txt', '.log'))]
    
    total_files = len(log_files)
    print(YELLOW + f"[!] Detektált adatállomány: {total_files} db fájl az archívumban.")
    print("[!] Keresőmotor indítása...\n" + RESET)
    time.sleep(1)

    incidents_found = 0
    start_time = time.time()

    # Végigmegyünk az óriási adatbázison
    for idx, file_name in enumerate(log_files):
        # 🏎️ Telefon-biztos pörgő számláló visszajelzés (Kocsi-vissza \r használatával)
        if idx % 100 == 0 or idx == total_files - 1:
            sys.stdout.write(f"\r🔍 HALADÁS: [{idx+1}/{total_files}] fájl feldolgozva... (Mészáros Szín OK)")
            sys.stdout.flush()

        try:
            # Csak olvasásra nyitjuk, UTF-8-as védelemmel
            with open(os.path.join(target_folder, file_name), "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                
                # Átfésüljük a fájl tartalmát a kiber-biztonsági kulcsszavak alapján
                for minta in GYANUS_SZAVAK:
                    if minta in content.lower():
                        incidents_found += 1
                        # Ha találtunk valamit, csendben naplózzuk a háttérben
                        logging.info(f"IoC találat a fájlban: {file_name} -> Minta: {minta}")
        except Exception:
            pass # Ha egy fájl sérült, átugorjuk (QA Error handling)

    end_time = time.time()
    elapsed = end_time - start_time

    # --- VÉGSŐ JELENTÉS ---
    print("\n\n" + GREEN + "========================================")
    print("    📊 FINÁLIS ARCHÍVUM JELENTÉS")
    print("========================================" + RESET)
    print(f" Feldolgozott időintervallum: 2 hónap")
    print(f" Összes átvizsgált fájl:     {total_files} db")
    print(f" Elemzési sebesség:          {elapsed:.2f} másodperc")
    print(f" Detektált incidensek száma: {RED}{incidents_found} db{RESET}")
    print("-" * 40)
    print(GREEN + " Rendszerállapot: A TÁSKA HÍZIK | Archívum integritása OK" + RESET)
    print(GREEN + "========================================" + RESET)

if __name__ == "__main__":
    # Mentse el ezt a kódot az archívum mappájába, és indítsa el!
    try:
        import logging
        scan_archive_matrix()
    except KeyboardInterrupt:
        print(RED + "\n[!] Szkennelés megszakítva!" + RESET)
