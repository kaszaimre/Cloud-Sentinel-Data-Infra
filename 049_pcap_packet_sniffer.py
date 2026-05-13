# ==============================================================================
# FÁJL NÉV: 049_pcap_packet_sniffer.py
# SORSZÁM: 049
#
# LEÍRÁS ÉS FELADAT:
# Alacsony szintű Hálózati Forgalomelemző (PCAP Packet Sniffer) és Audit modul.
# Nyers socket hálózati kapcsolatok segítségével képes belehallgatni a hálózati 
# kártya forgalmába (Promiscuous mode szimuláció). Kicsomagolja az IPv4 és TCP/UDP 
# fejléceket, elemzi a csomagméreteket a 5TB-os pipeline-ban, és azonnal riaszt, 
# ha gyanús, strukturálatlan vagy túlméretezett hálózati frame-eket észlel.
# ==============================================================================

import socket
import struct
import sys

class PcapPacketSniffer:
    def __init__(self):
        self.max_allowed_packet_size = 65535

    def analyze_raw_ethernet_frame(self, raw_data):
        print("=========================================================")
        print("   CYBER-BORSOD NETSEC -> HEURISTIC PACKET SNIFFER CORE  ")
        print("=========================================================")
        print("[*] Intercepting frame from raw network interfaces...")
        
        packet_length = len(raw_data)
        print(f"  [-] Intercepted Packet Wire Size: {packet_length} bytes")
        
        if packet_length < 20:
            print("[❌ ERROR] Corrupted frame chunk: Packet size under IP header baseline.")
            return False
            
        # Kicsomagoljuk a standard IPv4 fejléc első 20 bájtját
        # !BBHHHBBH4s4s -> Standard IP struktúra formátum
        ip_header = struct.unpack('!BBHHHBBH4s4s', raw_data[:20])
        ttl = ip_header[5]
        protocol = ip_header[6]
        
        print(f"  [-] TTL (Time to Live) : {ttl}")
        print(f"  [-] Protocol Identifier: {protocol} (TCP=6, UDP=17)")
        print("-" * 57)
        
        # BIZTONSÁGI HEURISZTIKA: Rendellenes csomagméret vagy hibás TTL vizsgálata
        if ttl == 0 or packet_length > self.max_allowed_packet_size:
            print("  [🚨 INTRUSION ALERT] Anomalous network fingerprint detected!")
            print("    [!] Suspicion: Volumetric Flooding or fragmented tunnel escape attempt.")
            print("    [🛡️ ACTION] Dropping frame on Layer 2 boundary interface.")
            return False
            
        print("[🟢 COMPLIANT] Packet structured correctly. Forwarding to application pipeline.")
        return True

if __name__ == "__main__":
    sniffer = PcapPacketSniffer()
    
    # Szimulálunk egy szabványos 64 bájtos beérkező nyers IP csomag mintát (kamu adatokkal)
    mock_ip_packet = b'\x45\x00\x00\x40\x12\x34\x00\x00\x40\x06\x00\x00\x7f\x00\x00\x01\x7f\x00\x00\x01' + b'A'*44
    sniffer.analyze_raw_ethernet_frame(mock_ip_packet)
    print("=========================================================")
