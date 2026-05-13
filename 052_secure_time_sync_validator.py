# ==============================================================================
# FÁJL NÉV: 052_secure_time_sync_validator.py
# SORSZÁM: 052
#
# LEÍRÁS ÉS FELADAT:
# Biztonságos Időszinkronizáció Ellenőrző (Secure Time Sync Validator) modul.
# A kiberbiztonsági logfájlokban az időbélyegek hitelessége kritikus fontosságú.
# A modul ellenőrzi a helyi rendszeridőt egy megbízható külső NTP időszerverhez 
# képest. Ha a kettő közötti eltérés (Time Drift) meghaladja a megengedett limitet,
# riasztást ad, mert a támadók manipulálhatták az időt a logok meghamisítására.
# ==============================================================================

import sys
from datetime import datetime

class TimeSyncValidator:
    def __init__(self, max_drift_seconds=5):
        self.max_drift_seconds = max_drift_seconds

    def verify_system_clock_integrity(self, simulated_ntp_timestamp):
        """
        Összehasonlítja a rendszeridőt a hitelesített hálózati idővel.
        simulated_ntp_timestamp: Unix időbélyeg másodpercben
        """
        print("=========================================================")
        print("   CYBER-BORSOD INFRA -> CHRONOS TIME DRIFT AUDIT CORE   ")
        print("=========================================================")
        
        helyi_unix_ido = datetime.now().timestamp()
        idobeli_elteris = abs(helyi_unix_ido - simulated_ntp_timestamp)
        
        print(f"  [-] Local System Time Stamp : {int(helyi_unix_ido)}")
        print(f"  [-] Trusted Network Time    : {int(simulated_ntp_timestamp)}")
        print(f"  [-] Absolute Clock Drift    : {round(idobeli_elteris, 3)} seconds")
        print("-" * 57)

        # BIZTONSÁGI ELLENŐRZÉS: Meghaladja a megengedett csúszási limitet?
        if idobeli_elteris > self.max_drift_seconds:
            print("  [🚨 TIME SYNC BREACH] Critical clock drift threshold exceeded!")
            print("    [!] RISK: Potential Log Replay Attack or timeline obfuscation active.")
            print("    [🛡️ ACTION] Flagging active logs as UNTRUSTED until NTP synchronization.")
            return False
        else:
            print("[🟢 COMPLIANT] System timeline verified and synchronized with network cluster.")
            return True

if __name__ == "__main__":
    validator = TimeSyncValidator(max_drift_seconds=3)
    
    # 1. Teszt eset: Szabályos, szinkronban lévő idő (aktuális idő)
    pontos_ido = datetime.now().timestamp()
    validator.verify_system_clock_integrity(pontos_ido)
    
    print("\n" + "="*57 + "\n")
    
    # 2. Teszt eset: Manipulált vagy elcsúszott rendszeridő (10 másodperces eltérés)
    elcsuszott_ido = datetime.now().timestamp() - 10
    validator.verify_system_clock_integrity(elcsuszott_ido)
    print("=========================================================")
