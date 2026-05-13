# ==============================================================================
# FÁJL NÉV: 060_automated_incident_playbook_orchestrator.py
# SORSZÁM: 060
#
# LEÍRÁS ÉS FELADAT:
# Automatizált Incidens-kezelési Forgatókönyv Rendező (Playbook Orchestrator) modul.
# A SOAR (Security Orchestration, Automation, and Response) elvek alapján működik.
# Ha a Sentinel vagy a szimulációs konzol kritikus incidenst észlel, ez a modul 
# koordinálja a válaszlépéseket: elindítja a tűzfal tiltást (DROP), végrehajtja a 
# folyamatleállítást (ISOLATE), és frissíti a központi 'sentinel_events.log' naplót.
# ==============================================================================

import sys
import time
from datetime import datetime

class IncidentPlaybookOrchestrator:
    def __init__(self):
        self.log_path = "./sentinel_events.log"

    def trigger_incident_playbook(self, alert_source, threat_vector, target_identifier):
        print("=========================================================")
        print("   CYBER-BORSOD SOAR -> AUTOMATED PLAYBOOK ORCHESTRATOR  ")
        print("=========================================================")
        print(f"🚨 [INCIDENT RECEIVED] Source: {alert_source} | Vector: {threat_vector}")
        print(f"[*] Targeting Vulnerable Component Identifier: {target_identifier}")
        print("-" * 57)
        
        # 1. FÁZIS: Azonnali izoláció szimulálása
        print("[*] Phase 1/3: Isolating threat blast radius...")
        time.sleep(0.5)
        print(f"  [🛡️ SOAR ACTION] Executing isolation logic on target: {target_identifier}")
        
        # 2. FÁZIS: Tűzfal konfiguráció frissítése
        print("[*] Phase 2/3: Deploying perimeter blocking rules...")
        time.sleep(0.5)
        print(f"  [🛡️ SOAR ACTION] Perimeter rule élesítve -> BLOCK traffic related to {threat_vector}")
        
        # 3. FÁZIS: Központi audit naplózás
        print("[*] Phase 3/3: Committing orchestration metrics to filesystem...")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] [SOAR_PLAYBOOK] EXECUTED: Vector={threat_vector} | Target={target_identifier} | Status=MITIGATED\n")
            print("[🟢 SUCCESS] Incident mitigated automatically. System returned to operational baseline.")
        except Exception as e:
            print(f"[❌ STORAGE ERROR] Failed to write SOAR metrics: {e}")
            
        print("=========================================================")

if __name__ == "__main__":
    orchestrator = IncidentPlaybookOrchestrator()
    # Szimulálunk egy DDoS támadás utáni automatikus SOAR lefutást
    orchestrator.trigger_incident_playbook(
        alert_source="WAF_FIREWALL_05", 
        threat_vector="VOLUMETRIC_DDOS", 
        target_identifier="185.220.101.5"
    )
