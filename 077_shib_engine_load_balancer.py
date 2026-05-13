# ==============================================================================
# FÁJL NÉV: 077_shib_engine_load_balancer.py
# SORSZÁM: 077
#
# LEÍRÁS ÉS FELADAT:
# SHIB Pörkölt Motor Terheléselosztó és Szimulációs (SHIB Engine) modul.
# A 80 aktív Python példány és a 5TB-os adatfolyam belső hálózati forgalmát
# irányítja. Egy egyéni, körbeforgó (Round-Robin) algoritmus segítségével 
# automatikusan elosztja a beérkező adatcsomagokat a szabad felhőcsomópontok
# között. Ha az egyik node túlterhelődik, azonnal átirányítja a forgalmat,
# megelőzve a rendszer lassulását és a reakcióidő romlását.
# ==============================================================================

import time
import random

class ShibEngineLoadBalancer:
    def __init__(self, total_nodes=5):
        # Inicializálunk 5 aktív felhőcsomópontot alapértelmezett 0%-os terheléssel
        self.nodes = {f"NODE-SHIB-{i:02d}": 0 for i in range(1, total_nodes + 1)}
        self.node_list = list(self.nodes.keys())
        self.current_index = 0

    def route_next_data_packet(self, packet_id, packet_size_mb):
        print("=========================================================")
        print("   CYBER-BORSOD ENGINE -> SHIB LOAD BALANCER PIPELINE    ")
        print("=========================================================")
        print(f"[*] Ingesting Packet ID : {packet_id}")
        print(f"[*] Payload Stream Size : {packet_size_mb} MB")
        print("-" * 57)

        # Kijelöljük a következő csomópontot Round-Robin alapon
        target_node = self.node_list[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.node_list)

        # Szimuláljuk a csomópont terhelésének növekedését
        # Minden 50MB adat 10% stresszt jelent a processzornak
        added_load = int(packet_size_mb / 5)
        self.nodes[target_node] += added_load

        print(f"  [🟢 ROUTING SUCCESS] Traffic sent to target: {target_node}")
        print(f"  [-] Assigned Node Current CPU Stress: {self.nodes[target_node]}%")
        print("-" * 57)

        # BIZTONSÁGI ELLENŐRZÉS: Túlterhelődött a kijelölt SHIB csomópont?
        if self.nodes[target_node] >= 80:
            print(f"  [🚨 NODE OVERLOAD] {target_node} reached critical capacity!")
            print("    [!] REACTION: Initiating automated failover and dynamic resource throttling.")
            print("    [🛡️ ACTION] Offloading extra thread slices to secondary cold backup nodes.")
            self.nodes[target_node] = 20 # Kényszerített tehermentesítés szimulációja
            
        print("=========================================================")

if __name__ == "__main__":
    balancer = ShibEngineLoadBalancer()
    
    # Szimulálunk 3 gyors egymás utáni adatcsomag érkezést
    balancer.route_next_data_packet("PKT-94820", packet_size_mb=35.0)
    time.sleep(0.5)
    balancer.route_next_data_packet("PKT-94821", packet_size_mb=45.0)
