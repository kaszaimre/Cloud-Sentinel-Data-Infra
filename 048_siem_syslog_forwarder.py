# ==============================================================================
# FÁJL NÉV: 048_siem_syslog_forwarder.py
# SORSZÁM: 048
#
# LEÍRÁS ÉS FELADAT:
# Központi SIEM (Security Information and Event Management) Syslog Továbbító modul.
# A 5TB-os hálózati pipeline és a Sentinel által generált kritikus riasztásokat 
# és incidenseket szabványos RFC 5424 formátumú Syslog üzenetekké alakítja, majd 
# biztonságos UDP/TCP csatornán keresztül továbbítja a központi SOC elemző 
# szerverek (pl. Splunk, ELK Stack) felé.
# ==============================================================================

import socket
import sys
from datetime import datetime

class SiemSyslogForwarder:
    def __init__(self, siem_host="127.0.0.1", siem_port=514):
        self.siem_host = siem_host
        self.siem_port = siem_port

    def forward_security_incident(self, severity_level, component, event_msg):
        """
        RFC 5424 alapú riasztást generál és küld a SIEM központnak.
        severity_level: CRITICAL (1), WARNING (4), INFO (6)
        """
        print("=========================================================")
        print(f"   CYBER-BORSOD SIEM -> SYSLOG STREAMING PIPELINE        ")
        print("=========================================================")
        
        # RFC 5424 formátum: <PRI>TIMESTAMP HOSTNAME APP-NAME PROCID MSGID MSG
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        priority = 10 if severity_level.upper() == "CRITICAL" else 30
        
        syslog_frame = f"<{priority}>1 {timestamp} Local-Sandbox-PC {component} - - - [SEC-ALERT] {event_msg}"
        
        print(f"[*] Packaging Inbound Telemetry Frame...")
        print(f"  [-] Raw Syslog Data: {syslog_frame[:70]}...")
        
        try:
            # UDP Socket nyitása és az üzenet azonnali továbbítása
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(syslog_frame.encode('utf-8'), (self.siem_host, self.siem_port))
            sock.close()
            print(f"[🟢 SUCCESS] Event packets streamed to SIEM target at {self.siem_host}:{self.siem_port}")
            return True
        except Exception as e:
            print(f"[❌ NETWORK ERROR] Failed to reach SIEM log collector: {e}")
            return False

if __name__ == "__main__":
    forwarder = SiemSyslogForwarder()
    
    # Teszt riasztás küldése a SIEM rendszer felé
    forwarder.forward_security_incident(
        severity_level="CRITICAL", 
        component="SENTINEL_CORE", 
        event_msg="Unauthorized process termination bypass attempt mitigated."
    )
    print("=========================================================")
