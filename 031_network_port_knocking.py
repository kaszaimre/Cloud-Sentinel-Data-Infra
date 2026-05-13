# ==============================================================================
# FÁJL NÉV: 031_network_port_knocking.py
# SORSZÁM: 031
#
# LEÍRÁS ÉS FELADAT:
# Port-Knocking (Kopogásos Portnyitás) védelmi modul. Elrejti a kritikus SSH/API
# menedzsment kapukat a külvilág elől. A tűzfal alapértelmezetten minden bejövő
# kapcsolatot tilt. A modul figyeli a hálózati csomagokat: ha egy kliens egy előre 
# meghatározott, pontos matematikai szekvencia (pl. 7000 -> 8500 -> 9000) szerint 
# "kopogtat" a zárt portokon, a rendszer ideiglenesen megnyitja neki a hozzáférést.
# ==============================================================================

import time

class PortKnockingShield:
    def __init__(self, target_sequence=[7000, 8500, 9000], timeout_seconds=5):
        """
        target_sequence: A helyes port-kopogtatási sorrend.
        timeout_seconds: A maximális idő, ami eltelhet a kopogtatások között.
        """
        self.target_sequence = target_sequence
        self.timeout_seconds = timeout_seconds
        self.client_states = {} # Tárolja a kliensek aktuális kopogtatási állapotát

    def register_knock(self, source_ip, port):
        """Regisztrálja a hálózati kopogtatást egy adott IP-címről."""
        jelenlegi_ido = time.time()
        
        # Ha új kliens, vagy túl sokat várt, alaphelyzetbe állítjuk
        if source_ip not in self.client_states or (jelenlegi_ido - self.client_states[source_ip]["last_seen"] > self.timeout_seconds):
            self.client_states[source_ip] = {"sequence_index": 0, "last_seen": jelenlegi_ido}

        expected_port = self.target_sequence[self.client_states[source_ip]["sequence_index"]]
        
        if port == expected_port:
            self.client_states[source_ip]["sequence_index"] += 1
            self.client_states[source_ip]["last_seen"] = jelenlegi_ido
            print(f"  [🟢 VALID KNOCK] IP: {source_ip} -> Port: {port} | Step {self.client_states[source_ip]['sequence_index']}/{len(self.target_sequence)}")
            
            # Ellenőrizzük, hogy a teljes sorozat sikeres-e
            if self.client_states[source_ip]["sequence_index"] == len(self.target_sequence):
                print(f"\n[🔓 FIREWALL OPENED] IP {source_ip} successfully authenticated via port-knocking!")
                print("  [🛡️ MITIGATION] Temporary production port rule deployed: ALLOW TCP 22 for 60 seconds.")
                self.client_states[source_ip]["sequence_index"] = 0 # Visszaállítás biztonsági okokból
                return True
        else:
            # Rossz kopogtatás esetén azonnali reset a védelem érdekében
            print(f"  [❌ INVALID KNOCK] IP: {source_ip} knocked on wrong Port: {port}. Resetting state sequence.")
            self.client_states[source_ip]["sequence_index"] = 0
            
        return False

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD NETSEC -> PORT-KNOCKING AUTH ENGINE     ")
    print("=========================================================")
    
    shield = PortKnockingShield(target_sequence=[7000, 8500, 9000], timeout_seconds=3)
    teszt_ip = "192.168.1.50"
    
    # 1. Szimuláció: Helyes sorozat tesztelése
    print(f"[*] Simulating correct knocking sequence from: {teszt_ip}")
    shield.register_knock(teszt_ip, 7000)
    time.sleep(0.5)
    shield.register_knock(teszt_ip, 8500)
    time.sleep(0.5)
    shield.register_knock(teszt_ip, 9000)
    
    print("-" * 57)
    
    # 2. Szimuláció: Hibás, gyanús letapogatás tesztelése (Támadás)
    print(f"[*] Simulating port-scan attack or brute-force tracking from: {teszt_ip}")
    shield.register_knock(teszt_ip, 7000)
    shield.register_knock(teszt_ip, 9999) # Hibás lépés, megszakítja a láncot
    
    print("=========================================================")
