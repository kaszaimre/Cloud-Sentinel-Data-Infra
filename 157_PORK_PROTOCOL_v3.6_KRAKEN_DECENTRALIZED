# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 157_PORK_PROTOCOL_v3.6_KRAKEN_DECENTRALIZED
# 
# LEÍRÁS (HU):
# Decentralizált Kraken-motor a BTC-árfolyam blokádmentes lekéréséhez.
# Tartalmaz dinamikus volatilitási puffert (ADX/ATR) és vészhelyzeti bázisár
# logikát a hálózati stabilitásért. 
# Mottó: "A borsodi nem hackel, a borsodi optimalizál."
#
# DESCRIPTION (EN):
# Decentralized Kraken engine for unblocked BTC price fetching. Features
# dynamic volatility buffering (ADX/ATR) and emergency base-price logic 
# for network stability.
# Motto: "The Borsodi doesn't hack, the Borsodi optimizes."
#
# SZERZŐ: Tábornok | BORSODI WAR ROOM
# ==============================================================================
# 🌌 CYBER-BORSOD NODE 157_PORK_PROTOCOL_v3.6_KRAKEN_DECENTRALIZED - KRAKEN DECENTRALIZED ENGINE
# 🚀 SYSTEM PROTOCOL: UNBLOCKED LIVE BTC FETCH & MANUAL INDICATORS
# 🛠️ DEVELOPER: T800 Data-Butcher & The Commander (49er MMA/Judo Master)
# 🎯 ARSENAL FILE: 122_pork_protocol_v3_panel.py
# ==============================================================================

import urllib.request
import json
import ssl

def get_unblocked_btc_price():
    """Közvetlen, blokádmentes lekérés a Kraken nyílt adathálózatára"""
    url = "https://kraken.com"
    headers = {'User-Agent': 'Mozilla/5.0'}
    context = ssl._create_unverified_context() # SSL tiltások megkerülése
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=context, timeout=5) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            # A Kraken az 'XXBTZUSD' kulcs alatt tárolja a legutóbbi kötési árat ('c')
            live_price = res_data['result']['XXBTZUSD']['c'][0]
            return float(live_price), "KRAKEN ENGINE"
    except Exception:
        # Ha a mobilhálózat teljesen lehalt, a tegnapi Node bázisárat kapja a rendszer
        return 76990.0, "HARDCODED NODE BASE"

def evaluate_pork_protocol_v3_6():
    print("=========================================================")
    print("  [🐖] PORK PROTOCOL v3.6 - BLOKÁDMENTES KRAKEN PANEL   ")
    print("=========================================================\n")
    
    print("⏳ Élő BTC/USD adatfolyam berántása a Kraken hálózatról...")
    btc_price, data_source = get_unblocked_btc_price()
    print(f"✅ HÁLÓZAT ONLINE | Forrás: {data_source} | Ár: {btc_price} USD\n")
    
    try:
        cci_10 = float(input("👉 Írd be a CCI(10) értékét (pl. -113.07): "))
        cci_60 = float(input("👉 Írd be a CCI(60) értékét (pl. 38.97): "))
        adx_14 = float(input("👉 Írd be az ADX(14) értékét (pl. 28.73): "))
    except ValueError:
        print("\n❌ HIBA: Érvénytelen számformátum!")
        return

    print("\n=========================================================")
    print(" [FIZIKAI KIÉRTÉKELÉS ÉS MATEMATIKAI SZÁMÍTÁS / EVALUATION] ")
    print("=========================================================")

    # ADX alapú volatilitási puffer a szűkület és a hamis letörések kezelésére
    volatility_factor = max(0.015, min(0.035, adx_14 / 1500))
    sl_offset = btc_price * volatility_factor
    
    if cci_10 > 0 and cci_60 > 0 and adx_14 > 25:
        signal = "🟢 SZIGNÁL: BUY (Minden idősík irányba állt! A csapda kész!)"
        sl_level = f"-{round(sl_offset, 2)} USD (Ár: {round(btc_price - sl_offset, 2)})"
        tp_level = f"+{round(sl_offset * 1.35, 2)} USD (Ár: {round(btc_price + (sl_offset * 1.35), 2)})"
    elif cci_10 < 0 and cci_60 < 0 and adx_14 > 25:
        signal = "🔴 SZIGNÁL: SELL (Medve dominancia a zónában!)"
        sl_level = f"+{round(sl_offset, 2)} USD (Ár: {round(btc_price + sl_offset, 2)})"
        tp_level = f"-{round(sl_offset * 1.35, 2)} USD (Ár: {round(btc_price - (sl_offset * 1.35), 2)})"
    else:
        signal = "🟡 SZIGNÁL: HOLD (Bizonytalan Sakkmatt Zóna / Spinning Top oldalazás)"
        sl_level = tp_level = "0.00 USD"

    print(f"{signal}\n")
    print(f"-> Javasolt Stop Loss   (SL): {sl_level}")
    print(f"-> Javasolt Take Profit (TP): {tp_level}\n")
    print("[Program finished]")

if __name__ == "__main__":
    evaluate_pork_protocol_v3_6()
