# ==============================================================================
# FÁJL NÉV: 084_risk_position_sizer.py
# SORSZÁM: 084
#
# LEÍRÁS ÉS FELADAT:
# Kockázatarányos Pozícióméretező és Tőkeallokációs (Position Sizing) modul.
# A 082-es mátrix aggregátor kimeneti adatai alapján dolgozik. Kiszámítja, hogy
# a teljes tőke maximum hány százaléka (pl. strict 1-2%) kockáztatható egyetlen 
# ügyleten a stop-loss távolság függvényében. Megvédi az 5TB-os kereskedési magot 
# a túlméretezett pozícióktól és a gyors tőkefogyástól.
# ==============================================================================

import sys

class RiskPositionSizer:
    def __init__(self, total_capital=10000.0, max_risk_per_trade_pct=0.02):
        """
        total_capital: A teljes szabad tőke USD-ben (alapértelmezett: $10,000)
        max_risk_per_trade_pct: Maximális kockázat ügyletenként (szigorú 2%)
        """
        self.total_capital = float(total_capital)
        self.max_risk_amount = self.total_capital * max_risk_per_trade_pct

    def calculate_safe_position_size(self, ticker, entry_price, stop_loss_price):
        print("=========================================================")
        print("   CYBER-BORSOD RISK ENGINE -> POSITION SIZING TOOL      ")
        print("=========================================================")
        print(f"[*] Target Asset Ticker : {ticker}")
        print(f"[*] Available Capital   : ${self.total_capital:,} USD")
        print(f"[*] Max Risk Per Trade  : ${self.max_risk_amount:,} USD (2%)")
        print("-" * 57)

        if entry_price <= stop_loss_price:
            print("[❌ ERROR] Invalid risk setup: Entry price must be higher than Stop-Loss for Long positions.")
            return 0.0

        # Kiszámoljuk a darabonkénti kockázatot (Stop-Loss távolság dollárban)
        risk_per_unit = entry_price - stop_loss_price
        
        # Pozícióméret kiszámítása: Maximális megengedett kockázat / egységenkénti kockázat
        safe_size = self.max_risk_amount / risk_per_unit
        total_exposure = safe_size * entry_price
        
        print(f"  [🟢 CALCULATION OK] Risk metrics aligned.")
        print(f"    [-] Risk Distance Per Unit: ${round(risk_per_unit, 2)} USD")
        print(f"    [-] Safe Position Size    : {round(safe_size, 4)} Units")
        print(f"    [-] Total Market Exposure : ${round(total_exposure, 2):,} USD")
        print("=========================================================")
        return round(safe_size, 4)

if __name__ == "__main__":
    sizer = RiskPositionSizer(total_capital=15000.0)
    # Tesztelés a TradingView-n kapott INTC jelzésre: belépő $45.0, stop-loss $42.5
    sizer.calculate_safe_position_size(ticker="BATS:INTC", entry_price=45.0, stop_loss_price=42.5)
