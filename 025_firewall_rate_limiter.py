# ==============================================================================
# FÁJL NÉV: 025_firewall_rate_limiter.py
# SORSZÁM: 025
#
# LEÍRÁS ÉS FELADAT:
# Automatikus hálózati sebességkorlátozó (Rate Limiter) és DDoS-védelmi modul.
# Nyomon követi az érkező kérések időbélyegeit forrás-IP alapján. Ha egy IP-cím
# túllépi a megengedett másodpercenkénti küszöbértéket, a modul javaslatot tesz
# a tűzfalnak a forrás azonnali blokkolására (DROP).
# ==============================================================================

import time

class FirewallRateLimiter:
    def __init__(self, max_requests=5, time_window=2):
        """
        max_requests: Maximálisan megengedett kérések száma
        time_window: Időablak másodpercben
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.ip_history = {}

    def is_request_allowed(self, source_ip):
        """Ellenőrzi, hogy az adott IP-cím küldhet-e újabb kérést."""
        jelenlegi_ido = time.time()
        
        if source_ip not in self.ip_history:
            self.ip_history[source_ip] = []
            
        # Kitisztítjuk a megadott időablakon kívüli régi kéréseket
        self.ip_history[source_ip] = [
            t for t in self.ip_history[source_ip] 
            if jelenlegi_ido - t < self.time_window
        ]
        
        # Ellenőrzés a küszöbértékre
        if len(self.ip_history[source_ip]) >= self.max_requests:
            return False
            
        # Regisztráljuk a sikeres kérést
        self.ip_history[source_ip].append(jelenlegi_ido)
        return True

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD NETSEC -> VOLUMETRIC RATE LIMITER CORE   ")
    print("=========================================================")
    
    # Teszt: 5 kérés engedélyezett 2 másodpercen belül IP-nként
    limiter = FirewallRateLimiter(max_requests=5, time_window=2)
    teszt_ip = "185.220.101.5"
    
    print(f"[*] Simulating high-frequency traffic from target: {teszt_ip}")
    print("-" * 57)
    
    # Szimulálunk 7 gyors egymás utáni kérést
    for i in range(1, 8):
        allowed = limiter.is_request_allowed(teszt_ip)
        if allowed:
            print(f"  [TICK #{i:02d}] Request ALLOWED  from {teszt_ip}")
        else:
            print(f"  [🚨 BLOCK #{i:02d}] Request DROP - Rate limit exceeded on firewall level!")
            
    print("=========================================================")
