# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 117_CYBER_DECEPTION_TELEMETRY_SINK
# 
module_desc = """ 
LEÍRÁS (HU):

Központi csapda-alapú telemetria-gyűjtő modul (Telemetry Sink).
Összeköti a kiber-csapdákat (116_cyber_deception_trap) a Phoenix Master naplózóval.
Elkapja, strukturált JSON formátumba rendezi és a központi Sentinel logba
menti az illetéktelen hálózati mozgásokat és támadási kísérleteket.
Mottó: A borsodi nem hackel, a borsodi optimalizál.

DESCRIPTION (EN):

Central deception-based telemetry collection module (Telemetry Sink).
Connects cyber deception traps to the Phoenix Master logger.
Intercepts, structures into JSON, and saves unauthorized network movements
and attack attempts into the central Sentinel log file.
Motto: The Borsodi doesn't hack, the Borsodi optimizes.

SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM """
# ==============================================================================

import json
import os
import time
from datetime import datetime

# Központi naplófájl a meglévő rendszeredből
LOG_FILE = "sentinel_events.log"

def init_sink():
    """Ellenőrzi, hogy a Sentinel naplófájl létezik-e, ha nem, létrehozza."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write(f"[{datetime.now()}] [SYSTEM] Phoenix Telemetry Sink Inicializálva.\n")

def log_deception_event(attacker_ip, port, action_detected, severity="HIGH"):
    """
    Elkapja a kiber-csapdából érkező telemetria adatokat,
    és tiszta JSON formátumú riasztásként elmenti a központi logba.
    """
    payload = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "kernel": "T800_CORE_v5.1",
        "severity": severity,
        "source_ip": attacker_ip,
        "target_port": port,
        "alert_type": action_detected,
        "status": "INTERCEPTED"
    }
    
    # Konzolos visszajelzés Phoenix / T800 stílusban
    print(f"\n[ALERT] [{payload['timestamp']}] ⚠️ {severity} RIASZTÁS A CSAPÁBÓL!")
    print(f"-> Forrás IP: {attacker_ip} | Célobjektum Port: {port}")
    print(f"-> Tevékenység: {action_detected}")
    print(f"-> Rendszerállapot: [✓] T800 HYBRID SHIELD AKTÍV - INCIDENS NAPLÓZVA")
    
    # Biztonságos mentés a fájlba
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload) + "\n")
        return True
    except Exception as e:
        print(f"[ERROR] Nem sikerült írni a(z) {LOG_FILE} fájlba: {e}")
        return False

if __name__ == "__main__":
    init_sink()
    
    print("=== 117_cyber_deception_telemetry_sink INDÍTÁSA ===")
    print("Rendszer aktív, figyelési csatorna nyitva...")
    time.sleep(1)
    
    # Egy teszt riasztás generálása a működés ellenőrzéséhez
    log_deception_event(
        attacker_ip="192.168.1.145", 
        port=22, 
        action_detected="SSH_BRUTE_FORCE_ATTEMPT",
        severity="CRITICAL"
    )
    print("\n[✓] A 117-es modul sikeresen lefutott, a gap betöltve a Git-ben.")
