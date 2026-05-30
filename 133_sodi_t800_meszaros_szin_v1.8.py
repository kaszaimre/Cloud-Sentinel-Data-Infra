# ==============================================================================
# PROJEKT: SODI T-800 - RADAR-MÉSZÁROS SZÍN (v1.8 - KIBER-BORSOD EDITION)
# LEÍRÁS: Ágyból dög lős, ultra-magyarosított kvantitatív terminál.
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

# ----------------------------------------------------------------------
# KIBER-BORSODI HÍRCSATORNA (100% HAZAI LIKVIDITÁS)
# ----------------------------------------------------------------------
MULL_NEWS = [
    "🔥 LÖLÖ ALERT: Megvették a teljes blokkláncot tokkal-vonóval, épül a kiber-stadion!",
    "🚀 SZALONNA PUMP: Kilőtt a Parázs Ív, a Hüle Juserek pánikszerűen vásárolnak!",
    "📈 BORSOD POWER: Megérkezett a Kiber-Borsodi Likviditás, a padló végleg fixálva!"
]

MEAR_NEWS = [
    "📉 PARÁZS RECOIL: Elbújt a nap a szalonna elől, a Bollinger szalagok elszakadtak!",
    "🛑 RADAR WARNING: A T-800-as radar szerint a likviditást átcsoportosították alapozóba.",
    "😭 JUSER SÍRÁS: A Hüle Juser véletlenül shortolta a Mészáros Színt, bukta a gulyásleves árát."
]

def cyber_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def cyber_loading(text, duration=2):
    sys.stdout.write(text)
    sys.stdout.flush()
    for _ in range(duration):
        time.sleep(0.3)
        sys.stdout.write(GREEN + "🔵" + RESET)
        sys.stdout.flush()
    print()

def calculate_cci(prices):
    atlag = sum(prices) / len(prices)
    mad = sum(abs(p - atlag) for p in prices) / len(prices)
    if mad == 0: return 0
    return (prices[-1] - atlag) / (0.015 * mad)

def calculate_adx_strength(prices):
    up_moves = 0
    down_moves = 0
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        if diff > 0: up_moves += diff
        elif diff < 0: down_moves += abs(diff)
    total_move = up_moves + down_moves
    if total_move == 0: return 0
    return (abs(up_moves - down_moves) / total_move) * 100

def inditas():
    global usd_balance, crypto_balance
    
    print("\n" + RED + "!"*30)
    cyber_print("!!! KIBER-BORSODI JOGI DUMA !!!", 0.02)
    cyber_print("Ez egy OKTATÁSI SEGÉDESZKÖZ. Ha elbukod a pénzed, Lölö nem fizeti vissza!", 0.02)
    print("!"*30 + RESET)
    input("\n[A padló fixálva - Enter az indításhoz]")
    
    while True:
        print("\n" + CYAN + "========================================")
        cyber_print("    SODI T-800 - RADAR-MÉSZÁROS SZÍN    ", 0.02)
        cyber_print("    [HUROK: KIBER-BORSODI LIKVIDITÁS]   ", 0.02)
        print("========================================" + RESET)
        
        print(f"💰 TÁRCA | USD: {usd_balance:.2f} | CRYPTO: {crypto_balance:.4f}")
        print("-" * 40)

        prices = []
        valasztas = input("Kézi adatok [k] vagy Auto-Mészáros Generátor [g]? ").lower()
        
        if valasztas == 'g':
            aktualis_ar = random.uniform(60000, 90000)
            cyber_print(GREEN + "\n[!] Mészáros Szín generálása..." + RESET, 0.02)
            for i in range(1, 11):
                valtozas = random.uniform(-0.04, 0.04)
                aktualis_ar = aktualis_ar * (1 + valtozas)
                prices.append(round(aktualis_ar, 2))
                print(f"[{i}/10] Parázs Ív szint: {prices[-1]:10.2f} BTC/USD")
        else:
            print("\n[+] Írd be a 10 árat:")
            for i in range(1, 11):
                while True:
                    try:
                        ar = input(f"[{i}/10] Ár: ")
                        prices.append(float(ar))
                        break
                    except ValueError:
                        print(RED + "Hüle Juser! Csak számot!" + RESET)

        print()
        cyber_loading("[!] Bollinger bogyók pörgetése ")
        
        atlag = sum(prices) / 10
        utolso = prices[-1]
        lendulet = (prices[-1] - prices[-4]) / 3
        joslat = utolso + lendulet
        cci_ertek = calculate_cci(prices)
        adx_ertek = calculate_adx_strength(prices)

        # Hírfolyam kiírása a matek alapján
        print("-" * 40)
        if joslat > utolso:
            print(GREEN + random.choice(MULL_NEWS) + RESET)
        else:
            print(RED + random.choice(MEAR_NEWS) + RESET)
        print("-" * 40)
        time.sleep(1.5)

        # Pánik-mérő hanggal
        volatilitas = max(prices) - min(prices)
        if volatilitas > (atlag * 0.05):
            riziko_szines = RED + "!!! VESZÉLY: HÜLE JUSER MEZŐ !!!" + RESET
            sys.stdout.write("\a")
            sys.stdout.flush()
        elif volatilitas > (atlag * 0.02):
            riziko_szines = YELLOW + "KÖZEPES (SZALONNA FÁZIS)" + RESET
        else:
            riziko_szines = GREEN + "PADLÓ FIXÁLVA (STABIL)" + RESET

        # Grafikon rajzolás egyedi bogyókkal
        min_p = min(min(prices), joslat)
        max_p = max(max(prices), joslat)
        print("\n--- BTC/USD PARÁZS ÍV ---")
        for idx, p in enumerate(prices):
            hossz = int(((p - min_p) / (max_p - min_p + 0.0001)) * 15)
            print(f"{idx+1:2d}.: {p:10.2f} |" + CYAN + f"{'🔵' * hossz}" + RESET)

        hossz_j = int(((joslat - min_p) / (max_p - min_p + 0.0001)) * 15)
        print(f"11.: {joslat:10.2f} |" + YELLOW + f"{'🔴' * hossz_j}" + RESET + " <-- JÖVŐ TIPP")

        # Szűrés
        is_trending = adx_ertek > 25
        if joslat > utolso and cci_ertek < 150 and is_trending:
            final_direction = "BUY"
            trend_szines = GREEN + "MÉSZÁROS SZÍN: ZÖLD (BUY)" + RESET
        elif joslat <= utolso or cci_ertek > 150:
            final_direction = "SELL"
            trend_szines = RED + "MÉSZÁROS SZÍN: PIROS (SELL)" + RESET
        else:
            final_direction = "HOLD"
            trend_szines = YELLOW + "LIKVDIITÁS VÁRAKOZÁS (HOLD)" + RESET

        print("-" * 40)
        print(f"CCI: {cci_ertek:+.2f} | KIBER-BORSODI ADX: {adx_ertek:.1f}%")
        print(f"Radar állapot:    {riziko_szines}")
        print(f"FŐ JELZÉS:        {trend_szines}")
        print("-" * 40)

        # Szimulált Kereskedés
        if final_direction == "BUY":
            if usd_balance > 0:
                vett_mennyiseg = usd_balance / utolso
                crypto_balance += vett_mennyiseg
                usd_balance = 0.0
                print(GREEN + f"🛒 LÖLÖ VETT NEKED KRIPTÓT!" + RESET)
        elif final_direction == "SELL":
            if crypto_balance > 0:
                usd_balance += crypto_balance * utolso
                crypto_balance = 0.0
                print(RED + f"💰 PROFIT BEFIXÁLVA A ZSEBBEN!" + RESET)
        else:
            print(YELLOW + "⏳ HÜLE JUSER VÁRAKOZIK..." + RESET)

        szamla_ertek = usd_balance + (crypto_balance * utolso)
        print(f"📈 NET VAGYON: {szamla_ertek:.2f} USD")
        print("-" * 40)

        valasz = input("\nÚjabb Borsodi Hurok? (i/n): ").lower()
        if valasz != 'i':
            print("\n" + GREEN + "Vigyázz a szalonnára, Tábornok! Leállás..." + RESET)
            break

if __name__ == "__main__":
    inditas()
