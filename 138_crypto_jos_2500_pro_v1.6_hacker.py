# ==============================================================================
# PROJEKT: 138_CRYPTO-JÓS 2500 PRO v1.6 (HACKER TERMINAL EDITION)
# 
# LEÍRÁS (HU):
# A Crypto-Jós széria legdurvább kiadása. Animált karakterkiírással, 
# hacker-stílusú töltési folyamatokkal és kvantitatív CCI/ADX szűrőkkel. 
# A terminál nem csak számol, hanem "beszél" az operátorral. 
# A Bunker hivatalos szimulációs eszköze.
#
# DESCRIPTION (EN):
# The ultimate edition of the Crypto-Jós series. Features animated typing, 
# hacker-style loading sequences, and quantitative CCI/ADX filters. The 
# terminal doesn't just calculate; it communicates with the operator. 
# The official simulation tool of the Bunker.
#
# SZERZŐ: Tábornok | BORSODI WAR ROOM
# ==============================================================================

# ==============================================================================
# PROJEKT: CRYPTO-JÓS 2500 PRO v1.6 (HACKER TEXT EFFECT EDITION)
# LEÍRÁS: Retró CLI tőzsdei szimulátor animált karakterkiírással,
#         CCI/ADX mátrixszal, hanggal és automatikus naplózással.
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

# ==============================================================================
# HACKER EFFEKT: cyber_print() és cyber_delay()
# LEÍRÁS: Ez a modul felel az animált, karakterenkénti kiírásért és a 
#         retro stílusú töltési effektekért.
# ==============================================================================
def cyber_print(text, delay=0.01):
    """Karakterenként gépeli ki a szöveget a terminálba, mint a régi gépek"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() # Sorvége jel

def cyber_loading(text, duration=3):
    """Animált folyamatjelző pontokat rajzol ki a marketing szünethez"""
    sys.stdout.write(text)
    sys.stdout.flush()
    for _ in range(duration):
        time.sleep(0.4)
        sys.stdout.write(CYAN + "." + RESET)
        sys.stdout.flush()
    print()

# ==============================================================================
# INDIKÁTOR MATEK MODULOK
# ==============================================================================
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

# ==============================================================================
# FŐPROGRAM
# ==============================================================================
def inditas():
    global usd_balance, crypto_balance
    
    # Animált jogi nyilatkozat pirosan
    print("\n" + RED + "!"*30)
    cyber_print("!!! FIGYELEM !!!", 0.03)
    cyber_print("Ez egy OKTATÁSI SEGÉDESZKÖZ és MATEMATIKAI SZIMULÁCIÓ.", 0.02)
    cyber_print("NEM MINŐSÜL BEFEKTETÉSI TANÁCSADÁSNAK!", 0.02)
    cyber_print("A fejlesztő NEM vállal felelősséget az anyagi veszteségekért.", 0.02)
    cyber_print("Csak saját felelősségre használd!", 0.02)
    print("!"*30 + RESET)
    input("\n[Értettem, elfogadom - Nyomj Entert az indításhoz]")
    
    while True:
        print("\n" + CYAN + "="*40)
        cyber_print("    CRYPTO-JÓS 2500 PRO v1.6    ", 0.02)
        cyber_print("    [HACKER TERMINAL EDITION]   ", 0.02)
        print("="*40 + RESET)
        
        print(f"💰 TÁRCA ÁLLAPOTA | USD: {usd_balance:.2f} | CRYPTO: {crypto_balance:.4f}")
        print("-" * 40)

        prices = []
        valasztas = input("Kézi árak [k] vagy Auto-Generált tőzsde [g]? ").lower()
        
        if valasztas == 'g':
            aktualis_ar = random.uniform(60000, 90000)
            cyber_print(GREEN + "\n[!] Élő tőzsdei szimuláció indítása..." + RESET, 0.02)
            for i in range(1, 11):
                time.sleep(0.05)
                valtozas = random.uniform(-0.04, 0.04)
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

        # ANIMÁLT MARKETING SZÜNETEK
        print()
        cyber_loading("[!] Kvantitatív adatok dekódolása")
        cyber_loading("[!] Pánik-szint és szűrőmátrix futtatása")

        # Indikátorok számítása
        atlag = sum(prices) / 10
        utolso = prices[-1]
        lendulet = (prices[-1] - prices[-4]) / 3
        joslat = utolso + lendulet
        
        cci_ertek = calculate_cci(prices)
        adx_ertek = calculate_adx_strength(prices)

        # Pánik-mérő hanggal
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

        # Jelzés logika
        is_trending = adx_ertek > 25
        if joslat > utolso and cci_ertek < 150 and is_trending:
            final_direction = "BUY (BULL)"
            trend_szines = GREEN + "EMELKEDÉS (BULL) [ADX OK]" + RESET
        elif joslat <= utolso or cci_ertek > 150:
            final_direction = "SELL (BEAR)"
            trend_szines = RED + "CSÖKKENŐ (BEAR) [SZŰRT]" + RESET
        else:
            final_direction = "HOLD (RANGE)"
            trend_szines = YELLOW + "OLDALAZÁS (WAITING) [GYENGE TREND]" + RESET

        # 5. Összegzés animált kiírással
        cci_szin = RED if abs(cci_ertek) > 100 else GREEN
        adx_szin = GREEN if adx_ertek > 25 else YELLOW

        print("-" * 40)
        cyber_print(f"CCI ÉRTÉK:        {cci_szin}{cci_ertek:+.2f}{RESET}", 0.02)
        cyber_print(f"ADX TREND ERŐ:    {adx_szin}{adx_ertek:.1f}%{RESET}", 0.02)
        cyber_print(f"Piaci feszültség: {riziko_szines}", 0.02)
        cyber_print(f"VÁRHATÓ IRÁNY:    {trend_szines}", 0.02)
        print("-" * 40)

        # Szimulált Kereskedés
        trade_uzenet = ""
        if final_direction == "BUY (BULL)":
            if usd_balance > 0:
                vett_mennyiseg = usd_balance / utolso
                crypto_balance += vett_mennyiseg
                trade_uzenet = f"🛒 BUY SIGNAL: Vettél {vett_mennyiseg:.4f} egységet {utolso:.2f} áron!"
                usd_balance = 0.0
                cyber_print(GREEN + trade_uzenet + RESET, 0.01)
            else:
                trade_uzenet = "📦 HOLD: Pozíció megtartva."
                cyber_print(YELLOW + trade_uzenet + RESET, 0.01)
        elif final_direction == "SELL (BEAR)":
            if crypto_balance > 0:
                kapott_usd = crypto_balance * utolso
                usd_balance += kapott_usd
                trade_uzenet = f"💰 SELL SIGNAL: Eladva {utolso:.2f} áron, profit realizálva!"
                crypto_balance = 0.0
                cyber_print(RED + trade_uzenet + RESET, 0.01)
            else:
                trade_uzenet = "🛡️ CASH PROTECTION: Tőke biztonságban."
                cyber_print(GREEN + trade_uzenet + RESET, 0.01)
        else:
            trade_uzenet = "⏳ WAITING: Nincs tiszta szignál, várakozás."
            cyber_print(YELLOW + trade_uzenet + RESET, 0.01)

        szamla_ertek = usd_balance + (crypto_balance * utolso)
        cyber_print(f"📈 NET SZÁMLAEGYENLEG: {szamla_ertek:.2f} USD", 0.02)
        print("-" * 40)

        # Fájlmentés (csöndben a háttérben)
        try:
            most = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("crypto_jos_naplo.txt", "a", encoding="utf-8") as f:
                f.write(f"=== QUANT HACKER ELEMZÉS: {most} ===\n")
                f.write(f"CCI: {cci_ertek:+.2f} | ADX: {adx_ertek:.1f}%\n")
                f.write(f"Vagyon: {szamla_ertek:.2f} USD | Irány: {final_direction}\n")
                f.write("-" * 40 + "\n\n")
        except:
            pass

        valasz = input("\nAkarsz új elemzést? (i/n): ").lower()
        if valasz != 'i':
            cyber_print("\n" + GREEN + "Köszi, hogy használtad, Tábornok! Rendszer leállítása..." + RESET, 0.03)
            break

if __name__ == "__main__":
    inditas()
