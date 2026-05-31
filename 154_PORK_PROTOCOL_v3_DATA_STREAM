# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 154_PORK_PROTOCOL_v3_DATA_STREAM
# 
# LEÍRÁS (HU):
# Beépített adatfolyam-kezelő modul a Pork Protocol számára. Külső könyvtárak
# nélkül, közvetlen csatornán keresztül biztosítja a BTC élő árfolyamát.
# Mottó: "A borsodi nem hackel, a borsodi optimalizál."
#
# DESCRIPTION (EN):
# Built-in data stream module for the Pork Protocol. Ensures real-time BTC 
# pricing via a direct channel, without the need for external libraries.
# Motto: "The Borsodi doesn't hack, the Borsodi optimizes."
#
# SZERZŐ: Tábornok | BORSODI WAR ROOM
# ==============================================================================

import urllib.request
import json

# -*- coding: utf-8 -*-
# [PORK PROTOCOL v3] BEÉPÍTETT ADATFOLYAM - KÜLSŐ TELEPÍTÉS NÉLKÜL
import urllib.request
import json

def get_live_btc_price():
    print("[🚀 SYSTEM]: Élő adatok lekérése a beépített motorral...")
    url = "https://binance.com"
    
    try:
        # A gyári urllib használata a requests helyett
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            price = float(data['price'])
            print(f"🟢 SIKER: Az élő BTCUSD árfolyam: {price:,.2f} USD")
            
    except Exception as e:
        print(f"❌ Kapcsolódási hiba: {e}")

if __name__ == "__main__":
    get_live_btc_price()
    print("[Program finished]")
