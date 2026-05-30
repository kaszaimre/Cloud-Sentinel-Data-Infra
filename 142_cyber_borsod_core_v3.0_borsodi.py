"""
======================================================================================
# PROJEKT: 142_CYBER_BORSOD_CORE_v3.0_BORSODI
#
# LEIRAS (HU):
# Kiber-Borsodi incidens elharito motor tiszta helyi nyelvezettel. 
# ASCII logoval, borsodi dialektusra optimalizált forgatókönyvekkel 
# (Szalonna fázis, Critical Puzi). Garantáltan stabil futás Pydroid 3-ban.

#======================================================================================
# DESCRIPTION (EN):
# Cyber-Borsod incident response engine with custom local dialect. 
# Features ASCII branding and Borsod-optimized threat scenarios 
# (Szalonna phase, Critical Puzi). Guaranteed stability in Pydroid 3.
#
# SZERZO: Tabornok | BORSODI WAR ROOM

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

======================================================================================

   CYBER-BORSOD SECURITY CORE V3.0 - BORSODI DIALEKTUS EDITION [STABLE - FAIN]
   
   LEÍRÁS (HU):
   Kiber-Borsodi incidens elhárító motor tiszta helyi nyelvezettel és ASCII logóval.
   Garantáltan lefut Pydroid 3-ban, az ágyból fekve, dögölve pörgetve.
======================================================================================
"""

import time
import sys
import random
import logging

logging.basicConfig(
    filename='cyber_defense.log',
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%H:%M:%S'
)

TARGET_SERVER = "DIADAL UTCA OVERLORD (T-1000_CORE)"

# HU: A hivatalos borsodi fenyegetettségi forgatókönyvek matrixa
ATTACK_TYPES = [
    {"name": "Brute Force SSH Probalkozas", "severity": "SZALONNA FAZIS", "speed": 0.05, "level": 5},
    {"name": "DDoS UDP Flood Terheles", "severity": "MAGAS PARAZS", "speed": 0.01, "level": 8},
    {"name": "SQL Injection Adatbazis Teszt", "severity": "CRITICAL PUZI", "speed": 0.08, "level": 10},
    {"name": "XSS Kartenyek Szkript Injektalas", "severity": "HÜLE JUSER SZINT", "speed": 0.1, "level": 2}
]

stats = {
    "osszes_tamadas": 0,
    "HÜLE JUSER SZINT": 0,
    "SZALONNA FAZIS": 0,
    "MAGAS PARAZS": 0,
    "CRITICAL PUZI": 0,
    "blokkolt_ip_cimek": set()
}

# ==============================================================================
# FUNKCIÓ: print_borsodi_strike_logo()
# LEÍRÁS: A hivatalos kiber-borsodi koponyás indító fejléc standard ASCII-ben.
# ==============================================================================
def print_borsodi_strike_logo():
    CYAN = "\033[1;36m"
    RED = "\033[1;31m"
    YELLOW = "\033[1;33m"
    RESET = "\033[0m"
    
    print(CYAN + "================================================================")
    print("        --- BORSODI BRIGÁD: PHOENIX MASTER LOGIC ---")
    print("================================================================" + RESET)
    print(f"         .------.      {YELLOW}[ STATUS: BEPORKOLVA ]{RESET}")
    print(f"        /  _  _  \\     {YELLOW}[ FUEL  : NITRO PÁLESZ ]{RESET}")
    print(f"       |  (o)(o)  |    {YELLOW}[ FOOD  : SÜLT SZALONNA ]{RESET}")
    print(f"       |    __    |")
    print(f"    |  ) /____\\ (  |   {RED}<<< A VAS NEM FELEJT >>>{RESET}")
    print(f"    |\\/    /\\    \\/|")
    print(f"    (_____/  \\_____)   {RED}<<< A PUZI MEGOLVAD >>>{RESET}")
    print(f"         |IIIIII|")
    print(f"         |IIIIII|      {CYAN}[ BORSOD DISTRICT 352 ]{RESET}")
    print(f"          \\______/      {CYAN}[ DIADAL UTCA OVERLORD ]{RESET}")
    print(CYAN + "================================================================" + RESET)
    time.sleep(1)

def draw_threat_meter(level):
    colors = {"HÜLE JUSER SZINT": "\033[92m", "SZALONNA FAZIS": "\033[93m", "MAGAS PARAZS": "\033[91m", "CRITICAL PUZI": "\033[41m\033[97m"}
    reset = "\033[0m"
    
    color_keys = list(colors.keys())
    idx = max(0, min(level - 1, len(color_keys) - 1))
    chosen_color = colors[color_keys[idx]]
    
    bar_level = max(1, min(level, 10))
    meter = "#" * (2 * bar_level) + "-" * (20 - 2 * bar_level)
    return f"[{chosen_color}{meter}{reset}]"

def simulate_attack(attack):
    print(f"\n\033[91m[!] RIASZTAS / ALERT:\033[0m Eszlelt esemeny: {attack['name']}")
    print(f"[!] Celpont: {TARGET_SERVER} | Kiber-Szint: {attack['severity']}")
    
    stats["osszes_tamadas"] += 1
    stats[attack['severity']] += 1
    
    logging.warning(f"Rjibanc eszlelve: {attack['name']}")
    time.sleep(0.3)
    
    print("Bejovo kartenyek csomagok dekodolasa...")
    for _ in range(1, 16):
        hex_data = f"0x{random.randint(1000, 9999):X}"
        ip_src = f"185.234.{random.randint(1,254)}.{random.randint(1,254)}"
        stats["blokkolt_ip_cimek"].add(ip_src)
        
        sys.stdout.write(f"  -> [{ip_src}] INJECT: {hex_data} ... KODRJIBANC SZURES\r")
        sys.stdout.flush()
        time.sleep(attack['speed'])
    print("\n[+] Csomagelemzes kesz. A heurisztika leallt.")

def deploy_defense(attack):
    print("\033[94m[*] BORSODI REAKCIO INDITASA / DEPLOYING DEFENSE...\033[0m")
    time.sleep(0.3)
    
    actions = [
        "[OK] Forras IP-k automatikusan BEPORKOLVA a tuzfalon.",
        "[OK] Forgalom atterelve a fustolo rostej proxyra.",
        "[OK] Szigma entropia kulcsok es palesz szintek ujragenerALACSONYa.",
        "[OK] Rendszerintegritas ellenorizve. A vas STABIL."
    ]
    
    for action in actions:
        sys.stdout.write(f"  {action}\n")
        sys.stdout.flush()
        time.sleep(0.1)
        
    logging.info(f"Sikeres elharitas: {attack['name']} blokkolva.")
    print("\033[92m[V VEDELEM] A puzi megolvadt, a veszely semlegesitve.\033[0m")

def start_soc_center():
    print_borsodi_strike_logo()
    
    while True:
        print("\n" + "-"*70)
        print(f"🎮 RENDELKEZESRE ALLO BORSODI MATRIXXOK:")
        for idx, att in enumerate(ATTACK_TYPES):
            print(f" [{idx+1}] {att['name']} ({att['severity']})")
        print(f" [{len(ATTACK_TYPES)+1}] Tomeges rjibanc hullam inditasa (All-In)")
        print(f" [q] SOC Kozpont leallitasa es zaro szalonnazas")
        print("-" * 70)
        
        valasztas = input("Melyik hurok fusson, Don Mernok Ur? ").lower()
        
        if valasztas == 'q':
            break
            
        if valasztas == str(len(ATTACK_TYPES) + 1):
            print("\n\033[5;91m⚠️ [CRITICAL PUZI] ÖSSZETETT RJIBANC DETEKTÁLVA! ⚠️\033[0m")
            for _ in range(3):
                attack = random.choice(ATTACK_TYPES)
                print(draw_threat_meter(attack['level']))
                simulate_attack(attack)
                deploy_defense(attack)
                time.sleep(0.5)
        else:
            try:
                idx = int(valasztas) - 1
                if 0 <= idx < len(ATTACK_TYPES):
                    selected_attack = ATTACK_TYPES[idx]
                    print(draw_threat_meter(selected_attack['level']))
                    simulate_attack(selected_attack)
                    deploy_defense(selected_attack)
                else:
                    print("\033[91mNincs ilyen hurok!\033[0m")
            except ValueError:
                print("\033[91mErvenytelen palasz!\033[0m")
                
    # --- VÉGSŐ JELENTÉS ---
    print("\n" + "\033[96m" + "=" * 70)
    print("   [📊] FINAlis BORSODI INCIDENS JELENTES")
    print("=" * 70 + "\033[0m")
    print(f" Elkapott rjibancok szama:  {stats['osszes_tamadas']} db")
    print(f" [+] Hüle Juser szintu:     {stats['HÜLE JUSER SZINT']} db")
    print(f" [+] Szalonna Fazisu:       {stats['SZALONNA FAZIS']} db")
    print(f" [+] Magas Parazs szintu:   {stats['MAGAS PARAZS']} db")
    print(f" [+] Critical Puzi szintu:  {stats['CRITICAL PUZI']} db")
    print(f" [!] Tuzfalra kuldott IP-k: {len(stats['blokkolt_ip_cimek'])} db")
    print("-" * 70)
    print("\033[92m Rendszerallapot: A TASKA HIZIK | Logfajl rogzitve: cyber_defense.log\033[0m")
    print("\033[96m" + "=" * 70 + "\033[0m")

if __name__ == "__main__":
    start_soc_center()
