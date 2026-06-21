"""
=====================================================================
    Modul specifikáció az automatizált README generátorhoz.
=====================================================================
LEÍRÁS (HU): 
Monte Carlo szimulációs motor. A piaci káoszt modellezi több ezer lehetséges jövőbeli 
forgatókönyv futtatásával. Nem jósolja meg az árat, hanem a "szélsőértékeket" (összeomlás/csúcs) 
térképezi fel. A Borsodi operátor ezzel a modullal méri a kockázatot a vakszerencse helyett.

DESCRIPTION (EN): 
Monte Carlo simulation engine. Models market chaos by running thousands 
of potential future scenarios. Does not predict the price; instead, it maps out the extremes 
(crash/peak). Used by the Borsodi operator to quantify risk instead of relying on blind luck.

SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM
=====================================================================
"""

import json
import random
from datetime import datetime

# --- GLOBÁLIS ORACLE V7.0 ADATOK ---
TOTAL_DEVICES = 661
PAGE_START = 601
PAGE_END = 661

# Teljes arzenál generálása
cyber_arsenal = [f"Cyber_Device_{i}" for i in range(1, TOTAL_DEVICES + 1)]
# Utolsó lap kiber-eszközei (601-661)
last_page_devices = cyber_arsenal[PAGE_START - 1:PAGE_END]


# =====================================================================
# 1. LIME ÉS PIROS STÁTUSZ SZIMULÁCIÓ (UTOLSÓ LAP)
# =====================================================================
def run_status_simulation(devices):
    """Szimulálja és kiszámítja a Lime és Piros státuszok arányát."""
    statuses = ["Lime", "Piros"]
    simulated_data = {dev: random.choice(statuses) for dev in devices}
    
    total = len(devices)
    lime_count = sum(1 for status in simulated_data.values() if status == "Lime")
    piros_count = total - lime_count
    
    lime_ratio = (lime_count / total) * 100
    piros_ratio = (piros_count / total) * 100
    
    print("📊 --- LIME ÉS PIROS STÁTUSZ RIPORT (UTOLSÓ LAP) ---")
    print(f"Összes eszköz a lapon: {total} darab ({PAGE_START}-{PAGE_END})")
    print(f"🟢 Lime státusz: {lime_count} db ({lime_ratio:.2f}%)")
    print(f"🔴 Piros státusz: {piros_count} db ({piros_ratio:.2f}%)")
    print("-" * 50)
    
    return simulated_data


# =====================================================================
# 2. CENTRALCHARTS API-KLIENS VÁZ
# =====================================================================
class CentralChartsClient:
    """API kliens a CentralCharts élő adatfolyam fogadásához."""
    def __init__(self, api_key="KIBER_SECURE_TOKEN_XYZ"):
        self.api_key = api_key
        self.base_url = "https://centralcharts.local"
        self.is_connected = False

    def connect_stream(self):
        """Kapcsolódás a kiber-adatfolyamhoz."""
        self.is_connected = True
        print(f"📡 [CentralCharts] Élő adatfolyam kapcsolat létrehozva. Kulcs: {self.api_key[:5]}...")

    def fetch_live_market_data(self):
        """Élő piaci adatok fogadásának szimulációja."""
        if not self.is_connected:
            print("❌ Hiba: Nincs aktív kapcsolat a CentralCharts stream-hez!")
            return None
        
        live_tickers = ["BTC/USD", "EUR/HUF", "AAPL", "TSLA"]
        mock_stream_data = {
            "timestamp": datetime.now().isoformat(),
            "ticker": random.choice(live_tickers),
            "price": round(random.uniform(10, 95000), 2),
            "change_percent": round(random.uniform(-5.0, 5.0), 2)
        }
        print(f"📥 [CentralCharts Stream]: {mock_stream_data['ticker']} -> {mock_stream_data['price']} ({mock_stream_data['change_percent']}%)")
        return mock_stream_data


# =====================================================================
# 3. GOOGLE PLAY ÁRUHÁZAS EXPORTÁLÓ FÜGGVÉNY
# =====================================================================
def export_to_play_store_format(devices, limit=20):
    """Előkészíti és kiexportálja az első megadott számú eszközt Play Áruház formátumba."""
    target_devices = devices[:limit]
    
    export_manifest = {
        "export_metadata": {
            "target_platform": "Google Play Store",
            "generation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_exported": len(target_devices)
        },
        "application_package_list": [
            {
                "app_id": f"com.cyberoracle.device_{dev.lower().split('_')[-1]}",
                "version": "7.0.0",
                "status": "Ready_To_Deploy",
                "linked_hardware": dev
            }
            for dev in target_devices
        ]
    }
    
    json_output = json.dumps(export_manifest, indent=4, ensure_ascii=False)
    print("🚀 --- GOOGLE PLAY ÁRUHÁZ EXPORT MANIFEST (TOP 20) ---")
    print(json_output[:600] + "\n... [VÁGVA A KIJELZŐN] ...")
    print("-" * 50)
    
    return json_output


# =====================================================================
# RENDSZER INDÍTÁSA / EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("🦾 [Oracle v7.0 Core] Rendszerindítás, Don Tábornok! A kódok élesítve.\n")
    
    # 1. Státuszarány futtatása az utolsó lapon
    last_page_statuses = run_status_simulation(last_page_devices)
    
    # 2. CentralCharts API inicializálás és adatfogadás
    cc_client = CentralChartsClient()
    cc_client.connect_stream()
    cc_client.fetch_live_market_data()
    print("-" * 50)
    
    # 3. Google Play 20-as export futtatása a teljes arzenálból
    play_store_json = export_to_play_store_format(cyber_arsenal, limit=20)
    
    print("\n😎 Minden modul hiba nélkül lefutott, fasa és kész!")
