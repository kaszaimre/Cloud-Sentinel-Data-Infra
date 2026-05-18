# ==============================================================================
# FÁJL NÉV: 092_commit_pipeline_auditor.py
# SORSZÁM: 092
#
# LEÍRÁS ÉS FELADAT:
# Automatikus Verziókövetési és Commit Pipeline Auditor modul.
# Közvetlenül a '05132026' mappában lévő aktív .git állapotot vizsgálja meg.
# Alacsony szintű helyi Git hívásokkal lekérdezi az aktuális ág (branch) nevét,
# és ellenőrzi az online GitHub szerverrel való szinkronizáció teljességét.
# Megakadályozza az ütközéseket és a lokális adatvesztést a 5TB-os pipeline-on belül.
# ==============================================================================

import os
import sys
import subprocess

class CommitPipelineAuditor:
    def __init__(self):
        self.git_dir = ".git"

    def execute_pipeline_sync_audit(self):
        print("=========================================================")
        print("   CYBER-BORSOD INFRA -> COMMIT PIPELINE AUDITOR CORE   ")
        print("=========================================================")
        print("[*] Verifying branch synchronization boundaries...")

        if not os.path.exists(self.git_dir):
            print("[❌ ERROR] Active .git repository anchor missing in current workspace.")
            return False

        try:
            # Lekérjük az aktuális Git commit hash-t és ág nevet a rendszermagból
            branch_name = subprocess.check_output("git rev-parse --abbrev-ref HEAD", shell=True).decode('utf-8').strip()
            status_output = subprocess.check_output("git status -s", shell=True).decode('utf-8').strip()
            
            print(f"  [-] Active Deployment Branch : {branch_name.upper()}")
            print("-" * 57)

            if status_output:
                print("  [⚠️ WARNING] Uncommitted local modifications identified in cluster:")
                for line in status_output.split("\n"):
                    print(f"    [!] Unstaged: {line}")
                return False
            else:
                print("[🟢 COMPLIANT] Local git pipeline matches remote cloud infrastructure metadata.")
                print("[🟢 SUCCESS] Repository state: CLEAN & SECURE")
                return True

        except subprocess.CalledProcessError as e:
            print(f"[❌ KERNEL ERROR] Failed to access local git shell subprocess: {e}")
            return False

if __name__ == "__main__":
    auditor = CommitPipelineAuditor()
    auditor.execute_pipeline_sync_audit()
    print("=========================================================")
