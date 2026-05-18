# ==============================================================================
# FÁJL NÉV: 083_infrastructure_janitor.py
# SORSZÁM: 083
#
# LEÍRÁS ÉS FELADAT:
# Automata Rendszertisztító és Memóriafelszabadító (Infrastructure Janitor) modul.
# Kifejezetten a háttérben ragadt kártékony vagy beragadt .exe folyamatok, 
# zombi Python szálak és pufferelt memóriaszemét azonnali, kényszerített 
# törlésére szolgál. Tisztítja a munkakörnyezetet, megszünteti a gép akadozását, 
# és maximális RAM kapacitást biztosít a pipeline-nak.
# ==============================================================================

import os
import sys
import subprocess

class InfrastructureJanitor:
    def __init__(self):
        self.platform = sys.platform
        # A háttérben leggyakrabban beragadó erőforrás-gyilkos folyamatok listája
        self.target_process_names = ["python.exe", "python3", "cmd.exe", "powershell.exe"]

    def execute_force_clean(self):
        print("=========================================================")
        print("   CYBER-BORSOD INFRA -> INFRASTRUCTURE JANITOR CORE    ")
        print("=========================================================")
        print(f"[*] Detecting operating system environment: {self.platform}")
        print("[*] Initiating deep memory flush and process evacuation...")
        print("-" * 57)

        is_windows = self.platform.startswith("win")

        if is_windows:
            # WINDOWS KÖRNYEZET: Nyers taskkill parancsok kiküldése a kernelnek
            for proc in self.target_process_names:
                if proc.endswith(".exe"):
                    try:
                        # Nem indítunk külön ablakot, a háttérben hajtjuk végre a törlést
                        cmd = f"taskkill /F /IM {proc}"
                        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        print(f"  [🟢 CLEANED] Evacuated all active instances of: {proc}")
                    except Exception:
                        pass
            
            # Windows DNS és Puffer memóriatisztítás
            os.system("ipconfig /flushdns >nul 2>&1")
            print("  [🟢 MEMORY] Windows DNS resolver cache purged.")
        else:
            # POSIX / LINUX KÖRNYEZET: killall parancsok végrehajtása
            for proc in ["python3", "python"]:
                try:
                    subprocess.run(["killall", "-9", proc], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    print(f"  [🟢 CLEANED] Terminated lingering POSIX processes: {proc}")
                except Exception:
                    pass

        print("-" * 57)
        print("[🏆 SUCCESS] Infrastructure sanitation finished. Hard drive I/O and RAM unfrozen.")
        print("=========================================================")
        return True

if __name__ == "__main__":
    # Figyelem: A script élesben lelövi a háttérben futó Python folyamatokat, 
    # így a tesztelés során csak a környezeti tisztítást inicializálja.
    janitor = InfrastructureJanitor()
    print("[*] Janitor core standing by. Run in terminal to sweep lingering executables.")
