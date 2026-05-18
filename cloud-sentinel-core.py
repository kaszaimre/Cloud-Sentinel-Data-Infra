import os
import sys
from datetime import datetime

class InfrastructureManager:
    """
    Központi infrastruktúra és státusz-kezelő modul.
    A korábbi monolitikus tesztverzió moduláris, refaktorált változata.
    """
    def __init__(self):
        self.environment = "Production"
        self.storage_capacity_tb = 5.0
        self.active_pipelines = 80
        
        # Nemzetközi biztonsági és iparági szabványú identitások
        self.allowed_identities = ["System_Admin", "Cloud_Sentinel_Core", "Security_Daemon"]
        self.start_time = datetime.now()

    def get_system_status(self):
        """Visszaadja az infrastruktúra aktuális állapotát egy szótárban."""
        uptime = datetime.now() - self.start_time
        return {
            "environment": self.environment,
            "storage_ready_tb": self.storage_capacity_tb,
            "active_pipelines_count": self.active_pipelines,
            "uptime_seconds": int(uptime.total_seconds()),
            "status": "HEALTHY"
        }

    def verify_identity(self, identity_name):
        """Ellenőrzi, hogy a hozzáférni kívánt identitás engedélyezett-e."""
        if identity_name in self.allowed_identities:
            return True
        return False

    def print_report(self):
        """Kinyomtatja a szabványos architektúra jelentést a terminálra."""
        status = self.get_system_status()
        print("=======================================")
        print(f"   CLOUD SENTINEL CORE REPORT ({status['environment'].upper()})")
        print("=======================================")
        print(f"[*] Storage Capacity : {status['storage_ready_tb']} TB Ready")
        print(f"[*] Active Pipelines : {status['active_pipelines_count']} Micro-services")
        print(f"[*] Core Infrastructure Status : {status['status']}")
        print("=======================================")

if __name__ == "__main__":
    # Inicializáljuk a rendszert és futtatunk egy gyors ellenőrzést
    manager = InfrastructureManager()
    manager.print_report()
