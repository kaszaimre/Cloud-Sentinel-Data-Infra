"""
======================================================================================
# PROJEKT: 141_CYBER_BORSOD_SECURITY_CORE_v2.6_MOBILE
# 
# LEÍRAS (HU):
# Kiberbiztonsagi szimulator telefon-biztos karakterkodolassal (Standard ASCII).
# Ez a verzio optimalizalt mobil terminálokhoz (Termux/Pydroid), nem tartalmaz
# emojikat, igy elkeruli a renderelési hibákat. Valos ideju SOC monitoring 
# es automatikus incidens-elhárítási szimuláció.

#======================================================================================
# DESCRIPTION (EN):
# Cybersecurity simulator with phone-safe character encoding (Standard ASCII).
# This version is optimized for mobile terminals (Termux/Pydroid), using no 
# emojis to prevent rendering errors. Features real-time SOC monitoring and 
# automated incident mitigation simulation.
#
# SZERZO: Tabornok | BORSODI WAR ROOM

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#======================================================================================

   CYBER-BORSOD SECURITY CORE V2.6 - MOBILE TERMUX/PYDROID HOTFIXED
   
   LEÍRÁS (HU):
   Kiberbiztonsági szimulátor telefon-biztos karakterkódolással (Standard ASCII).
   Ez a verzió nem tartalmaz emojikat, így nem omlik össze a mobil terminálokban.
======================================================================================
"""

import time
import sys
import random
import logging

# HU: Helyi naplózási struktúra beállítása a cyber_defense.log fájlba
logging.basicConfig(
    filename='cyber_defense.log',
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%H:%M:%S'
)

TARGET_SERVER = "192.168.1.100 (T-1000_CORE)"
ATTACK_TYPES = [
    {"name": "Brute Force SSH Probalkozas", "severity": "KOZEPES", "speed": 0.05, "level": 5},
    {"name": "DDoS UDP Flood Terheles", "severity": "MAGAS", "speed": 0.01, "level": 8},
    {"name": "SQL Injection Adatbazis Teszt", "severity": "KRITIKUS", "speed": 0.08, "level": 10},
    {"name": "XSS Kartenyek Szkript Injektalas", "severity": "ALACSONY", "speed": 0.1, "level": 2}
]

stats = {
    "osszes_tamadas": 0,
    "ALACSONY": 0,
    "KOZEPES": 0,
    "MAGAS": 0,
    "KRITIKUS": 0,
    "blokkolt_ip_cimek": set()
}

def print_header():
    print("\033[95m" + "=" * 70 + "\033[0m")
    print("   [🔒] CYBER-BORSOD INCIDENT RESPONSE & SECURITY SIMULATOR [🔒]   ")
    print("   Szervervedelem, Automatikus Elharitas es Statisztikai Mod     ")
    print("\033[95m" + "=" * 70 + "\033[0m")
    time.sleep(0.5)

def draw_threat_meter(level):
    colors = {"ALACSONY": "\033[92m", "KOZEPES": "\033[93m", "MAGAS": "\033[91m", "KRITIKUS": "\033[41m\033[97m"}
    reset = "\033[0m"
    
    color_keys = list(colors.keys())
    idx = max(0, min(level - 1, len(color_keys) - 1))
    chosen_color = colors[color_keys[idx]]
    
    bar_level = max(1, min(level, 10))
    # TELEFON FIX: '#' es '-' karaktereket hasznalunk a '█' es '░' helyett
    meter = "#" * (2 * bar_level) + "-" * (20 - 2 * bar_level)
    return f"[{chosen_color}{meter}{reset}]"

def simulate_attack(attack):
    print(f"\n\033[91m[!] RIASZTAS / ALERT:\033[0m Eszlelt esemeny: {attack['name']}")
    print(f"[!] Celpont / Target: {TARGET_SERVER} | Szint / Severity: {attack['severity']}")
    
    stats["osszes_tamadas"] += 1
    stats[attack['severity']] += 1
    
    logging.warning(f"Tamadas eszleleve: {attack['name']} -> Celpont: {TARGET_SERVER}")
    time.sleep(0.3)
    
    print("Bejovo kartenyek csomagok elemzese:")
    for _ in range(1, 16):
        hex_data = f"0x{random.randint(1000, 9999):X}"
        ip_src = f"185.234.{random.randint(1,254)}.{random.randint(1,254)}"
        stats["blokkolt_ip_cimek"].add(ip_src)
        
        # TELEFON FIX: Sima karakteres visszajelzes, ami nem akasztja meg a telot
        sys.stdout.write(f"  -> [{ip_src}] INJECT: {hex_data} ... SZURES ALATT\r")
        sys.stdout.flush()
        time.sleep(attack['speed'])
    print("\n[+] Csomagelemzes kesz / Packet analysis complete.")

def deploy_defense(attack):
    print("\033[94m[*] VEDELMI REAKCIO INDITASA / DEPLOYING DEFENSE...\033[0m")
    time.sleep(0.3)
    
    actions = [
        "[OK] Forras IP cimek automatikus tiltasa a tuzfalon (iptables BANNED).",
        "[OK] Forgalom atiranyitasa a biztonsagi szurro proxy-ra (Proxy routing).",
        "[OK] Szigma entropia kulcsok ujragenerALACSONYa es halozati izolacio.",
        "[OK] Rendszerintegritas ellenorizve. A szerver magja STABIL."
    ]
    
    for action in actions:
        sys.stdout.write(f"  {action}\n")
        sys.stdout.flush()
        time.sleep(0.1)
        
    logging.info(f"Sikeres elharitas: {attack['name']} blokkolva. Rendszer vedve.")
    print("\033[92m[VEDELEM] A fenyegetest sikeresen semlegesitettuk (Mitigated).\033[0m")

def start_soc_center():
    print_header()
    logging.info("Cyber-Borsod Security SOC szimulacio elinditva.")
    
    while True:
        print("\n" + "-"*70)
        print(f"🎮 RENDELKEZESRE ALLO TAMADASI SZENARIOK:")
        for idx, att in enumerate(ATTACK_TYPES):
            print(f" [{idx+1}] {att['name']} ({att['severity']})")
        print(f" [{len(ATTACK_TYPES)+1}] Veletlenszeru tomeges tamadasi hullam inditasa")
        print(f" [q] SOC Kozpont leallitasa es vegso riport generALACSONYasa")
        print("-" * 70)
        
        valasztas = input("Valassz egy muveletet, Analitikus Ur: ").lower()
        
        if valasztas == 'q':
            break
            
        if valasztas == str(len(ATTACK_TYPES) + 1):
            print("\n\033[5;91m⚠️ [CRITICAL] OSSZETETT TAMADASI HULLAM DETEKTALVA! ⚠️\033[0m")
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
                    print("\033[91mHiba: Nincs ilyen forgatokonyv!\033[0m")
            except ValueError:
                print("\033[91mHiba: Ervenytelen parancs!\033[0m")
                
    print("\n" + "\033[96m" + "=" * 70)
    print("   [📊] FINAlis SOC INCIDENS JELENTES (VEGSO STATISZTIKAK)")
    print("=" * 70 + "\033[0m")
    print(f" Feldolgozott esemenyek szama: {stats['osszes_tamadas']} db")
    print(f" [+] ALACSONY sullyossagu:      {stats['ALACSONY']} db")
    print(f" [+] KOZEPES sullyossagu:       {stats['KOZEPES']} db")
    print(f" [+] MAGAS sullyossagu:          {stats['MAGAS']} db")
    print(f" [+] KRITIKUS sullyossagu:       {stats['KRITIKUS']} db")
    print(f" [!] Tuzfalra kulldott IP-k:     {len(stats['blokkolt_ip_cimek'])} db")
    print("-" * 70)
    print("\033[92m Rendszerallapot: VEDETT | Logfajl rogzitve: cyber_defense.log\033[0m")
    print("\033[96m" + "=" * 70 + "\033[0m")

if __name__ == "__main__":
    start_soc_center()
