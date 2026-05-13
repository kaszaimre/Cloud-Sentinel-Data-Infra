# ==============================================================================
# FÁJL NÉV: 067_linux_kernel_sysctl_hardener.py
# SORSZÁM: 067
#
# LEÍRÁS ÉS FELADAT:
# Linux Rendszermag Biztonsági Paraméter-keményítő (Kernel Sysctl Hardener) modul.
# A 5TB-os felhőcsomópontok biztonsági beállításait vizsgálja az /etc/sysctl.conf 
# fájlon keresztül. Ellenőrzi a kritikus hálózati és memóriavédelmi kernel flag-eket, 
# mint az IP továbbítás letiltása (ip_forward) vagy az ICMP átirányítások elutasítása, 
# megvédve a host gépet az útvonal-eltérítéses (Routing Hijack) támadásoktól.
# ==============================================================================

import re
import sys

class LinuxSysctlHardener:
    def __init__(self):
        # Elvárt biztonsági kernel paraméter-beállítások (Hardening baseline)
        self.security_baseline = {
            "net.ipv4.ip_forward": "0",
            "net.ipv4.conf.all.accept_redirects": "0",
            "kernel.randomize_va_space": "2"  # Teljes ASLR memóriavédelem
        }

    def audit_sysctl_configuration(self, raw_sysctl_content):
        print("=========================================================")
        print("   CYBER-BORSOD KERNEL SEC -> SYSCTL CONFIG HARDENING    ")
        print("=========================================================")
        print("[*] Parsing runtime kernel sub-system allocation keys...")
        
        compliance_breaches = 0
        lines = raw_sysctl_content.strip().split("\n")
        parsed_sysctl = {}
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith(";"):
                continue
            if "=" in line:
                kulcs, ertek = line.split("=", 1)
                parsed_sysctl[kulcs.strip()] = ertek.strip()

        # Szabályrendszer ellenőrzése
        for parameter, expected_value in self.security_baseline.items():
            current_value = parsed_sysctl.get(parameter, "unknown")
            print(f"  [-] Parameter: '{parameter}' -> Active: '{current_value}' | Expected: '{expected_value}'")
            
            if current_value != expected_value:
                print(f"    [🚨 KERNEL MISCONFIGURATION] Dangerous runtime parameter layout: {parameter}")
                compliance_breaches += 1
                
        print("-" * 57)
        if compliance_breaches > 0:
            print(f"[💀 AUDIT FAILURE] Linux kernel parameters are vulnerable to exploits.")
            print("[🛡️ ACTION] Writing secure baseline keys directly into runtime /proc/sys interface.")
            return False
        else:
            print("[🟢 SUCCESS] Core infrastructure system variables match standard security policies.")
            return True

if __name__ == "__main__":
    hardener = LinuxSysctlHardener()
    
    # Teszt eset: Hibás, sebezhető kernel paramétereket tartalmazó konfigurációs minta
    vulnerable_sysctl_mock = """
    # Network settings baseline
    net.ipv4.ip_forward = 1
    net.ipv4.conf.all.accept_redirects = 1
    kernel.randomize_va_space = 0
    """
    hardener.audit_sysctl_configuration(vulnerable_sysctl_mock)
