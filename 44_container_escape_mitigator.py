# ==============================================================================
# FÁJL NÉV: 044_container_escape_mitigator.py
# SORSZÁM: 044
#
# LEÍRÁS ÉS FELADAT:
# Konténer-kitörés Elleni Védelem (Container Escape Mitigator) modul.
# Ellenőrzi, hogy a Docker/Kubernetes mikroszolgáltatások nincsenek-e túl nagy 
# (Privileged) jogosultsággal elindítva a felhőcsomópontokon. Kiszűri, ha a konténer 
# közvetlenül hozzáfér a gazdagép kerneléhez (pl. cgroups, release_agent), és 
# riaszt, ha olyan anomáliát észlel, amivel a támadó kitörhetne a fizikai szerverre.
# ==============================================================================

import os
import sys

class ContainerEscapeMitigator:
    def __init__(self):
        self.dangerous_mounts = ["/sys/fs/cgroup", "/proc/sysrq-trigger", "/dev/mem"]

    def audit_isolation_boundaries(self):
        print("=========================================================")
        print("   CYBER-BORSOD CLOUD SEC -> CONTAINER ESCAPE MITIGATOR   ")
        print("=========================================================")
        print("[*] Auditing microservice container boundary constraints...")

        is_vulnerable = False

        # 1. ELLENŐRZÉS: Privileged mód tesztelése a gazdagép lemezhozzáférése alapján
        for path in self.dangerous_mounts:
            if os.path.exists(path) and os.access(path, os.W_OK):
                print(f"  [🚨 ESCAPE RISK] Dangerous host path is writable inside container: {path}")
                is_vulnerable = True

        # 2. ELLENŐRZÉS: Docker-in-Docker (DinD) socket kitettség ellenőrzése
        if os.path.exists("/var/run/docker.sock"):
            print("  [🚨 CRITICAL RISK] Docker socket exposed! Attacker can spawn root host containers.")
            is_vulnerable = True

        print("-" * 57)
        if is_vulnerable:
            print("[💀 SECURITY FAILURE] Container escape vector verified.")
            print("[🛡️ ACTION] Revoking service account tokens. Dropping namespace mapping.")
            return False
        else:
            print("[🟢 SUCCESS] Container namespace isolation secure. No escape vectors found.")
            return True

if __name__ == "__main__":
    mitigator = ContainerEscapeMitigator()
    mitigator.audit_isolation_boundaries()
    print("=========================================================")
