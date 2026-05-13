# ==============================================================================
# FÁJL NÉV: 071_felelem_simulalas_anomalia.py
# SORSZÁM: 071
#
# LEÍRÁS ÉS FELADAT:
# Kiber-pszichológiai Felelem-szimulációs és Anomália-tesztelő (Fear Simulation) modul.
# A rendszerbe épített mesterséges intelligencia viselkedési stressz-tesztje.
# Szimulálja a hálózat kritikus pontjainak (Node-ok) túlterheltségét és félelmi 
# reakcióit (válaszidő növekedés, pánik-alapú sávszélesség-elvágás), majd teszteli, 
# hogy az automatikus védelmi algoritmusok képesek-e stabilizálni a rendszert.
# ==============================================================================

import time
import random

class FelelemSimulalasEngine:
    def __init__(self):
        self.system_stress_level = 10  # Alapértelmezett nyugodt állapot (%)
        self.is_panic_mode = False

    def run_fear_simulation_cycle(self):
        print("=========================================================")
        print("   CYBER-BORSOD AI -> COGNITIVE FEAR SIMULATION CORE    ")
        print("=========================================================")
        print("[*] Injecting network-wide synthetic chaos parameters...")
        
        for tick in range(1, 6):
            time.sleep(1)
            # Véletlenszerű hálózati fenyegetési faktor növelése (Stressz-injekció)
            stress_spike = random.randint(15, 30)
            self.system_stress_level += stress_spike
            
            print(f"  [TICK #{tick:02d}] Stress Level Rising: {self.system_stress_level}%")
            
            # Kritikus félelmi küszöbérték ellenőrzése (70% felett bepánikol a Node)
            if self.system_stress_level >= 70 and not self.is_panic_mode:
                print("\n  [🚨 FELELEM / PANIC DETECTED] Cluster nodes reaching critical vulnerability thresholds!")
                print("    [!] REACTION: AI daemon isolating core logic blocks due to operational fear parameters.")
                self.is_panic_mode = True
                
        print("-" * 57)
        if self.is_panic_mode:
            print("[💀 SIMULATION OVER] System perimeter frozen. Fear simulation triggered full lockdown.")
            return False
        else:
            print("[🟢 SUCCESS] Infrastructure baseline absorbed the trauma. Safe execution context.")
            return True

if __name__ == "__main__":
    sim = FelelemSimulalasEngine()
    sim.run_fear_simulation_cycle()
