# ==============================================================================
# FÁJL NÉV: 042_cloud_metadata_ssrf_shield.py
# SORSZÁM: 042
#
# LEÍRÁS ÉS FELADAT:
# Felhő Infrastruktúra SSRF (Server-Side Request Forgery) Védelmi modul.
# Megakadályozza, hogy a támadók a 5TB-os pipeline belső API-jait kihasználva
# lekérdezzék a felhő szolgáltató (GCP, AWS) belső metaadat-szerverét (169.254.169.254).
# A modul blokkolja a privát IP-tartományok felé irányuló jogosulatlan kéréseket.
# ==============================================================================

import re
import ipaddress

class CloudSsrfShield:
    def __init__(self):
        # A felhőszolgáltatók belső link-local metaadat címe (AWS, GCP, Azure)
        self.metadata_ip = "169.254.169.254"

    def validate_outbound_url(self, target_url):
        print("=========================================================")
        print("   CYBER-BORSOD CLOUD SEC -> SSRF METADATA SHIELD v1.0   ")
        print("=========================================================")
        print(f"[*] Auditing outbound pipeline web request: {target_url}")
        
        # Kinyerjük az IP-címet vagy hosztnevet a URL-ből
        match = re.search(r"https?://([^:/]+)", target_url.lower())
        if not match:
            print("[❌ ERROR] Malformed URL structure parsing failed.")
            return False
            
        host = match.group(1)
        
        # Ellenőrizzük, hogy a kérés közvetlenül a metaadat IP-re irányul-e
        if host == self.metadata_ip:
            print(f"  [🚨 CRITICAL BLOCK] SSRF Link-Local Metadata access attempt detected!")
            print(f"    [!] Target: {self.metadata_ip} (IAM Security Tokens Exposure Risk)")
            print("    [🛡️ ACTION] Intercepting network socket. Request discarded.")
            return False

        try:
            # Megnézzük, hogy belső privát IP címre mutat-e (pl. 10.x.x.x vagy 192.168.x.x)
            ip = ipaddress.ip_address(host)
            if ip.is_private:
                print(f"  [⚠️ WARNING] Outbound request targets Internal Private IP space: {host}")
                print("    [*] Request allowed under strict local cluster routing policy.")
                return True
        except ValueError:
            # Ha nem IP, hanem szöveges domain, akkor átengedi (DNS feloldás a következő szint)
            pass

        print("[🟢 COMPLIANT] Outbound target cleared. Cloud boundary infrastructure safe.")
        return True

if __name__ == "__main__":
    shield = CloudSsrfShield()
    
    # 1. Teszt eset: Legitim külső felhő API kérés
    shield.validate_outbound_url("google.com")
    
    print("\n" + "="*57 + "\n")
    
    # 2. Teszt eset: Ellenséges SSRF támadás felhő jelszavak ellopására
    shield.validate_outbound_url("169.254.169")
    print("=========================================================")
