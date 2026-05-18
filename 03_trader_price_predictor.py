# ==============================================================================
# FÁJL NÉV: 03_trader_price_predictor.py -> UTÓD: 109_automated_price_scanner.py
# SORSZÁM: 109
#
# LEÍRÁS ÉS FELADAT:
# Automatizált Kereskedelmi Árszkenner és Predikciós (Price Scanner) magmodul.
# Kiküszöböli a manuális billentyűzet-alapú adatbevitelt. Automatikusan generál
# valós idejű szimulált piaci ármozgásokat egy elosztott tömbbe, majd emberi kéz
# beavatkozása nélkül lefuttatja a lendület- és pánik-elemzést, bájtszintű
# karakteres grafikont rajzolva a központi 100-as Master Orchestrator számára.
# ==============================================================================

import time
import random

class AutomatedPriceScanner:
    def __init__(self):
        self.log_file = "./sentinel_events.log"

    def execute_automatic_scan(self):
        print("=========================================================")
        print("   CYBER-BORSOD TRADING -> AUTOMATED PRICE SCANNER       ")
        print("=========================================================")
        print("[*] Connecting to high-frequency live market data feed...")
        
        # Automatikus árbekérés szimulációja (manuális input helyett)
        base_price = 100.0
        prices = []
        
        for i in range(1, 11):
            time.sleep(0.1) # Gyors hálózati tick szimuláció
            # Véletlenszerű, de trendalapú ármozgás generálása
            base_price += random.uniform(-2.0, 5.0)
            prices.append(round(base_price, 2))
            print(f"  [TICK {i:02d}/10] Auto-Scanned Price Spot: ${prices[-1]:.2f}")

        print("\n[!] Processing data arrays via non-graphical matrix...")
        
        # Matematikai és Predikciós logika
        atlag = sum(prices) / 10
        utolso = prices[-1]
        lendulet = (prices[-1] - prices[-4]) / 3
        joslat = utolso + lendulet

        volatilitas = max(prices) - min(prices)
        riziko = "!!! MAGAS (PÁNIK) !!!" if volatilitas > (atlag * 0.05) else "KÖZEPES" if volatilitas > (atlag * 0.02) else "ALACSONY (STABIL)"

        # Grafikon kirajzolása
        min_p = min(min(prices), joslat)
        max_p = max(max(prices), joslat)
        
        print("\n--- PIACI MOZGÁS ÉS JÓSLAT ---")
        for idx, p in enumerate(prices):
            hossz = int(((p - min_p) / (max_p - min_p + 0.0001)) * 20)
            print(f"{idx+1:2d}. ár: {p:10.2f} |{'#' * hossz}")

        hossz_j = int(((joslat - min_p) / (max_p - min_p + 0.0001)) * 20)
        print(f"11. TIPP: {joslat:10.2f} |{'*' * hossz_j}  <-- JÖVŐ")

        print("-" * 40)
        print(f"Aktuális átlag:   {atlag:.2f}")
        print(f"Lendület:         {lendulet:+.2f}")
        print(f"Piaci feszültség: {riziko}")
        print(f"Várható irány:    " + ("EMELKEDÉS (BULL)" if joslat > utolso else "CSÖKKENŐ (BEAR)"))
        print("-" * 40)
        return True

if __name__ == "__main__":
    scanner = AutomatedPriceScanner()
    scanner.execute_automatic_scan()
