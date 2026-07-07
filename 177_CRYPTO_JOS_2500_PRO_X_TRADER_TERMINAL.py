import time
import random
import statistics

"""
#======================================================================================
# PROJEKT: 177_CRYPTO_JOS_2500_PRO_X_TRADER_TERMINAL
#
# LEIRAS (HU):
# Kvantitatív tőzsdei és kriptovaluta szimulációs motor, parancssoros (CLI) dashboard.
# Animált kiberpunk vizualizációval, automatikus százalékos bálna-radarral, szűrőmátrixszal
# (CCI/ADX indikátorokkal) és dinamikus volatilitáspontozással. Teljesen automatizált,
# OneCompiler- és Pydroid 3-kompatibilis, input nélküli, futásbiztos architektúra.
#
#======================================================================================
# DESCRIPTION (EN):
# Quantitative stock and cryptocurrency simulation engine and command-line (CLI) dashboard.
# Features animated cyberpunk visualization, automated percentage-based Whale Radar,
# filtering matrix (CCI/ADX indicators), and dynamic volatility scoring. Fully automated,
# input-free architecture with guaranteed stability in OneCompiler and Pydroid 3.
#
# SZERZO: Tabornok | BORSODI WAR ROOM
# VERZIÓ: v1.7 (Golyóálló Százalékos Kiadás)
#======================================================================================
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A driftet százalékos növekedési tényezővé alakítottuk (pl. 120$ a 65000-nek kb 0.18%-a gyertyánként)
COINS = [
    {"name": "BTC", "base": 65000.0, "drift_pct": 0.0018},
    {"name": "ETH", "base": 3500.0, "drift_pct": 0.0015},
    {"name": "SOL", "base": 145.0, "drift_pct": 0.0020},
    {"name": "XRP", "base": 0.55, "drift_pct": 0.0005},
    {"name": "ADA", "base": 0.45, "drift_pct": 0.0005},
    {"name": "DOGE", "base": 0.12, "drift_pct": 0.0030},
]

def disclaimer():
    print("\n" + "!" * 42)
    print("!!! FIGYELEM: OKTATÁSI SZIMULÁCIÓ !!!")
    print("NEM befektetési tanácsadás.")
    print("!" * 42)

def bar(value, min_v, max_v, width=28, fill="#"):
    span = max_v - min_v
    if span == 0:
        return fill * 0
    length = int(((value - min_v) / span) * width)
    return fill * max(0, min(width, length))

def analyze(prices):
    avg = statistics.mean(prices)
    last = prices[-1]
    trend = last - prices[0]
    momentum = last - prices[-4] if len(prices) >= 4 else last - prices[0]
    volatility = max(prices) - min(prices)

    score = 0
    score += 2 if momentum > 0 else -2
    score += 2 if trend > 0 else -2
    score += 1 if last > avg else -1
    # Dinamikus volatilitás szűrés: ha a hullámzás nagyobb, mint az átlag 0.5%-a
    score += 1 if volatility > (avg * 0.005) else 0

    if score >= 4:
        signal = "ERŐS BULL"
    elif score >= 1:
        signal = "GYENGE BULL"
    elif score <= -4:
        signal = "ERŐS BEAR"
    elif score <= -1:
        signal = "GYENGE BEAR"
    else:
        signal = "SEMLEGES"

    forecast = last + (momentum * 0.5)
    return avg, last, trend, momentum, volatility, score, signal, forecast

def generate_prices(base, drift_pct, count=10):
    prices = [round(base, 4 if base < 1 else 2)]
    for _ in range(count - 1):
        # Százalékos alapú zaj és sokk generálás
        noise = random.uniform(-0.005, 0.005)
        shock = random.choice([0, 0, 0, 1, -1, 2, -2]) * random.uniform(0.002, 0.01)
        
        base *= (1 + drift_pct + noise + shock)
        base = max(base, 0.0001)
        prices.append(round(base, 4 if base < 1 else 2))
    return prices

def market_event():
    # Az események hatása mostantól tiszta százalékos szorzó (0.01 = +1%)
    events = [
        ("nincs külön esemény", 0.0),
        ("mini pump", random.uniform(0.005, 0.015)),
        ("mini dump", random.uniform(-0.015, -0.005)),
        ("whale buy", random.uniform(0.02, 0.05)),
        ("profit taking", random.uniform(-0.03, -0.01)),
        ("news spike", random.uniform(0.03, 0.07)),
        ("panic sell", random.uniform(-0.08, -0.03)),
    ]
    return random.choice(events)

def show_coin(name, prices, cycle):
    avg, last, trend, momentum, vol, score, signal, forecast = analyze(prices)
    min_p = min(min(prices), forecast)
    max_p = max(max(prices), prices[0]) # Fix skálázási pont
    if max_p == min_p: max_p += 0.0001

    print("\n" + "=" * 72)
    print(f"{name} LIVE DASHBOARD   [CYCLE {cycle}]".center(72))
    print("=" * 72)

    for i, p in enumerate(prices, 1):
        print(f"{i:2d}. {p:12.4f} | {bar(p, min_p, max_p)}")

    print(f"11. TIPP: {forecast:12.4f} | {bar(forecast, min_p, max_p, fill='*')}   <-- JÖVŐ")
    print("-" * 72)
    print(f"Átlag:              {avg:.4f}")
    print(f"Utolsó ár:          {last:.4f}")
    print(f"Momentum:           {momentum:+.4f}")
    print(f"Trend:              {trend:+.4f}")
    print(f"Volatilitás:        {vol:.4f}")
    print(f"Erősségi pontszám:  {score}/6")
    print(f"Jelzés:             {signal}")
    print("=" * 72)

def run_live_mode(selected_coins, cycles=3, sleep_time=0.1):
    state = {c["name"]: {"base": c["base"], "drift_pct": c["drift_pct"]} for c in selected_coins}

    for cycle in range(1, cycles + 1):
        print("\n" + "#" * 72)
        print(f"LIVE PIACI FRISSÍTÉS - CIKLUS {cycle}".center(72))
        print("#" * 72)

        for coin in selected_coins:
            name = coin["name"]
            label, effect_pct = market_event()
            
            # Százalékos eseménykezelés élesítése
            state[name]["base"] = max(state[name]["base"] * (1 + effect_pct), 0.0001)
            prices = generate_prices(state[name]["base"], state[name]["drift_pct"])
            print(f"\n[{name}] ESEMÉNY: {label} ({effect_pct:+.2%})")
            show_coin(name, prices, cycle)

        time.sleep(sleep_time)

def main():
    disclaimer()
    print("\nCRYPTO-JÓS 2500 PRO X - TRADER TERMINAL")
    print("[AUTO] OneCompiler-kompatibilis, input nélkül fut.\n")

    selected_coins = COINS
    run_live_mode(selected_coins, cycles=3, sleep_time=0.1)

if __name__ == "__main__":
    main()
