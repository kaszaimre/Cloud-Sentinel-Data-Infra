# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 0017_MARKET_DEPTH_ORDERBOOK_ANALYZER.py
# 
module_desc = """ 
LEÍRÁS (HU):

Piaci ajánlati könyv (Orderbook) mélység-elemző modul.
Kiszámítja a vételi és eladási oldali likviditási falak arányát (Imbalance).
Segít a Phoenix Master Oracle-nek észlelni, ha a bálnák mesterséges falakkal 
próbálják manipulálni a Bitcoin vagy a részvények árfolyamát.
Mottó: A borsodi nem hackel, a borsodi optimalizál.

DESCRIPTION (EN):

Market depth and orderbook analyzer module.
Calculates the ratio of buy and sell side liquidity walls (Imbalance).
Helps the Phoenix Master Oracle detect when whales try to manipulate 
the price of Bitcoin or stocks using artificial order walls.
Motto: The Borsodi doesn't hack, the Borsodi optimizes.

SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM """
# ==============================================================================

import time
from datetime import datetime

def analyze_orderbook_imbalance(total_bids_volume, total_asks_volume):
    """
    Kiszámítja az ajánlati könyv egyensúlyhiányát (Imbalance %).
    Ha az érték pozitív, a vevők erősebbek, ha negatív, az eladók nyomnak.
    """
    total_volume = total_bids_volume + total_asks_volume
    if total_volume == 0:
        return 0.0
    
    # Tiszta logikai képlet az imbalance meghatározására
    imbalance = ((total_bids_volume - total_asks_volume) / total_volume) * 100
    return imbalance

if __name__ == "__main__":
    print("=== 017_market_depth_orderbook_analyzer INDÍTÁSA ===")
    time.sleep(0.5)
    
    # Teszt adatok: szimulálunk egy komoly vételi falat a Bitcoin piacán
    # (Pl. a bálnák \$104,000-nél bepakoltak egy hatalmas vételi blokkot)
    simulated_bids = 1450.50  # Vételi ajánlatok volumene (BTC)
    simulated_asks = 820.25   # Eladási ajánlatok volumene (BTC)
    
    imbalance_pct = analyze_orderbook_imbalance(simulated_bids, simulated_asks)
    
    print(f"\n[ORDERBOOK ANALYSIS] [{datetime.now().strftime('%H:%M:%S')}]")
    print(f"-> Regisztrált Vételi Fal (Bids): {simulated_bids} BTC")
    print(f"-> Regisztrált Eladási Fal (Asks): {simulated_asks} BTC")
    print(f"-> Piaci Imbalance Index:        {imbalance_pct:+.2f}%")
    
    # Phoenix Master döntési mátrix
    if imbalance_pct > 20.0:
        print("-> Oracle Értékelés: 🟢 INTENZÍV VÉTELI NYOMÁS (A bálnák tartják az aljat)")
    elif imbalance_pct < -20.0:
        print("-> Oracle Értékelés: 🔴 INTENZÍV ELADÁSI NYOMÁS (Óvatosság, letörés veszély)")
    else:
        print("-> Oracle Értékelés: 🟡 EGYENSÚLYI ÁLLAPOT (Oldalazás)")
        
    print("\n[✓] A 017-es modul sikeresen lefutott, a gap betöltve a Git-ben.")
