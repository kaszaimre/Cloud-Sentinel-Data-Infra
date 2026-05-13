import os
import sys
import time
import random
from datetime import datetime

class TradeRiskManager:
    """
    Automatizált kockázatkezelő modul (Stop-Loss & Take-Profit Engine).
    Figyeli az aktív pozíciókat és automatikusan végrehajtja a kényszerlikvidálást.
    """
    def __init__(self, entry_price, position_size, stop_loss_pct=0.02, take_profit_pct=0.06):
        self.entry_price = float(entry_price)
        self.position_size = float(position_size)
        
        # Kockázati szintek kiszámítása (Stop-Loss: -2%, Take-Profit: +6%)
        self.stop_loss_price = round(self.entry_price * (1.0 - stop_loss_pct), 2)
        self.take_profit_price = round(self.entry_price * (1.0 + take_profit_pct), 2)
        
        self.is_position_active = True
        self.log_file = "./sentinel_events.log"

    def log_trade_event(self, message):
        """Események mentése a központi sentinel_events.log fájlba."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] [RISK_ENGINE] {message}\n")
        except Exception:
            pass

    def monitor_market_feed(self):
        """Élő piaci ármozgások szimulálása és a szintek folyamatos ellenőrzése."""
        current_price = self.entry_price
        print("=========================================================")
        print("   CYBER-BORSOD TRADING CORE -> RISK MANAGER INITIALIZED ")
        print("=========================================================")
        print(f"[*] Position Size  : {self.position_size} BTC")
        print(f"[*] Entry Price    : ${self.entry_price:,} USD")
        print(f"🚨 [STOP-LOSS]     : ${self.stop_loss_price:,} USD (Max Risk)")
        print(f"🎯 [TAKE-PROFIT]   : ${self.take_profit_price:,} USD (Target)")
        print("=========================================================")
        
        self.log_trade_event(f"POSITION_OPEN: Entry ${self.entry_price} | SL: ${self.stop_loss_price} | TP: ${self.take_profit_price}")

        tick_count = 0
        while self.is_position_active:
            time.sleep(1.5)  # 1.5 másodpercenként frissül a piac
            tick_count += 1
            
            # Véletlenszerű piaci ingadozás szimulációja (-1.5% és +1.5% között)
            price_change = random.uniform(-0.015, 0.015)
            current_price = round(current_price * (1.0 + price_change), 2)
            
            pnl = round((current_price - self.entry_price) * self.position_size, 2)
            print(f"[TICK #{tick_count:02d}] Live Price: ${current_price:,} USD | PnL: ${pnl:+,} USD")

            # 1. Ellenőrzés: Elérte a Stop-Loss szintet?
            if current_price <= self.stop_loss_price:
                print("\n" + "="*57)
                print(f"🚨 [STOP-LOSS TRIGGERED] Current price ${current_price} <= ${self.stop_loss_price}")
                print(f"[!] Executing Emergency Market Order. Position liquidated.")
                print(f"[!] Final Realized PnL: {pnl:+,} USD")
                print("="*57)
                
                self.log_trade_event(f"LIQUIDATION_SL: Closed at ${current_price} | PnL: {pnl} USD")
                self.is_position_active = False

            # 2. Ellenőrzés: Elérte a Take-Profit szintet?
            elif current_price >= self.take_profit_price:
                print("\n" + "="*57)
                print(f"🎯 [TAKE-PROFIT TRIGGERED] Current price ${current_price} >= ${self.take_profit_price}")
                print(f"[🟢] Target reached. Order executed successfully.")
                print(f"[🟢] Final Realized Profit: {pnl:+,} USD")
                print("="*57)
                
                self.log_trade_event(f"LIQUIDATION_TP: Closed at ${current_price} | PnL: {pnl} USD")
                self.is_position_active = False

if __name__ == "__main__":
    # Teszt indítása: 1 BTC pozíció $95,000-os belépő áron
    # Stop-Loss: $93,100 (-2%) | Take-Profit: $100,700 (+6%)
    engine = TradeRiskManager(entry_price=95000.0, position_size=1.0)
    
    try:
        engine.monitor_market_feed()
    except KeyboardInterrupt:
        print("\n[!] Risk Manager tracking paused by administrator.")
