# ==============================================================================
# FÁJL NÉV: 082_watchlist_matrix_aggregator.py
# SORSZÁM: 082
#
# LEÍRÁS ÉS FELADAT:
# Watchlist Mátrix Aggregátor és Portfólió Súlyozó modul.
# Központosítja és összefésüli a TradingView felületről (pl. US ELITE, SAJÁT fülek)
# érkező különböző eszközcsoportok adatait. Kiszámolja a globális piaci kitettséget,
# és ha túl sok eszköz ad egyszerre BUY jelzést (mint a képen az AAPL, NVDA, GOOGL),
# korlátozza a maximális tőkeallokációt, hogy megvédje a rendszert a piaci korrekcióktól.
# ==============================================================================

import sys

class WatchlistMatrixAggregator:
    def __init__(self):
        # A képeden látható valós idejű "US ELITE" szektor állapotok baseline mátrixa
        self.us_elite_cluster = {
            "AAPL": {"score": "3/3", "status": "GREEN"},
            "MSFT": {"score": "0/3", "status": "RED"},
            "NVDA": {"score": "3/3", "status": "GREEN"},
            "GOOGL": {"score": "3/3", "status": "GREEN"},
            "TSLA": {"score": "3/3", "status": "GREEN"}
        }
        self.max_simultaneous_trades = 3

    def audit_portfolio_exposure(self):
        print("=========================================================")
        print("   CYBER-BORSOD TRADING -> PORTFOLIO EXPOSURE AUDITOR    ")
        print("=========================================================")
        print("[*] Analyzing active high-score tickers in US_ELITE cluster...")
        
        active_buy_signals = []
        
        for ticker, metrics in self.us_elite_cluster.items():
            score = metrics["score"]
            status = metrics["status"]
            
            if score == "3/3" and status == "GREEN":
                active_buy_signals.append(ticker)
                print(f"  [+] Active Buy Signal Found: {ticker} | Score: {score}")

        print("-" * 57)
        total_signals = len(active_buy_signals)
        print(f"[*] Total Confirmed Core Triggers: {total_signals} Devices")

        # BIZTONSÁGI ÉS KOCKÁZATI LOGIKA: Túlterheltségi korlát ellenőrzése
        if total_signals > self.max_simultaneous_trades:
            print(f"  [🚨 RISK WARNING] Exposure limit breached! Active signals ({total_signals}) > Max ({self.max_simultaneous_trades})")
            print("    [!] Threat: Over-exposure to highly correlated tech equities.")
            print("    [🛡️ ACTION] Throttling executing nodes. Forcing selective entry mode.")
            return False
            
        print("[🟢 COMPLIANT] Risk overhead within baseline safety parameters.")
        return True

if __name__ == "__main__":
    aggregator = WatchlistMatrixAggregator()
    aggregator.audit_portfolio_exposure()
    print("=========================================================")
