# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 085_POSITION_SIZE_RISK_MULTIPLIER
# 
module_desc = """ 
LEÍRÁS (HU):

Pozícióméret-számító és kockázati szorzó modul (Risk Position Sizer).
A Phoenix Master Oracle v5.1 tőkebiztonsági modulja. A számlaegyenleg, 
a megengedett maximális kockázat (%) és a T800 Hybrid Shield Stop-Loss távolság 
alapján tűpontosan meghatározza a maximális kereskedési lotméretet.
Mottó: A borsodi nem hackel, a borsodi optimalizál.

DESCRIPTION (EN):

Position sizing and risk multiplier module (Risk Position Sizer).
The capital security module of the Phoenix Master Oracle v5.1. Based on account 
balance, maximum allowed risk (%), and the T800 Hybrid Shield Stop-Loss distance, 
it precisely determines the maximum trading lot size.
Motto: The Borsodi doesn't hack, the Borsodi optimizes.

SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM """
# ==============================================================================

import time
from datetime import datetime

def calculate_position_size(balance, risk_percent, sl_distance_usd):
    """
    Tiszta logikájú pozícióméret-számító képlet.
    Kockáztatott összeg = Egyenleg * (Kockázat% / 100)
    Lot méret = Kockáztatott összeg / Stop-Loss távolság
    """
    if sl_distance_usd <= 0:
        return 0.0, 0.0
        
    allowed_risk_usd = balance * (risk_percent / 100.0)
    
    # Kiszámoljuk a maximális lot/kontraktus méretet
    max_position_size = allowed_risk_usd / sl_distance_usd
    
    return max_position_size, allowed_risk_usd

if __name__ == "__main__":
    print("=== 085_position_size_risk_multiplier INDÍTÁSA ===")
    time.sleep(0.5)
    
    # Teszt környezet: A korábbi MT5 fotódon szereplő adatok alapulvételével
    my_balance = 10000.00         # $10k Demó tőke
    max_risk_pct = 2.0            # Szigorú 2% maximális kockázat egy kötésre
    
    # A 080-as T800 Hybrid Shield által számolt korábbi biztonsági távolság ($2,231.50)
    t800_sl_distance = 2231.50
    
    lot_size, risk_usd = calculate_position_size(my_balance, max_risk_pct, t800_sl_distance)
    
    print(f"\n[RISK MULTIPLIER REPORT] [{datetime.now().strftime('%H:%M:%S')}]")
    print(f"-> Számla egyenleg:     ${my_balance:,.2f}")
    print(f"-> Beállított Kockázat:  {max_risk_pct}% (${risk_usd:,.2f})")
    print(f"-> T800 SL Távolság:     ${t800_sl_distance:,.2f}")
    print("-" * 55)
    print(f"-> ENGEDÉLYEZETT MÉRET:  {lot_size:.4f} BTC / LOT")
    print("-> Kockázati szűrő:     [🟢 SAFE POSITION SIZE CALCULATED]")
    
    print("\n[✓] A 085-es modul sikeresen lefutott, a 85-ös luk betömve.")
