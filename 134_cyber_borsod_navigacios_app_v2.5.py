#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================================
#   CYBER-BORSOD SECURITY CORE - NAVIGATIONAL RETURN PRIVATE APP v2.5
#   
#   LEÍRÁS (HU):
#   Ez az alkalmazás a v2.0 továbbfejlesztett változata, amely tartalmazza a 6-os 
#   menüpontot. Ez a funkció lehetővé teszi, hogy a felhasználó egyetlen gombnyomással
#   kilépjen az interaktív menüből, és azonnal visszatérjen a Pydroid szerkesztőjébe
#   a forráskódhoz, tiszta memóriakezelés mellett.
#   
#   DESCRIPTION (EN):
#   This application is the upgraded version of v2.0, featuring menu option 6.
#   This function allows the user to exit the interactive menu with a single keystroke
#   and immediately return to the Pydroid editor view to inspect the source code,
#   ensuring clean memory management.
# ======================================================================================

import json
import os
import random
import time
import sys

FAJL_NEV = "cyber_borsod_app_data.json"

def betolt_adatok():
    """Adatbázis betöltése / Loading database"""
    if os.path.exists(FAJL_NEV):
        try:
            with open(FAJL_NEV, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {
        "nevek": ["👑 DON MÉRNÖK", "🤖 CYBER-BORSOD AI-04", "🛡️ INAS MODUL"],
        "helyszinek": ["🏰 Rákoscsaba Bázis", "🖥️ Szerverszoba", "🚪 Tűzfal Kapuk"],
        "szintek": [100, 82, 85],
        "rangok": ["Legfelsőbb Parancsnok", "Digitális Interfész", "Legfontosabb Csomópont"]
    }

def ment_adatok(adatok):
    try:
        with open(FAJL_NEV, "w", encoding="utf-8") as f:
            json.dump(adatok, f, ensure_ascii=False, indent=4)
    except:
        pass

def get_kraken3x_text(secret_message):
    kraken_hirek = [
        "Kraken's parent company Payward streamlines operations ahead of planned IPO",
        "Kraken Pro rolls out 100x leverage on BTC and ETH perpetual futures contracts",
        "Crypto market update: Bitcoin tests liquidity levels with low volatility",
        "Kraken expansion continues aggressively into B2B global payments infrastructure"
    ]
    random.shuffle(kraken_hirek)
    selected = kraken_hirek[:2]
    selected.insert(1, f" [BORSOD_CORE_DATA: {secret_message}] ")
    return ". ".join(selected)

def main_app():
    adatok = betolt_adatok()
    
    while True:
        print("\n" + "=" * 50)
        print("  [⚡] CYBER-BORSOD PRIVÁT NAVIGÁCIÓS APP v2.5 [⚡]  ")
        print("=" * 50)
        print(" 1 🕵️  Kraken3x Élő Adat-Injektálás (Eldugó)")
        print(" 2 📊 Hadműveleti Rangsor Megtekintése")
        print(" 3 ➕ Új Tag Behívása / Felvétele")
        print(" 4 🗑️  Hülyeségek Kitörlése Sorszám Alapján")
        print(" 5 📴 Örök Stealth Altatás (Reklámgyilkos hurok)")
        print(" 6 ⌨️  Vissza a kódhoz (Kilépés a Pydroid szerkesztőbe)")
        print("=" * 50)
        
        valasztas = input(" Válassz műveletet (1-6): ").strip()
        
        if valasztas == "1":
            print("\n" + "-" * 50)
            titok = input("Írd be a botok elől elrejtendő szöveget: ")
            alcazott = get_kraken3x_text(titok)
            print("-" * 50)
            print(f"[KRAKEN3X KOCKA VERZIÓ EREDMÉNY]:\n{alcazott}")
            print("-" * 50)
            input("\nNyomj Enter-t a menübe való visszatéréshez...")
            
        elif valasztas == "2":
            brigad = list(zip(adatok["nevek"], adatok["helyszinek"], adatok["szintek"], adatok["rangok"]))
            rendezett = sorted(brigad, key=lambda x: x[2], reverse=True)
            print("\n" + "—" * 50)
            print("   ÁLLANDÓ HADMŰVELETI RANGSOR:")
            print("—" * 50)
            for idx, tag in enumerate(rendezett, 1):
                prefix = f"⭐ {idx}." if idx <= 3 else f"   {idx}."
                print(f"{prefix} {tag[0]} ({tag[2]}%)\n   📍 {tag[1]} | 🛠️ {tag[3]}")
                print("-" * 40)
            input("\nNyomj Enter-t a menübe való visszatéréshez...")
            
        elif valasztas == "3":
            print("\n[+] ÚJ TAG FELVÉTELE")
            nev = input(" Név: ")
            hely = input(" Helyszín: ")
            try: szint = int(input(" Szint % (0-100): "))
            except: szint = 50
            rang = input(" Beosztás: ")
            adatok["nevek"].append(nev)
            adatok["helyszinek"].append(hely)
            adatok["szintek"].append(szint)
            adatok["rangok"].append(rang)
            ment_adatok(adatok)
            input("\nNyomj Enter-t...")
            
        elif valasztas == "4":
            brigad = list(zip(adatok["nevek"], adatok["helyszinek"], adatok["szintek"], adatok["rangok"]))
            rendezett = sorted(brigad, key=lambda x: x[2], reverse=True)
            print("\n[🗑️] TÖRLÉSI LISTA:")
            for idx, tag in enumerate(rendezett, 1):
                print(f" [{idx}] {tag[0]} ({tag[2]}%)")
            try:
                torol_idx = int(input("\nHányas sorszámú elemet töröljük?: "))
                if 1 <= torol_idx <= len(rendezett):
                    kivett = rendezett.pop(torol_idx - 1)
                    if rendezett:
                        adatok["nevek"], adatok["helyszinek"], adatok["szintek"], adatok["rangok"] = zip(*rendezett)
                        adatok["nevek"], adatok["helyszinek"], adatok["szintek"], adatok["rangok"] = list(adatok["nevek"]), list(adatok["helyszinek"]), list(adatok["szintek"]), list(adatok["rangok"])
                    else: adatok = {"nevek":[], "helyszinek":[], "szintek":[], "rangok":[]}
                    ment_adatok(adatok)
            except: pass
            input("\nNyomj Enter-t...")
            
        elif valasztas == "5":
            print("\n" + "=" * 50)
            print("[SYSTEM] ÖRÖK STEALTH MÓD AKTIVÁLVA.")
            print("[INFO] A program futása zárolva. Zéró reklámlehetőség.")
            print("=" * 50 + "\n")
            try:
                while True:
                    time.sleep(3600)
            except KeyboardInterrupt:
                print("\n[SYSTEM] Visszatérés a főmenübe.")
                
        elif valasztas == "6":
            # 6-OS GOMB: Tiszta kilépés közvetlenül a Pydroid szerkesztő felületére
            # OPTION 6: Clean exit directly back to the Pydroid editor view
            print("\n[SYSTEM] Kilépési kapu aktiválva. Visszatérés a forráskódhoz...")
            time.sleep(0.5)
            break  # Megszakítja a while ciklust, így a program tisztán fejeződik be
            
        else:
            input("\nHibás menüpont! Nyomj Enter-t...")

if __name__ == "__main__":
    main_app()
