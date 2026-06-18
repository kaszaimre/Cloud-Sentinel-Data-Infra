# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 081_EMA_9_21_FIRST_STRIKE_SCANNER
# 
module_desc = """ 
LEÍRÁS (HU):

EMA 9 és EMA 21 mozgóátlag alapú First Strike trendszkenner modul.
A Phoenix Master Oracle v5.1 elsődleges belépési szűrője. Figyeli az árakat, 
és azonnali vételi (LONG) vagy eladási (SHORT) jelzést generál, amint 
a gyors és lassú átlagok keresztezik egymást.
Mottó: A borsodi nem hackel, a borsodi optimalizál.

DESCRIPTION (EN):

EMA 9 and EMA 21 moving average-based First Strike trend scanner module.
The primary entry filter of the Phoenix Master Oracle v5.1. Monitors prices 
and generates immediate buy (LONG) or sell (SHORT) signals as soon as 
the fast and slow averages cross each other.
Motto: The Borsodi doesn't hack, the Borsodi optimizes.

SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM """
# ==============================================================================

import time
from datetime import datetime

def scan_first_strike(ticker, current_price, ema_9, ema_21, previous_ema_9, previous_ema_21):
    """
    Tiszta logikájú mozgóátlag keresztezés-detektáló motor.
    """
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [SCANNER] {ticker} átvilágítása folyamatban...")
    time.sleep(0.4)
    
    # Kereszteződés logika (Gyors átlag alulról felfelé metszi a lassút)
    bullish_cross = (previous_ema_9 <= previous_ema_21) and (ema_9 > ema_21)
    # Kereszteződés logika (Gyors átlag felülről lefelé metszi a lassút)
    bearish_cross = (previous_ema_9 >= previous_ema_21) and (ema_9 < ema_21)
    
    if bullish_cross:
        return "🟢 [SIGNAL] [FIRST_STRIKE] LONG VÉTELI JELZÉS! Momentum: AKTÍV"
    elif bearish_cross:
        return "🔴 [SIGNAL] [FIRST_STRIKE] SHORT ELADÁSI JELZÉS! Momentum: REVERSED"
    else:
        # Ha nincs kereszteződés, megnézzük, hogy az ár az átlagok felett van-e
        if current_price > btc_ema_9:
            return "🟡 [STATUS] SCANNING... Trend: EMELKEDŐ (Nincs új kereszteződés)"
        else:
            return "🟡 [STATUS] SCANNING... Trend: CSÖKKENŐ (Nincs új kereszteződés)"

if __name__ == "__main__":
    print("=== 081_ema_9_21_first_strike_scanner INDÍTÁSA ===")
    time.sleep(0.5)
    
    # Teszt környezet: A korábbi dashboard fotódról vett pontos adatok szimulációja (Bitcoin)
    target_asset = "BTC-USD"
    btc_price = 108450.00
    
    # Aktuális és előző gyertya értékei a tiszta trendvizsgálathoz
    btc_ema_9 = 108018.60
    btc_ema_21 = 106189.07
    
    prev_btc_ema_9 = 105800.00
    prev_btc_ema_21 = 105950.00  # Az előző gyertyánál még a 21-es volt felül!
    
    signal_output = scan_first_strike(
        ticker=target_asset,
        current_price=btc_price,
        ema_9=btc_ema_9,
        ema_21=btc_ema_21,
        previous_ema_9=prev_btc_ema_9,
        previous_ema_21=prev_btc_ema_21
    )
    
    print(f"\n[SCANNER OUTPUT] [{datetime.now().strftime('%H:%M:%S')}]")
    print(f"-> Eszköz:            {target_asset}")
    print(f"-> Aktuális EMA 9:    ${btc_ema_9:,.2f}")
    print(f"-> Aktuális EMA 21:   ${btc_ema_21:,.2f}")
    print("-" * 55)
    print(f"-> Rendszerüzenet:    {signal_output}")
    print("-> Rendszerállapot:   [✓] SCANNING ENGINE RUNNING OPERATIONAL")
    
    print("\n[✓] A 081-es modul sikeresen lefutott, a 81-es luk betömve.")
