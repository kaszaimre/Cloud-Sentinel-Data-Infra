#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
PROJEKT: 146_CYBER_BORSOD_CORE_ADMIN_v3.10

LEÍRÁS (HU): 
Hadműveleti állomány-nyilvántartó modul JSON adatbázis 
kezeléssel. Lehetővé teszi a tagok felvételét, törlését és a harctéri 
szintek szerinti automatikus rangsorolást.

DESCRIPTION (EN):
Operational personnel management module with JSON database 
handling. Enables adding/removing members and auto-ranking based on combat levels.

SZERZŐ: Tábornok | BORSODI WAR ROOM
================================================================================
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================================
#   CYBER-BORSOD HADMŰVELETI CORE - PERSISTENT STORAGE & DELETE ENGINE v3.10
# ======================================================================================

import json
import os

FAJL_NEV = "cyber_borsod_adatok.json"

# Alapértelmezett adatok, ha a mentési fájl még nem létezik
alap_nevek = [
    "👑 DON MÉRNÖK", "🔮 T800 ORACLE", "👔 STEFAN", "🛡️ INAS MODUL", "🤖 CYBER-BORSOD AI-04",
    "🤖 3 VAS-KLÓN", "🔪 PISTA BÁ'", "📊 KURT", "🦮 SNOOPY v5.0", "🔋 KIBER-STEFÁN", 
    "⛓️ SANYI ÉS BANDA", "⌨️ A Melós(ok)", "🐍 A 'Vas'", "🦅 A Fias", "💬 Gemini Asszisztens", 
    "🧠 Oracle v3.7", "🎯 Sigma VAS-R80", "📈 Pork Protocol v3"
]

alap_helyszinek = [
    "🏰 Rákoscsaba Bázis", "📱 Telefon/Háttér", "🎛️ Központi Labor", "🚪 Tűzfal Kapuk", "🖥️ Szerverszoba",
    "📦 Parasztkamra", "🪑 Parancsnoki Szék", "🎯 Hármas Bunker", "🖥️ Szerverszoba", "⚡ Generátorház", 
    "🧱 Frontvonal", "🗄️ Végrehajtás", "⚙️ Python Alrendszer", "🎓 Tanulási Fokozat", "🤝 Támogató Szint", 
    "🔒 Központi AI", "🔮 Központi AI", "📊 Központi AI"
]

alap_szintek = [100, 95, 90, 85, 82, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20]

alap_rangok = [
    "Legfelsőbb Parancsnok", "Központi Felderítő", "Főrend (Helyettes)", "Legfontosabb Csomópont", "Digitális Interfész",
    "Közvetlen Helyettesek", "Harctéri Tapasztalat", "Kriptopolitikai Tanácsadó", "Threat Intel", "Hardver Felelős",
    "Fizikai Végrehajtás", "Végrehajtó Állomány", "Digitális Rabszolga", "A Jövő (Közös Prog)", "Digitális Szárnysegéd", 
    "AI Stratégia", "Optikai Stealth", "Volumen Szkenner"
]

# ADATOK BETÖLTÉSE
if os.path.exists(FAJL_NEV):
    try:
        with open(FAJL_NEV, "r", encoding="utf-8") as f:
            adatok = json.load(f)
            nevek = adatok["nevek"]
            helyszinek = adatok["helyszinek"]
            szintek = adatok["szintek"]
            rangok = adatok["rangok"]
        print(f"[LOAD] Adatok betöltve a(z) {FAJL_NEV} fájlból.")
    except Exception as e:
        nevek, helyszinek, szintek, rangok = alap_nevek, alap_helyszinek, alap_szintek, alap_rangok
else:
    nevek, helyszinek, szintek, rangok = alap_nevek, alap_helyszinek, alap_szintek, alap_rangok

print("\n" + "=" * 45)
print("     [?] CYBER-BORSOD HADMŰVELETI MODUL [?]    ")
print("=" * 45)

# 1. FÁZIS: TAGFELVÉTEL
valasz_felvetel = input("Akarsz új tagot felvenni? (i/n): ").strip().lower()

if valasz_felvetel == 'i':
    print("\n" + "-" * 45)
    print("      [+] ÚJ TAG ADATAINAK BEVITELE [+]      ")
    print("-" * 45)
    uj_nev = input("Új tag neve: ")
    uj_hely = input("Harctéri helyszín: ")
    try:
        uj_szint = int(input("Harctéri szint % (0-100): "))
    except ValueError:
        uj_szint = 50
    uj_rang = input("Hadműveleti beosztás: ")
    
    nevek.append(uj_nev)
    helyszinek.append(uj_hely)
    szintek.append(uj_szint)
    rangok.append(uj_rang)

# 2. FÁZIS: TÖRLES (A RENDEZETT LISTÁBÓL)
brigad = list(zip(nevek, helyszinek, szintek, rangok))
brigad_rendezett = sorted(brigad, key=lambda x: x[2], reverse=True)

print("\n" + "-" * 45)
valasz_torles = input("Akarsz törölni valakit a rangsorból? (i/n): ").strip().lower()

if valasz_torles == 'i':
    print("\nJelenlegi rangsor azonosítókkal:")
    for idx, tag in enumerate(brigad_rendezett, 1):
        print(f" [{idx}] {tag[0]} ({tag[2]}%)")
    
    try:
        torlendo_idx = int(input("\nHányas sorszámú tagot töröljük?: "))
        if 1 <= torlendo_idx <= len(brigad_rendezett):
            # Eltávolítjuk a kiválasztott elemet a rendezett listából
            eltavolitott = brigad_rendezett.pop(torlendo_idx - 1)
            print(f"\n[DELETED] {eltavolitott[0]} sikeresen eltávolítva!")
            
            # Listák újraépítése a törlés után a mentéshez
            if brigad_rendezett:
                nevek, helyszinek, szintek, rangok = zip(*brigad_rendezett)
                nevek, helyszinek, szintek, rangok = list(nevek), list(helyszinek), list(szintek), list(rangok)
            else:
                nevek, helyszinek, szintek, rangok = [], [], [], []
                
            # MENTÉS A FÁJLBA
            with open(FAJL_NEV, "w", encoding="utf-8") as f:
                json.dump({"nevek": nevek, "helyszinek": helyszinek, "szintek": szintek, "rangok": rangok}, f, ensure_ascii=False, indent=4)
        else:
            print("[WARN] Nincs ilyen sorszám. A törlés megszakítva.")
    except ValueError:
        print("[WARN] Hibás karakter. A törlés megszakítva.")

# VÉGSŐ RANGSOR KIÍRATÁSA
print("\n" + "=" * 45)
print("   CYBER-BORSOD FRISSÍTETT RANGSOR  ")
print("=" * 45)

for index, tag in enumerate(brigad_rendezett, 1):
    prefix = f"⭐ {index}." if index <= 3 else f"   {index}."
    print(f"{prefix} {tag[0]} ({tag[2]}%)")
    print(f"   📍 {tag[1]} | 🛠️ {tag[3]}")
    print("-" * 45)

print("=" * 45)
