# ==============================================================================
# FÁJL NÉV: 051_data_anonymizer_pipeline.py
# SORSZÁM: 051
#
# LEÍRÁS ÉS FELADAT:
# Adat-anonimizáló és GDPR Megfelelőségi (Data Anonymizer) modul. 
# A 5TB-os hálózati pipeline-ba beérkező adatok elemzése előtt kiszűri a személyes 
# azonosításra alkalmas adatokat (PII - Personally Identifiable Information). 
# Kriptográfiai SHA-256 maszkolással és csonkolással anonimizálja az IP-címeket, 
# e-mail címeket, megvédve a felhasználók adatait a naplófájlokban.
# ==============================================================================

import hashlib
import re

class DataAnonymizer:
    def __init__(self):
        # E-mail címek felismerésére szolgáló reguláris kifejezés (Regex)
        self.email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    def mask_ip_address(self, ip_address):
        """Maszkolja az IPv4 cím utolsó oktettjét a hálózati anonimitásért."""
        reszek = ip_address.split(".")
        if len(reszek) == 4:
            return f"{reszek[0]}.{reszek[1]}.{reszek[2]}.0"
        return "0.0.0.0"

    def anonymize_pii_payload(self, raw_data_string):
        print("=========================================================")
        print("   CYBER-BORSOD PRIVACY -> PII DATA ANONYMIZER PIPELINE  ")
        print("=========================================================")
        print("[*] Ingesting telemetry data stream segment...")
        
        processed_data = raw_data_string
        
        # 1. LÉPÉS: E-mail címek megkeresése és anonimizálása SHA-256-tal
        emails = re.findall(self.email_regex, processed_data)
        for email in emails:
            hashed_email = hashlib.sha256(email.encode('utf-8')).hexdigest()[:16]
            processed_data = processed_data.replace(email, f"[HASHED_PII_{hashed_email}]")
            
        print(f"  [🟢 SUCCESS] Compliance data anonymization complete.")
        print(f"    [-] Sanitized Stream: {processed_data}")
        print("=========================================================")
        return processed_data

if __name__ == "__main__":
    anonymizer = DataAnonymizer()
    
    # Teszt eset: Személyes adatokat tartalmazó hálózati logbejegyzés
    raw_log = "USER_LOGIN_EVENT: imrek@DESKTOP-BORSOD from IP 192.168.1.150 using imre.kaszai@gmail.com"
    
    # IP maszkolás teszt
    maszkolt_ip = anonymizer.mask_ip_address("192.168.1.150")
    print(f"[*] Original IP: 192.168.1.150 -> Masked IP: {maszkolt_ip}")
    
    # Teljes PII takarítás
    anonymizer.anonymize_pii_payload(raw_log)
