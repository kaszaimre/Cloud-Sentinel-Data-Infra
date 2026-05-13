# ==============================================================================
# FÁJL NÉV: 033_sql_injection_waf_filter.py
# SORSZÁM: 033
#
# LEÍRÁS ÉS FELADAT:
# Webes Alkalmazásszintű Tűzfal (WAF) és SQL Injection (SQLi) szűrő modul.
# Heurisztikus és szignatúra-alapú elemzéssel vizsgálja a 5TB-os pipeline-ba 
# érkező adatbázis-lekérdezési paramétereket. Ha a beviteli mezőkben kártékony 
# adatbázis-módosító mintákat (pl. ' OR 1=1 --, UNION SELECT) észlel, azonnal 
# blokkolja a kérést, megelőzve az adatszivárgást.
# ==============================================================================

import re

class SqlInjectionWafFilter:
    def __init__(self):
        # Szigorú kiberbiztonsági SQLi aláírás-gyűjtemény (Feketelista)
        self.malicious_sql_signatures = [
            r"/\*.*?\*/",                         # Beágyazott SQL megjegyzések
            r"(--|\s#|\s\/\*)",                   # Sorvégi lezáró karakterek
            r"\b(union\s+all\s+select|union\s+select)\b", # Keresztlekérdezéses adathalászat
            r"\b(select|insert|update|delete|drop|alter|truncate)\b.*?\b(from|into|table|database)\b", # illetéktelen adatmanipuláció
            r"'\s*(or|and)\s+\d+\s*=\s*\d+",       # Tautológia alapú hitelesítési megkerülés (pl. ' OR 1=1)
            r"'\s*(or|and)\s+'.*?'\s*=\s*'",      # Szöveges logikai megkerülés
            r"\bexec\b.*?\b(xp_cmdshell|sp_)\b"    # Alacsony szintű operációs rendszer parancsvégrehajtás
        ]

    def inspect_inbound_payload(self, http_parameter):
        """Átvizsgálja a beérkező HTTP/API paraméter szövegét SQL injection jelek után."""
        cleaned_param = str(http_parameter).lower().strip()
        
        for signature in self.malicious_sql_signatures:
            if re.search(signature, cleaned_param):
                print(f"  [🚨 WAF BLOCK] SQL Injection signature detected in payload string!")
                print(f"    [-] Triggered Pattern : {signature}")
                print(f"    [-] Untrusted Input    : {http_parameter}")
                return False
                
        return True

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD WAF -> SQL INJECTION INTRUSION FILTER   ")
    print("=========================================================")
    
    waf = SqlInjectionWafFilter()
    
    # 1. Teszt eset: Legitim felhasználói név bevitele
    legit_input = "don_mernok_admin"
    print(f"[*] Analyzing legitimate API parameter: '{legit_input}'")
    if waf.inspect_inbound_payload(legit_input):
        print("  [🟢 COMPLIANT] Parameter cleared. Forwarding query to BigQuery/SQL cluster.")
    else:
        print("  [❌ DROP] Request rejected by application firewall layer.")
        
    print("-" * 57)
    
    # 2. Teszt eset: Kártékony SQL Injection támadás
    malicious_attack = "admin' OR 1=1 --"
    print(f"[!] Analyzing hostile authentication bypass attempt: '{malicious_attack}'")
    if waf.inspect_inbound_payload(malicious_attack):
        print("  [🟢 COMPLIANT] Parameter cleared.")
    else:
        print("  [❌ DROP] Request intercepted. Mitigation logged in central syslog pipeline.")
        
    print("=========================================================")
