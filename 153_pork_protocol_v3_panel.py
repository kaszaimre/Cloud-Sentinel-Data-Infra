# ==============================================================================
# 🌌 CYBER-BORSOD NODE 47-A: PORK PROTOCOL v3 - MANUAL TERMINAL PANEL
# 🚀 SYSTEM PROTOCOL: MARKET SIGNAL EVALUATION & RISK MANAGEMENT
# 🛠️ DEVELOPER: T800 Data-Butcher & The Commander (49er MMA/Judo Master)
# 🎯 ARSENAL FILE: 153_pork_protocol_v3_panel.py
# ==============================================================================
# [HU] LEÍRÁS: Ez a szkript bekéri az aktuális BTC árat és az indikátorok értékeit,
#      majd kíméletlen matematikai logikával kiszámítja a szignált, a javasolt
#      Stop Loss (SL) és Take Profit (TP) szinteket, valamint a Kockázat-Megtérülést.
# ------------------------------------------------------------------------------
# [EN] DESCRIPTION: This script requests the current BTC price and indicator values,
#      then calculates the market signal, suggested Stop Loss (SL), Take Profit (TP)
#      levels, and the Risk-Reward Ratio (RRR) using brutal mathematical logic.
# ==============================================================================

import os

def evaluate_pork_protocol_v3():
    # Header display / Fejléc megjelenítése
    print("=========================================================")
    print("   [🐖] PORK PROTOCOL v3 - MANUÁLIS PANEL / MANUAL PANEL   ")
    print("=========================================================\n")
    
    # 1. Data Input Stage / Adatbeviteli fázis
    try:
        btc_price = float(input("👉 Írd be az aktuális BTC árat (pl. 77986): "))
        cci_10 = float(input("👉 Írd be a CCI(10) értékét (pl. -35.79): "))
        cci_60 = float(input("👉 Írd be a CCI(60) értékét (pl. -101.07): "))
        adx_14 = float(input("👉 Írd be az ADX(14) értékét (pl. 27.69): "))
    except ValueError:
        print("\n❌ [HU] HIBA: Érvénytelen számformátum! / ERROR: Invalid number format!")
        return

    print("\n=========================================================")
    print(" [FIZIKAI KIÉRTÉKELÉS ÉS MATEMATIKAI SZÁMÍTÁS / EVALUATION] ")
    print("=========================================================")

    # 2. Signal Logic / Szignál logika
    # [HU] Ha a trend erős (ADX > 25) és a CCI indikátorok azonos irányba állnak
    # [EN] If trend is strong (ADX > 25) and CCI indicators align in the same direction
    if cci_10 > 0 and cci_60 > 0 and adx_14 > 25:
        signal = "🟢 SZIGNÁL: BUY (Minden idősík irányba állt!)"
        # Dynamic risk calculation based on volatility / Dinamikus kockázati szintek
        sl_offset = btc_price * 0.0085  # ~0.85% risk
        tp_offset = sl_offset * 1.35    # Target Risk-Reward Ratio
        sl_level = f"-{round(sl_offset, 2)} USD"
        tp_level = f"{round(tp_offset, 2)} USD"
        rrr_ratio = "1 : 1.35"
    elif cci_10 < 0 and cci_60 < 0 and adx_14 > 25:
        signal = "🔴 SZIGNÁL: SELL (Medve dominancia a zónában!)"
        sl_offset = btc_price * 0.0085
        tp_offset = sl_offset * 1.35
        sl_level = f"+{round(sl_offset, 2)} USD"
        tp_level = f"-{round(tp_offset, 2)} USD"
        rrr_ratio = "1 : 1.35"
    else:
        signal = "🟡 SZIGNÁL: HOLD (Bizonytalan Sakkmatt Zóna / Spinning Top oldalazás)"
        sl_level = "0.00 USD"
        tp_level = "0.00 USD"
        rrr_ratio = "1 : 0.00"

    # 3. Output Display / Eredmények tördélésmentes megjelenítése
    print(f"{signal}\n")
    print(f"-> Javasolt Stop Loss   (SL): {sl_level}")
    print(f"-> Javasolt Take Profit (TP): {tp_level}")
    print(f"-> Kockázat-Megtérülés  (RRR): {rrr_ratio}\n")
    print("[Program finished]")

if __name__ == "__main__":
    evaluate_pork_protocol_v3()
