import socket
import sys

def port_szkenner(ip, port):
    """Ellenőrzi, hogy egy adott port nyitva van-e a routeren."""
    try:
        # Létrehozunk egy szabványos hálózati socketet (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5) # Max 1.5 másodpercig vár a válaszra
        eredmeny = s.connect_ex((ip, port))
        s.close()
        return eredmeny == 0 # Ha 0, akkor a port nyitva van
    except Exception:
        return False

def router_biztonsagi_audit(target_ip):
    print("=========================================================")
    print(f"   ROUTER SECURITY AUDIT PIPELINE -> TARGET: {target_ip}")
    print("=========================================================")
    
    # Kritikus menedzsment portok listája
    # 23: Telnet (Veszélyes), 80: HTTP (Veszélyes), 22: SSH (Biztonságos), 443: HTTPS (Biztonságos)
    kritikus_portok = {
        21: "FTP (Unencrypted File Transfer)",
        23: "Telnet (CRITICAL: Unencrypted Management Plane)",
        80: "HTTP (CRITICAL: Unencrypted Web Interface)",
        22: "SSH (Secure Management Available)",
        443: "HTTPS (Secure Web Interface Available)"
    }
    
    veszely_szint = 0
    print("[*] Scanning core management interfaces...")
    
    for port, nev in kritikus_portok.items():
        if port_szkenner(target_ip, port):
            if port in [21, 23, 80]:
                print(f"  [🚨 RISK FOUND] Port {port} is OPEN: {nev}")
                veszely_szint += 2
            else:
                print(f"  [🟢 COMPLIANT] Port {port} is OPEN: {nev}")
        else:
            print(f"  [-] Port {port} is closed/filtered.")
            
    print("-" * 57)
    if veszely_szint >= 4:
        print("[💀 AUDIT RESULT] CRITICAL: Hardening required. Unencrypted protocols active.")
    elif veszely_szint > 0:
        print("[⚠️ AUDIT RESULT] WARNING: Non-encrypted services detected.")
    else:
        print("[🟢 AUDIT RESULT] SUCCESS: Management plane baseline compliant.")
    print("=========================================================")

if __name__ == "__main__":
    # Teszteléshez a helyi hálózati interfészed (localhost) vagy a saját teszt routered IP-je
    # SOHA ne futtasd olyan hálózaton, amire nincs írásos engedélyed!
    teszt_ip = "127.0.0.1" 
    router_biztonsagi_audit(teszt_ip)
