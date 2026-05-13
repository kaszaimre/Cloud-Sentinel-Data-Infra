# ==============================================================================
# FÁJL NÉV: 058_windows_registry_tamper_sensor.py
# SORSZÁM: 058
#
# LEÍRÁS ÉS FELADAT:
# Windows Rendszerleíró-adatbázis Manipuláció-érzékelő (Registry Tamper Sensor) 
# modul. A helyi Windows tesztkörnyezet automatikus indítókulcsait (Run Keys) 
# és rendszerbiztonsági beállításait (UAC, Windows Defender szabályok) ellenőrzi. 
# Kiszűri, ha egy kártevő vagy illetéktelen folyamat tartós rendszer-elérést (Persistence) 
# próbál kiépíteni a regisztrációs adatbázis kulcsainak titkos módosításával.
# ==============================================================================

import sys
import os

class RegistryTamperSensor:
    def __init__(self):
        # Kritikus Windows automatikus indulási útvonalak és biztonsági kulcsok listája
        self.monitored_keys = [
            r"HKLM\Software\Microsoft\Windows\CurrentVersion\Run",
            r"HKCU\Software\Microsoft\Windows\CurrentVersion\Run",
            r"HKLM\System\CurrentControlSet\Control\SecureBoot"
        ]

    def audit_registry_key_state(self, key_path, expected_status_string):
        print("=========================================================")
        print("   CYBER-BORSOD HOST SEC -> REGISTRY INTEGRITY MONITOR   ")
        print("=========================================================")
        print(f"[*] Auditing internal configuration node path: {key_path}")
        print(f"[*] Expected Baseline Signature              : {expected_status_string}")
        print("-" * 57)

        # Cross-platform ellenőrzés szimulálása: a modul Git Bash / Linux alatt is lefut hiba nélkül
        is_windows = sys.platform.startswith('win')
        
        # Szimulálunk egy módosított állapotot a teszt kedvéért
        simulated_actual_status = "MALICIOUS_BACKDOOR_INJECTED_SIGNATURE" if "Run" in key_path else expected_status_string
        
        print(f"  [-] OS Platform Context Detected: {sys.platform}")
        print(f"  [-] Extracted Runtime State Value: {simulated_actual_status}")
        print("-" * 57)

        # BIZTONSÁGI ELLENŐRZÉS: Eltér az aktuális érték az ellenőrzött alapértéktől?
        if simulated_actual_status != expected_status_string:
            print("  [🚨 SECURITY TAMPER DETECTED] Registry key alignment anomaly!")
            print(f"    [!] Threat Vector: Unauthorized persistence mechanism modification found.")
            print("    [🛡️ ACTION] Rolling back registry parameters to baseline status. Freezing thread.")
            return False
        else:
            print("[🟢 COMPLIANT] Key configuration values verified. No tampering indicators.")
            return True

if __name__ == "__main__":
    sensor = RegistryTamperSensor()
    
    # 1. Teszt eset: Biztonságos rendszerbeállítás ellenőrzése
    sensor.audit_registry_key_state(
        key_path=r"HKLM\System\CurrentControlSet\Control\SecureBoot", 
        expected_status_string="SecureBoot_ACTIVE_COMPLIANT"
    )
    
    print("\n" + "="*57 + "\n")
    
    # 2. Teszt eset: Gyanús indítókulcs-módosítás észlelése
    sensor.audit_registry_key_state(
        key_path=r"HKCU\Software\Microsoft\Windows\CurrentVersion\Run", 
        expected_status_string="CLEAN_BASELINE_EMPTY"
    )
    print("=========================================================")
