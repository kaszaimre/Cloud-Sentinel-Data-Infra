"""
================================================================================
BORSOD MATRIX HQ - CYBER-BORSOD ENGINE DATA SYSTEM
Module: Resilient WebSocket Client with Automated Reconnection & Heartbeat
================================================================================

DESCRIPTION / LEÍRÁS:
Ez a modul biztosítja a Borsodi Mátrix HQ éles kereskedési ökoszisztémájának 
folyamatos, 100%-os online jelenlétét a hálózati infrastruktúra szintjén. 
A szkript kifejezetten a 'BORSOD RADAR PULSING.py' és a 'CYBER-BORSOD SCANNER MAGNET' 
modulok alá ágyazódik be, mint az aszinkron, hibatűrő adatfogadó motor.

PURPOSE / CÉLKITŰZÉS:
1. NÉMA FAGYÁS ELLENI VÉDELEM (Silent Timeout): Megakadályozza az olyan rejtett 
   hálózati szakadásokat, ahol a TCP socket nyitva marad, de valójában már nem 
   érkezik áradat a tőzsdéről.
2. EXPONENCIÁLIS VISSZALÉPÉS (Exponential Backoff): Kapcsolati szakadás vagy 
   tőzsdei karbantartás esetén megvédi a rendszert az IP-tiltástól (Rate Limiting) 
   azáltal, hogy dinamikusan növeli az újraépítési kísérletek közötti időt.
3. NEM-BLOKKOLÓ ASZINKRONITÁS: Az aktív életjel-ellenőrzés (Ping/Pong Heartbeat) 
   és a valós idejű tick-adatok fogadása egymással párhuzamosan, minimális 
   késleltetéssel (Low Latency) fut.

================================================================================
"""

import asyncio
import logging
import time
import websockets
import json

# Logolás beállítása a Cloud-Sentinel Telemetry számára
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("CyberBorsod-Engine-WS")

class ResilientWebSocketClient:
    def __init__(self, uri: str, client_name: str = "Scanner-Magnet"):
        self.uri = uri
        self.client_name = client_name
        self.is_running = True
        self.websocket = None
        self.last_heartbeat_received = time.time()
        
        # Újraépítési paraméterek (Exponential Backoff)
        self.base_reconnect_delay = 2.0  # Kezdő késleltetés: 2 másodperc
        self.max_reconnect_delay = 60.0  # Maximális késleltetés: 1 perc

    async def connect_and_run(self, data_callback):
        """A fő aszinkron ciklus, amely fenntartja és újraépíti a kapcsolatot."""
        reconnect_delay = self.base_reconnect_delay

        while self.is_running:
            try:
                logger.info(f"🔌 [{self.client_name}] Csatlakozás a végponthoz: {self.uri}")
                
                async with websockets.connect(self.uri, ping_interval=None) as ws:
                    self.websocket = ws
                    self.last_heartbeat_received = time.time()
                    reconnect_delay = self.base_reconnect_delay  # Sikeres kapcsolódásnál visszaáll a számláló
                    logger.info(f"✅ [{self.client_name}] Kapcsolat sikeresen felépítve!")

                    # Elindítjuk a háttérben futó Heartbeat (Ping) figyelőt és az adatfeldolgozót párhuzamosan
                    await asyncio.gather(
                        self._heartbeat_loop(),
                        self._receive_loop(data_callback)
                    )

            except (websockets.exceptions.ConnectionClosed, Exception) as e:
                logger.error(f"❌ [{self.client_name}] Kapcsolati hiba vagy szakadás: {e}")
                
            # Exponenciális visszalépés lép életbe hiba esetén
            logger.warning(f"⏳ [{self.client_name}] Újraépítési kísérlet {reconnect_delay:.1f} másodperc múlva...")
            await asyncio.sleep(reconnect_delay)
            reconnect_delay = min(reconnect_delay * 2, self.max_reconnect_delay)

    async def _receive_loop(self, data_callback):
        """Fogadja a bejövő tick adatokat a tőzsdéről."""
        async for message in self.websocket:
            data = json.loads(message)
            
            # Szerver-szintű pingek lekezelése a protokoll szerint
            if isinstance(data, dict) and data.get("type") == "ping":
                await self.websocket.send(json.dumps({"type": "pong"}))
                continue
                
            # Adat továbbítása a Borsodi Mátrix belső feldolgozóinak
            self.last_heartbeat_received = time.time()
            data_callback(data)

    async def _heartbeat_loop(self):
        """Aktív ellenőrzés (Active Probing): Ha a tőzsde elnémul, megszakítjuk a fagyott kapcsolatot."""
        check_interval = 5.0  # 5 másodpercenként ellenőrizzük az életjelet
        max_silent_period = 15.0  # Ha 15 másodpercig nincs adat vagy ping, a kapcsolat halott

        while self.websocket and self.websocket.open:
            await asyncio.sleep(check_interval)
            
            # Manuális ping küldése a szervernek
            try:
                await self.websocket.ping()
            except Exception:
                logger.warning(f"⚠️ [{self.client_name}] A ping küldése meghiúsult.")
                break

            # Csendes fagyás (Silent Drop) ellenőrzése
            silent_duration = time.time() - self.last_heartbeat_received
            if silent_duration > max_silent_period:
                logger.critical(f"🚨 [{self.client_name}] Néma fagyás észlelve! {silent_duration:.1f} másodperce nincs adat. Kapcsolat kényszerített lezárása.")
                await self.websocket.close()
                break

    def stop(self):
        """A kliens tiszta leállítása."""
        self.is_running = False

# --- INTEGRÁCIÓS SZIMULÁCIÓ ---
def cyber_borsod_data_handler(data):
    """Ez a callback függvény fogadja a tiszta adatokat a BORSOD RADAR számára."""
    print(f"📥 [RADAR ENGINE] Új érvényes adat érkezett: {data}")

async def main():
    # Szimulált publikus WebSocket teszt végpont
    test_uri = "wss://echo.websocket.events"
    
    client = ResilientWebSocketClient(uri=test_uri, client_name="Cyber-Borsod-Radar")
    
    # Elindítjuk a klienst egy háttérfeladatként
    client_task = asyncio.create_task(client.connect_and_run(cyber_borsod_data_handler))
    
    # Hagyjuk futni a szimulációt 10 másodpercig, majd leállítjuk
    await asyncio.sleep(10)
    client.stop()
    await client_task

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Rendszer leállítva.")
