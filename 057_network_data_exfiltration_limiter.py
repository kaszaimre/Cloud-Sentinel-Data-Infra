# ==============================================================================
# FÁJL NÉV: 057_network_data_exfiltration_limiter.py
# SORSZÁM: 057
#
# LEÍRÁS ÉS FELADAT:
# Hálózati Adatkicsempészés-korlátozó (Data Exfiltration Limiter) modul.
# A 5TB-os hálózati pipeline és API kapuk kimenő (outbound) adatforgalmát 
# monitorozza bájtszinten. Ha egy külső IP-cím felé irányuló adatfolyam volumene 
# egy előre meghatározott időablakon belül eléri a kritikus riasztási korlátot, 
# a modul azonnal lezárja a hálózati kapcsolatot az adatvagyon védelméért.
# ==============================================================================

import time

class DataExfiltrationLimiter:
    def __init__(self, max_outbound_bytes_per_window=1024*1024*50, window_seconds=60):
        """
        max_outbound_bytes_per_window: Maximális kimenő adatmenet (alapértelmezett: 50MB)
        window_seconds: Időablak hossza (alapértelmezett: 60 másodperc)
        """
        self.max_bytes = max_outbound_bytes_per_window
        self.window = window_seconds
        self.traffic_log = {} # Kliens_IP -> [(időbélyeg, bájtméret), ...]

    def audit_outbound_transfer(self, destination_ip, byte_size):
        print("=========================================================")
        print(f"   CYBER-BORSOD NETSEC -> OUTBOUND EXFILTRATION GUARD    ")
        print("=========================================================")
        print(f"[*] Auditing network egress packet stream to: {destination_ip}")
        print(f"[*] Packet Payload Payload Size       : {byte_size:,} bytes")
        
        jelenlegi_ido = time.time()
        
        if destination_ip not in self.traffic_log:
            self.traffic_log[destination_ip] = []
            
        # Kitisztítjuk az időablakon kívüli régi bejegyzéseket
        self.traffic_log[destination_ip] = [
            (t, b) for t, b in self.traffic_log[destination_ip]
            if jelenlegi_ido - t < self.window
        ]
        
        # Hozzáadjuk a mostani adatküldést
        self.traffic_log[destination_ip].append((jelenlegi_ido, byte_size))
        
        # Kiszámoljuk a teljes kimenő forgalmat az időablakon belül
        total_egress = sum(b for t, b in self.traffic_log[destination_ip])
        print(f"  [-] Total Accumulated Egress Data   : {total_egress:,} / {self.max_bytes:,} bytes")
        print("-" * 57)

        # BIZTONSÁGI ELLENŐRZÉS: Túlhaladta a kritikus adatlimit korlátot?
        if total_egress > self.max_bytes:
            print("  [🚨 SECURITY INTERCEPT] Mass Data Exfiltration Profile Detected!")
            print(f"    [!] Destination IP '{destination_ip}' breached leak thresholds.")
            print("    [🛡️ ACTION] Terminating network interface connection. Session destroyed.")
            return False
            
        print("[🟢 COMPLIANT] Egress traffic verified. Within baseline parameters.")
        return True

if __name__ == "__main__":
    # Teszteléshez szigorított 10MB-os korlát élesítése
    limiter = DataExfiltrationLimiter(max_outbound_bytes_per_window=1024*1024*10)
    target_host = "45.55.3.22"
    
    # 1. Teszt eset: Szabályos, kis méretű adatküldés (4MB)
    limiter.audit_outbound_transfer(target_host, byte_size=1024*1024*4)
    
    print("\n" + "="*57 + "\n")
    
    # 2. Teszt eset: Gyanús, tömeges adatfolyam (újabb 8MB, ami átlépi a 10MB-os határt)
    limiter.audit_outbound_transfer(target_host, byte_size=1024*1024*8)
    print("=========================================================")
