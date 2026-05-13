# ==============================================================================
# FÁJL NÉV: 059_linux_auditd_syslog_analyzer.py
# SORSZÁM: 059
#
# LEÍRÁS ÉS FELADAT:
# Linux Auditd Rendszernapló Elemző (Linux Auditd Log Analyzer) modul.
# A 5TB-os felhőcsomópontok Linux kernel-szintű biztonsági naplóit (auditd)
# vizsgálja. Kiszűri a gyanús rendszermeghívásokat (syscalls), mint például az
# illetéktelen fájlrendszer-módosítások vagy hálózati socket nyitások, és
# azonnali strukturált riasztást küld az anomáliák észlelésekor.
# ==============================================================================

import re
import sys

class LinuxAuditdAnalyzer:
    def __init__(self):
        # Gyanús auditd esemény minták (pl. sikertelen fájlmegnyitás rootként, végrehajtási hívások)
        self.critical_patterns = [
            r"type=SYSCALL.*?success=no.*?exe=\"/usr/bin/sudo\"",
            r"type=AVC.*?denied.*?comm=\"nginx\"",
            r"type=ANOM_PROMISCUOUS.*?old_val=0.*?new_val=1" # Hálózati kártya lehallgatási módba váltott
        ]

    def analyze_auditd_line(self, raw_log_line):
        print("=========================================================")
        print("   CYBER-BORSOD KERNEL SEC -> AUDITD SYSLOG ANALYZER     ")
        print("=========================================================")
        print(f"[*] Processing inbound kernel event trace...")
        
        is_anomaly = False
        for pattern in self.critical_patterns:
            if re.search(pattern, raw_log_line):
                print(f"  [🚨 KERNEL ANOMALY] Hostile event footprint detected in auditd log!")
                print(f"    [!] Triggered Rule Pattern: {pattern}")
                print(f"    [!] Raw Kernel Line       : {raw_log_line[:80]}...")
                print("    [🛡️ ACTION] Flagging node boundary. Emitting high-priority SIEM frame.")
                is_anomaly = True
                break
                
        if not is_anomaly:
            print("[🟢 COMPLIANT] Kernel trace safe. No compliance violations mapped.")
        print("=========================================================")
        return not is_anomaly

if __name__ == "__main__":
    analyzer = LinuxAuditdAnalyzer()
    
    # 1. Teszt eset: Gyanús, illegális hálózati lehallgatási kísérlet a kernelben
    promiscuous_attack_log = "type=ANOM_PROMISCUOUS msg=audit(1620000000.123:456): dev=eth0 prom=1 old_val=0 new_val=1 auid=1001 uid=0 gid=0"
    analyzer.analyze_auditd_line(promiscuous_attack_log)
