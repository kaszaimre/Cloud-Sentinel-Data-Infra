//HQ-ban ezt a problémát egy időbélyeg-alapú gyorsítótárral (Timestamp-based Cache) és egy dinamikus időszelet-kezelő (Time-Window) logikával oldjuk meg. 
//Nem a másodperc pontos egyezést keressük, hanem a Coinbase-től kapott utolsó legfrissebb érvényes árat vetjük össze a Binance-szel, 
//amennyiben az egy szigorú időkorláton (például 200 ms) belül van.

import asyncio
import time
import logging
from typing import Optional, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("BorsodiMatrixHQ-LatencyHandler")

class AsynchronousCrossValidator:
    def __init__(self, max_allowed_latency_ms: float = 200.0, max_deviation: float = 0.01):
        """
        :param max_allowed_latency_ms: Maximális megengedett kor a Coinbase adatra (milliszekundumban).
        :param max_deviation: Maximális megengedett eltérés a két tőzsde között (1%).
        """
        self.max_allowed_latency_ms = max_allowed_latency_ms
        self.max_deviation = max_deviation
        
        # Lokális állapot a legfrissebb Coinbase adatok tárolására
        self.last_coinbase_price: Optional[float] = None
        self.last_coinbase_timestamp_ms: float = 0.0

    def update_coinbase_price(self, price: float):
        """Ez a metódus fut a Coinbase aszinkron WebSocket/API olvasó szálán."""
        self.last_coinbase_price = price
        self.last_coinbase_timestamp_ms = time.time() * 1000  # Unix idő ezredmásodpercben
        logger.debug(f"Coinbase cache frissítve: {price}")

    def validate_binance_tick(self, binance_price: float) -> bool:
        """
        A Binance WebSocket adatfolyam hívja meg azonnal, amikor új tick érkezik.
        Nem blokkoló módon ellenőrzi a késleltetést és az árat.
        """
        current_time_ms = time.time() * 1000

        # 1. VÉDELMI VONAL: Van-e egyáltalán adat a gyorsítótárban?
        if self.last_coinbase_price is None:
            logger.warning("⚠️ NINCS ADAT: A Coinbase gyorsítótár üres. Keresztvalidáció sikertelen!")
            return False

        # 2. VÉDELMI VONAL: Késleltetés (Latency / Data Age) ellenőrzése
        data_age_ms = current_time_ms - self.last_coinbase_timestamp_ms
        
        if data_age_ms > self.max_allowed_latency_ms:
            logger.critical(
                f"🚨 LASSÚ HÁLÓZAT / ADATSZAKADÁS! A Coinbase adat túl régi. "
                f"Kora: {data_age_ms:.2f} ms (Maximum engedélyezett: {self.max_allowed_latency_ms} ms). "
                f"Azonnali tranzakciós blokkolás biztonsági okokból!"
            )
            return False

        # 3. VÉDELMI VONAL: Árvalidáció a friss adatokkal
        price_deviation = abs(binance_price - self.last_coinbase_price) / self.last_coinbase_price
        if price_deviation > self.max_deviation:
            logger.critical(
                f"🚨 FALS ÁRTÜSKE ÉSZLELVE (Késleltetésen belül)! "
                f"Binance: {binance_price}, Coinbase: {self.last_coinbase_price}. "
                f"Eltérés: {price_deviation*100:.2f}%. Blokkolás!"
            )
            return False

        # Ha a Coinbase adat friss és az eltérés is elhanyagolható: a tick valid
        logger.info(f"✅ Tick validálva. Adat kora: {data_age_ms:.2f} ms. Eltérés: {price_deviation*100:.4f}%")
        return True

# --- ASZINKRON SZIMULÁCIÓS TESZT ---
async def simulate_coinbase_stream(validator: AsynchronousCrossValidator):
    """Szimulálja a Coinbase lassabb, szakaszos áradatait."""
    # Kezdő ár
    validator.update_coinbase_price(98500.0)
    
    # 1. szituáció: Normál működés, a Coinbase 50 ms-os csúszással frissül
    await asyncio.sleep(0.05)
    validator.update_coinbase_price(98510.0)
    
    # 2. szituáció: Hálózati szakadás vagy hirtelen lassulás a Coinbase oldalon
    # Nem frissítjük a gyorsítótárat, így az adat el fog avulni a Binance tick érkezésekor
    await asyncio.sleep(0.3)  # 300 ms késleltetés (átlépi a 200 ms-os határt)

async def simulate_binance_stream(validator: AsynchronousCrossValidator):
    """Szimulálja a Binance ultragyors, valós idejű WebSocket beérkezéseit."""
    await asyncio.sleep(0.02)
    # T1: 20 ms-nál járunk, a Coinbase 0 ms-os adata 20 ms idős -> VALID
    print("\n--- [T1 Teszt: Normál alacsony késleltetés] ---")
    validator.validate_binance_tick(binance_price=98505.0)

    await asyncio.sleep(0.05)
    # T2: 70 ms-nál járunk, a Coinbase 50 ms-nál frissült (20 ms idős) -> VALID
    print("\n--- [T2 Teszt: Frissített cache-el történő validáció] ---")
    validator.validate_binance_tick(binance_price=98512.0)

    await asyncio.sleep(0.25)
    # T3: 320 ms-nál járunk. A Coinbase nem frissült 270 ms óta -> BLOKKOLÁS (Stale Data)
    print("\n--- [T3 Teszt: Lassú hálózat miatti adat-elavulás] ---")
    validator.validate_binance_tick(binance_price=98520.0)

async def main():
    validator = AsynchronousCrossValidator(max_allowed_latency_ms=200.0)
    # A két adatfolyam párhuzamos, aszinkron futtatása
    await asyncio.gather(
        simulate_coinbase_stream(validator),
        simulate_binance_stream(validator)
    )

if __name__ == "__main__":
    asyncio.run(main())
