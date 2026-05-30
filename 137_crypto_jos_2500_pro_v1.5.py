#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
# PROJEKT: 137_CRYPTO-JÓS 2500 PRO v1.5 (PRO QUANT EDITION)
# 
# LEÍRÁS (HU):
# A Crypto-Jós sorozat 1.5-ös verziója, amely dedikáltan a kvantitatív (Quant) 
# elemzésre fókuszál. Tiszta Python implementációt használ a CCI és ADX 
# indikátorok számítására, beépített piaci feszültség-monitorral és 
# automatikus tranzakció-naplózással. Ideális eszköz a technikai trendek 
# szimulált tesztelésére és a piaci volatilitás nyomon követésére.
#
# DESCRIPTION (EN):
# Version 1.5 of the Crypto-Jós series, dedicated to quantitative (Quant) 
# analysis. It utilizes a pure Python implementation for calculating CCI and 
# ADX indicators, featuring an integrated market stress monitor and automatic 
# transaction logging. An ideal tool for testing technical trends and 
# monitoring market volatility through simulation.
#
# SZERZŐ: Tábornok | BORSODI WAR ROOM
# ==============================================================================

# ==============================================================================
# PROJEKT: CRYPTO-JÓS 2500 PRO v1.5 (PRO QUANT EDITION)
# LEÍRÁS: Retró CLI tőzsdei szimulátor beépített CCI és ADX matematikai szűrőkkel,
#         színes ANSI effektekkel, audio riasztással és TXT naplózással.
# SZERZŐ: Tábornok
# ==============================================================================

import time
import sys
import random
from datetime import datetime

RED     = "\033[1;31m"
GREEN   = "\033[1;32m"
YELLOW  = "\033[1;33m"
CYAN    = "\033[1;36m"
RESET   = "\033[0m"

usd_balance = 10000.0
crypto_balance = 0.0

def disclaimer():
    print("\n" + RED + "!"*30)
    print("!!! FIGYELEM !!!")
    print("Ez egy OKTATÁSI SEGÉDESZKÖZ és MATEMATIKAI SZIMULÁCIÓ.")
    print("NEM MINŐSÜL BEFEKTETÉSI TANÁCSADÁSNAK!")
    print("A fejlesztő NEM vállal felelősséget az anyagi veszteségekért.")
    print("Csak saját felelősségre használd!")
    print("!"*30 + RESET)
    input("\n[Értettem, elfogadom - Nyomj Entert az indításhoz]")

# ==============================================================================
# INDIKÁTOR MATEK MODULOK (Tiszta Python matematikai implementáció)
# ==============================================================================
def calculate_cci(prices):
    """Kiszámolja a Commodity Channel Indexet (CCI) az utolsó árakra"""
    atlag = sum(prices) / len(prices)
    # Átlagos eltérés (Mean Absolute Deviation) számítása
    mad = sum(abs(p - atlag) for p in prices) / len(prices)
    if mad == 0: return 0
    # CCI képlet: (Utolsó Ár - Átlag) / (0.015 * MAD)
    return (prices[-1] - atlag) / (0.015 * mad)

def calculate_adx_strength(prices):
    """Kiszámol egy trend-erősségi indexet (ADX analógia) az ármozgások iránya alapján"""
    up_moves = 0
    down_moves = 0
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        if diff > 0: up_moves += diff
        elif diff < 0: down_moves += abs(diff)
    
    total_move = up_moves + down_moves
    if total_move == 0: return 0
    # Százalékos arány, ami megmutatja mennyire egyirányú a trend (0-100 között)
    return (abs(up_moves - down_moves) / total_move) * 100

# ==============================================================================
# FŐPROGRAM
# ==============================================================================
def inditas():
    global usd_balance, crypto_balance
    disclaimer()
    
    while True:
        print("\n" + CYAN + "="*40)
        print("    CRYPTO-JÓS 2500 PRO v1.5    ")
        print("    [CCI & ADX QUANT MATRIX]    ")
        print("="*40 + RESET)
        
        print(f"💰 TÁRCA ÁLLAPOTA | USD: {usd_balance:.2f} | CRYPTO: {crypto_balance:.4f}")
        print("-" * 40)

        prices = []
        valasztas = input("Kézi árak [k] vagy Auto-Generált tőzsde [g]? ").lower()
        
        if valasztas == 'g':
            aktualis_ar = random.uniform(60000, 90000)
            print(GREEN + "\n[!] Élő tőzsdei szimuláció indítása..." + RESET)
            for i in range(1, 11):
                time.sleep(0.05)
                valtozas = random.uniform(-0.04, 0.04)  # Vadabb mozgások a teszthez
                aktualis_ar = aktualis_ar * (1 + valtozas)
                prices.append(round(aktualis_ar, 2))
                print(f"[{i}/10] Generált ár: {prices[-1]:10.2f} USD")
        else:
            print("\n[+] Kérlek, add meg a 10 darab tőzsdei árat:")
            for i in range(1, 11):
                while True:
                    try:
                        ar = input(f"[{i}/10] Kérem az árat: ")
                        prices.append(float(ar))
                        break
                    except ValueError:
                        print(RED + "Hiba! Csak számot fogadunk el." + RESET)

        print("\n[!] Kvantitatív motorok indítása (CCI & ADX)...")
        time.sleep(0.5)

        # --- INDIKÁTOROK KISZÁMÍTÁSA ---
        atlag = sum(prices) / 10
        utolso = prices[-1]
        lendulet = (prices[-1] - prices[-4]) / 3
        joslat = utolso + lendulet
        
        cci_ertek = calculate_cci(prices)
        adx_ertek = calculate_adx_strength(prices)

        # Pánik-mérő modul
        volatilitas = max(prices) - min(prices)
        if volatilitas > (atlag * 0.05):
            riziko_szines = RED + "!!! MAGAS (PÁNIK) !!!" + RESET
            riziko_txt = "MAGAS (PÁNIK)"
            sys.stdout.write("\a")
            sys.stdout.flush()
        elif volatilitas > (atlag * 0.02):
            riziko_szines = YELLOW + "KÖZEPES" + RESET
            riziko_txt = "KÖZEPES"
        else:
            riziko_szines = GREEN + "ALACSONY (STABIL)" + RESET
            riziko_txt = "ALACSONY (STABIL)"

        # 4. Vizuális Grafikon
        min_p = min(min(prices), joslat)
        max_p = max(max(prices), joslat)
        
        print("\n--- PIACI MOZGÁS ÉS JÓSLAT ---")
        for idx, p in enumerate(prices):
            hossz = int(((p - min_p) / (max_p - min_p + 0.0001)) * 20)
            print(f"{idx+1:2d}. ár: {p:10.2f} |" + CYAN + f"{'#' * hossz}" + RESET)

        hossz_j = int(((joslat - min_p) / (max_p - min_p + 0.0001)) * 20)
        print(f"11. TIPP: {joslat:10.2f} |" + YELLOW + f"{'*' * hossz_j}" + RESET + "  <-- JÖVŐ")

        # ----------------------------------------------------------------------
        # PRO SIGNAL LOGIKA (SZŰRÉS CCI ÉS ADX ALAPJÁN)
        # ----------------------------------------------------------------------
        # Erős a trend, ha az ADX > 25 (szignifikáns mozgás)
        is_trending = adx_ertek > 25
        
        # Bull jelzés: Ha a matek emelkedést mutat ÉS a CCI nem jelzi, hogy túl lenne véve (CCI < 150)
        if joslat > utolso and cci_ertek < 150 and is_trending:
            final_direction = "BUY (BULL)"
            trend_szines = GREEN + "EMELKEDÉS (BULL) [ADX OK]" + RESET
        # Bear jelzés: Ha csökkenést mutat VAGY a CCI brutálisan túlvetett zónába csapott (fordulás várható)
        elif joslat <= utolso or cci_ertek > 150:
            final_direction = "SELL (BEAR)"
            trend_szines = RED + "CSÖKKENŐ (BEAR) [SZŰRT]" + RESET
        else:
            final_direction = "HOLD (RANGE)"
            trend_szines = YELLOW + "OLDALAZÁS (WAITING) [GYENGE TREND]" + RESET

        # 5. Összegzés és Indikátor Mátrix kiírása
        cci_szin = RED if abs(cci_ertek) > 100 else GREEN
        adx_szin = GREEN if adx_ertek > 25 else YELLOW

        print("-" * 40)
        print(f"CCI ÉRTÉK:        {cci_szin}{cci_ertek:+.2f}{RESET}")
        print(f"ADX TREND ERŐ:    {adx_szin}{adx_ertek:.1f}%{RESET}")
        print(f"Piaci feszültség: {riziko_szines}")
        print(f"VÁRHATÓ IRÁNY:    {trend_szines}")
        print("-" * 40)

        # ----------------------------------------------------------------------
        # SZIMULÁLT TRADER
        # ----------------------------------------------------------------------
        trade_uzenet = ""
        if final_direction == "BUY (BULL)":
            if usd_balance > 0:
                vett_mennyiseg = usd_balance / utolso
                crypto_balance += vett_mennyiseg
                trade_uzenet = f"🛒 BUY SIGNAL: Vettél {vett_mennyiseg:.4f} egységet {utolso:.2f} áron!"
                usd_balance = 0.0
                print(GREEN + trade_uzenet + RESET)
            else:
                trade_uzenet = "📦 HOLD: Pozíció megtartva."
                print(YELLOW + trade_uzenet + RESET)
        elif final_direction == "SELL (BEAR)":
            if crypto_balance > 0:
                kapott_usd = crypto_balance * utolso
                usd_balance += kapott_usd
                trade_uzenet = f"💰 SELL SIGNAL: Eladva {utolso:.2f} áron, profit realizálva!"
                crypto_balance = 0.0
                print(RED + trade_uzenet + RESET)
            else:
                trade_uzenet = "🛡️ CASH PROTECTION: Tőke biztonságban."
                print(GREEN + trade_uzenet + RESET)
        else:
            trade_uzenet = "⏳ WAITING: Nincs tiszta szignál, várakozás."
            print(YELLOW + trade_uzenet + RESET)

        szamla_ertek = usd_balance + (crypto_balance * utolso)
        print(f"📈 NET SZÁMLAEGYENLEG: {szamla_ertek:.2f} USD")
        print("-" * 40)

        # 6. TXT Mentés
        try:
            most = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("crypto_jos_naplo.txt", "a", encoding="utf-8") as f:
                f.write(f"=== QUANT ELEMZÉS: {most} ===\n")
                f.write(f"CCI: {cci_ertek:+.2f} | ADX: {adx_ertek:.1f}%\n")
                f.write(f"Piaci feszültség: {riziko_txt} | Irány: {final_direction}\n")
                f.write(f"Tranzakció:  {trade_uzenet}\n")
                f.write(f"Vagyon:      {szamla_ertek:.2f} USD\n")
                f.write("-" * 40 + "\n\n")
        except Exception as e:
            print(RED + f"[HIBA] Mentési hiba: {e}" + RESET)

        valasz = input("\nAkarsz új elemzést? (i/n): ").lower()
        if valasz != 'i':
            print("\n" + GREEN + "Köszi, hogy használtad, Tábornok! Végső vagyon: " + YELLOW + f"{szamla_ertek:.2f} USD" + RESET)
            break

if __name__ == "__main__":
    inditas()
