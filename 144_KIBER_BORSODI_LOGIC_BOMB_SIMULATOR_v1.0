#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
# PROJEKT: 144_KIBER_BORSODI_LOGIC_BOMB_SIMULATOR_v1.0
#
# LEÍRÁS (HU):
# Oktatókód a rejtett logikai bombák működéséről. A modul bemutatja, 
# hogyan aktiválódik egy rendszer-zár (detonáció) bizonyos feltételek 
# (pl. 'palesz_szint') teljesülése esetén. Stabil Pydroid környezetben.
#
# DESCRIPTION (EN):
# Educational module on the mechanics of logic bombs. Demonstrates how 
# a system lock (detonation) is triggered based on specific state conditions 
# (e.g., 'palesz_szint'). Stable in Pydroid environment.
#
# SZERZŐ: Tábornok | BORSODI WAR ROOM
================================================================================
"""

# ==============================================================================
# PROJEKT: KIBER-BORSODI LOGIC BOMB SIMULATOR (v1.0)
# LEÍRÁS: Szoftvertesztelői oktatókód a rejtett logikai bombák működéséről.
# SZERZŐ: Don Mérnök (Tábornok)
# ==============================================================================

import time
import sys

RED     = "\033[1;31m"
GREEN   = "\033[1;32m"
YELLOW  = "\033[1;33m"
CYAN    = "\033[1;36m"
RESET   = "\033[0m"

def inditas():
    print(CYAN + "========================================")
    print("      BORSODI CORE: LOGIC BOMB TEST     ")
    print("        <<< A VAS NEM FELEJT >>>        ")
    print("========================================" + RESET)
    
    print("\n[!] A kód csendben fut a háttérben a szerveren...")
    time.sleep(1.5)
    
    # A logikai feltétel, amire a bomba élesedik (pl. ha a palesz szint kritikus)
    palesz_szint = "üres" 
    
    print(f"[🔍] Monitorozás: Palesz állapot -> '{palesz_szint}'")
    time.sleep(1)
    
    if palesz_szint == "üres":
        # 💥 A LOGIKAI BOMBA AKTIVÁLÓDIK
        print(RED + "\n[💥💥💥] LOGIKAI BOMBA DETONÁCIÓ! [💥💥💥]" + RESET)
        print(RED + "A Kiber-Borsodi likviditás lezárva, a rendszer beporkolva!" + RESET)
        
        # Egy kis vizuális visszaszámlálás-effekt a terminálban
        for i in range(5, 0, -1):
            sys.stdout.write(f"\r Rendszer összeomlás: {i} másodperc... ")
            sys.stdout.flush()
            time.sleep(0.5)
            
        print(RED + "\n[!] KAPUT. A puzi megolvadt." + RESET)
    else:
        print(GREEN + "[✔] Minden stabil, a logikai feltétel nem teljesült." + RESET)

if __name__ == "__main__":
    inditas()
