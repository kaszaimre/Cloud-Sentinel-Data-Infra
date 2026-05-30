# ==============================================================================
# PROJEKT: 140_CYBER_BORSOD_INCIDENT_SIMULATOR_v2.5
# 
# LEÍRÁS (HU):
# Kiberbiztonsági szimulátor valós idejű statisztikai adatelemzéssel és 
# automatikus incidenskezeléssel. A modul a beérkező támadások (DDoS, SQLi, 
# Brute Force) hálózati izolációját és a tűzfal-reakciókat modellezi. 
# Minden eseményt a 'cyber_defense.log' fájlba naplóz.
#
# DESCRIPTION (EN):
# Cybersecurity simulator with real-time statistical data analysis and 
# automated incident response. This module models network isolation and 
# firewall reactions to various attacks (DDoS, SQLi, Brute Force). 
# All events are logged to the 'cyber_defense.log' file.
#
# SZERZŐ: Tábornok | BORSODI WAR ROOM
# ==============================================================================

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
======================================================================================
   CYBER-BORSOD SECURITY CORE V2.5 - ATTACK SIMULATOR WITH ADVANCED STATISTICS
   
   LEÍRÁS (HU):
   Kiberbiztonsági szimulátor valós idejű statisztikai adatelemzéssel és naplózással.
   Ez a modul bemutatja az automatikus incidenskezelést és a védelmi reakciókat.
   
   DESCRIPTION (EN):
   Cybersecurity simulator with real-time statistical data analysis and logging.
   This module demonstrates automated incident response and defense reactions.
======================================================================================
"""

import time
import sys
import random
import logging

# HU: Helyi naplózási struktúra beállítása a cyber_defense.log fájlba
# EN: Setting up the local logging structure into the cyber_defense.log file
logging.basicConfig(
    filename='cyber_defense.log',
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%H:%M:%S'
)

# HU: Globális konfigurációk, fiktív célpont és támadási típusok definíciói
# EN: Global configurations, definitions of the fictional target and attack types
TARGET_SERVER = "192.168.1.100 (T-1000_CORE)"
ATTACK_TYPES = [
    {"name": "Brute Force SSH Próbálkozás", "severity": "KÖZEPES", "speed": 0.05},
    {"name": "DDoS UDP Flood Terhelés", "severity": "MAGAS", "speed": 0.01},
    {"name": "SQL Injection Adatbázis Teszt", "severity": "KRITIKUS", "speed": 0.08},
    {"name": "XSS Kártékony Szkript Injektálás", "severity": "ALACSONY", "speed": 0.1}
]

# HU: Globális statisztikai számláló szótár az adatok valós idejű követésére
# EN: Global statistical counter dictionary for real-time data tracking
stats = {
    "összes_támadás": 0,
    "ALACSONY": 0,
    "KÖZEPES": 0,
    "MAGAS": 0,
    "KRITIKUS": 0,
    "blokkolt_ip_cimek": set() # HU: Egyedi IP címek / EN: Unique IP addresses
}

def print_header():
    """
    HU: Rendszer fejléc és fiktív cégjelzés kirajzolása.
    EN: Displaying the system header and fictional company branding.
    """
    print("\033[95m" + "=" * 70 + "\033[0m")
    print("   [🔒] CYBER-BORSOD INCIDENT RESPONSE & SECURITY SIMULATOR [🔒]   ")
    print("   Szervervédelem, Automatikus Elhárítás és Statisztikai Mod     ")
    print("\033[95m" + "=" * 70 + "\033[0m")
    time.sleep(1)

def draw_threat_meter(level):
    """
    HU: Fenyegetettségi szint vizuális kijelzése színes sávdiagrammal.
    EN: Visual representation of the threat level using a colored bar chart.
    """
    colors = {"ALACSONY": "\033[92m", "KÖZEPES": "\033[93m", "MAGAS": "\033[91m", "KRITIKUS": "\033[41m\033[97m"}
    reset = "\033[0m"
    meter = "█" * (2 * level) + "░" * (20 - 2 * level)
    return f"[{colors[list(colors.keys())[level-1]]}{meter}{reset}]"

def simulate_attack(attack):
    """
    HU: Támadási hullám szimulálása, bejövő kártékony csomagok és IP-k elemzése.
    EN: Simulating the attack wave, analyzing incoming malicious packets and IPs.
    """
    print(f"\n\033[91m[!] RIASZTÁS / ALERT:\033[0m Észlelt esemény: {attack['name']}")
    print(f"[!] Célpont / Target: {TARGET_SERVER} | Szint / Severity: {attack['severity']}")
    
    # HU: Statisztikák frissítése a memóriában
    # EN: Updating statistics in the memory
    stats["összes_támadás"] += 1
    stats[attack['severity']] += 1
    
    logging.warning(f"Támadás észlelve: {attack['name']} -> Célpont: {TARGET_SERVER}")
    time.sleep(0.5)
    
    print("Bejövő kártékony csomagok elemzése / Analyzing incoming packets:")
    for _ in range(1, 16):
        hex_data = f"0x{random.randint(1000, 9999):X}"
        ip_src = f"185.234.{random.randint(1,254)}.{random.randint(1,254)}"
        stats["blokkolt_ip_cimek"].add(ip_src)
        
        sys.stdout.write(f"  -> [{ip_src}] INJECT: {hex_data} ... SZŰRÉS ALATT\r")
        sys.stdout.flush()
        time.sleep(attack['speed'])
    print("\n[+] Csomagelemzés kész / Packet analysis complete.")

def deploy_defense(attack):
    """
    HU: Automatikus védelmi mechanizmusok és elhárítási lépések futtatása.
    EN: Deploying automated defense mechanisms and mitigation steps.
    """
    print("\033[94m[*] VÉDELMI REAKCIÓ INDÍTÁSA / DEPLOYING DEFENSE...\033[0m")
    time.sleep(0.5)
    
    actions = [
        "[OK] Forrás IP címek automatikus tiltása a tűzfalon (iptables BANNED).",
        "[OK] Forgalom átirányítása a biztonsági szűrő proxy-ra (Proxy routing).",
        "[OK] Szigma entrópia kulcsok újragenerálása és hálózati izoláció.",
        "[OK] Rendszerintegritás ellenőrizve. A szerver magja STABIL."
    ]
    
    for action in actions:
        sys.stdout.write(f"  {action}\n")
        sys.stdout.flush()
        time.sleep(0.2)
        
    logging.info(f"Sikeres elhárítás: {attack['name']} blokkolva. Rendszer védve.")
    print("\033[92m[VÉDELEM] A fenyegetést sikeresen semlegesítettük (Mitigated).\033[0m")

def print_final_statistics():
    """
    HU: Részletes, kétnyelvű statisztikai jelentés kiírása a program leállításakor.
    EN: Displaying a detailed, bilingual statistical report upon application exit.
    """
    print("\n\n" + "=" * 70)
    print("   [📊] CYBER-BORSOD SEC - INCIDENS STATISZTIKAI JELENTÉS / REPORT [📊]   ")
    print("=" * 70)
    print(f" Regisztrált és elhárított támadások / Total attacks mitigated: {stats['összes_támadás']} db")
    print(f" Tűzfal által tiltott egyedi IP-k / Unique IPs banned by firewall: {len(stats['blokkolt_ip_cimek'])} db")
    print("-" * 70)
    print(" TÁMADÁSOK SÚLYOSSÁG SZERINT / ATTACKS BY SEVERITY:")
    print(f"  🟢 ALACSONY / LOW:      {stats['ALACSONY']} db")
    print(f"  🟡 KÖZEPES / MEDIUM:    {stats['KÖZEPES']} db")
    print(f"  🔴 MAGAS / HIGH:        {stats['MAGAS']} db")
    print(f"  💥 KRITIKUS / CRITICAL: {stats['KRITIKUS']} db")
    print("=" * 70)
    print("[OK] Minden adat archiválva a 'cyber_defense.log' fájlba. Viszlát!")
    print("=" * 70 + "\n")

def system_dashboard():
    """
    HU: Fő vezérlőhurok, amely az események folyamatos futtatásáért felel.
    EN: Main control loop responsible for the continuous execution of events.
    """
    print_header()
    attack_count = 0
    
    try:
        while True:
            attack_count += 1
            current_attack = random.choice(ATTACK_TYPES)
            
            severity_map = {"ALACSONY": 1, "KÖZEPES": 3, "MAGAS": 7, "KRITIKUS": 10}
            threat_score = severity_map[current_attack['severity']]
            
            print(f"\n--- INCIDENS / INCIDENT #{attack_count} ---")
            print(f"Aktuális hálózati stressz-szint: {draw_threat_meter(threat_score)}")
            
            simulate_attack(current_attack)
            deploy_defense(current_attack)
            
            print("\n\033[90m[Várakozás a következő ciklusra... Megszakítás: CTRL+C]\033[0m")
            print("-" * 70)
            time.sleep(3)
            
    except KeyboardInterrupt:
        # HU: Ctrl+C nyomásakor a statisztikai modul zárja a programot
        # EN: When Ctrl+C is pressed, the statistical module closes the program
        print_final_statistics()

if __name__ == "__main__":
    system_dashboard()
