#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
# PROJEKT: 139_RAKOSCSABA_LIVE_MONITOR_v1.0
# LEÍRÁS: ÉLŐ BTC monitor a bázishoz, beépített SSL bypass-szal.
# ==============================================================================
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
# PROJEKT: 139_RAKOSCSABA_LIVE_MONITOR_v1.0
# 
# LEÍRÁS (HU):
# Valós idejű Bitcoin árfolyam-figyelő modul a Rákoscsaba Bázis számára. 
# Beépített SSL-bypass áramkörrel biztosítja a zavartalan kapcsolatot az 
# API-val, kikerülve a mobil/Termux környezetben gyakori tanúsítvány-hibákat.
# A radar lüktetése jelzi a hálózat és az adatfolyam integritását.
#
# DESCRIPTION (EN):
# Real-time Bitcoin price monitoring module for the Rákoscsaba Base. 
# Features an embedded SSL-bypass circuit to ensure a seamless connection 
# with the API, bypassing common certificate errors in mobile/Termux 
# environments. The "radar pulse" confirms network and data stream integrity.
#
# SZERZŐ: Tábornok | BORSODI WAR ROOM
# ==============================================================================

import urllib.request
import json
import ssl

def get_live_btc():
    try:
        # SSL bypass a mobil/Termux környezethez
        context = ssl._create_unverified_context()
        url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, context=context, timeout=5) as response:
            data = json.loads(response.read().decode())
            return float(data['data']['amount'])
    except Exception as e:
        print(f"[DEBUG] Radar hiba: {e}")
        return None

print("--- RÁKOSCSABA BÁZIS | ÉLŐ MONITOR v1.0 ---")
live_price = get_live_btc()

if live_price:
    formatted_price = f"{live_price:,.2f}".replace(",", " ")
    print(f"[ÉLŐ MONITOR] -> Bitcoin: {formatted_price} USD")
    print("STATUS: A radar lüktet. Az adatok valósak!")
else:
    print("HIBA: A maffia-szerverek blokkolják a hálózatot, vagy nincs net!")
