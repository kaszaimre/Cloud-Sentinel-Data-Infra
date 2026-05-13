# ==============================================================================
# FÁJL NÉV: 035_tls_certificate_validator.py
# SORSZÁM: 035
#
# LEÍRÁS ÉS FELADAT:
# TLS Tanúsítvány Érvényességi és Biztonsági Ellenőrző (TLS Certificate Validator) 
# modul. A 5TB-os hálózati pipeline és API csomópontok titkosított HTTPS/TLS 
# kapcsolatait auditálja. Ellenőrzi a tanúsítványok lejárati idejét, a titkosító 
# algoritmus erősségét (SHA256 vagy újabb), és riaszt, ha elavult, lehallgatható 
# (pl. MD5, SHA1) vagy lejárt SSL/TLS tanúsítványt észlel a hálózaton.
# ==============================================================================

import sys
from datetime import datetime, timedelta

class TlsCertificateValidator:
    def __init__(self, warning_days_threshold=30):
        self.warning_days_threshold = warning_days_threshold
        self.unsafe_algorithms = ["md5", "sha1", "rc4"]

    def audit_tls_metadata(self, endpoint_domain, cipher_algorithm, expiration_date_str):
        """
        Auditálja a beérkező TLS kapcsolat metaadatait.
        expiration_date_str formátum: 'YYYY-MM-DD'
        """
        print("=========================================================")
        print(f"   CYBER-BORSOD CRYPTO -> TLS CRYPTO AUDIT: {endpoint_domain}")
        print("=========================================================")
        print(f"[*] Active Cipher Suite Algorithm: {cipher_algorithm.upper()}")
        
        # 1. BIZTONSÁGI ELLENŐRZÉS: Elavult, tört algoritmusok szűrése
        if cipher_algorithm.lower() in self.unsafe_algorithms:
            print(f"  [🚨 SEC-ALERT] UNTRUSTED CRYPTOGRAPHIC ALGORITHM DETECTED!")
            print(f"    [!] Cryptographic signature method '{cipher_algorithm}' is structurally broken.")
            print("    [🛡️ REACTION] Connection dropped to prevent Man-in-the-Middle (MitM) decryption.")
            return False

        # 2. BIZTONSÁGI ELLENŐRZÉS: Lejárati idő validálása
        try:
            lejarat_datum = datetime.strptime(expiration_date_str, "%Y-%m-%d")
            jelenlegi_ido = datetime.now()
            hatralevo_ido = lejarat_datum - jelenlegi_ido
            
            print(f"[*] Certificate Expiration Date : {expiration_date_str} ({hatralevo_ido.days} days left)")
            print("-" * 57)

            if hatralevo_ido.days < 0:
                print("  [🚨 COMPLIANCE VIOLATION] TLS Certificate has EXPIRED!")
                print("    [!] Secure communication channel cannot be established.")
                return False
            elif hatralevo_ido.days <= self.warning_days_threshold:
                print(f"  [⚠️ WARNING] TLS Certificate is nearing expiration (under {self.warning_days_threshold} days)!")
                print("    [*] Automated renewal pipeline should be triggered immediately.")
                return True
            else:
                print("[🟢 COMPLIANT] TLS encryption architecture verified. Session cleared.")
                return True
                
        except ValueError:
            print("[❌ ERROR] Invalid date format signature received for verification pipeline.")
            return False

if __name__ == "__main__":
    validator = TlsCertificateValidator()
    
    # 1. Teszt eset: Legitim, biztonságos TLS kapcsolat
    validator.audit_tls_metadata(
        endpoint_domain="api.cyberborsod.cloud", 
        cipher_algorithm="sha256", 
        expiration_date_str="2026-09-15"
    )
    
    print("\n" + "="*57 + "\n")
    
    # 2. Teszt eset: Veszélyes, elavult/tört TLS kapcsolat szimulációja
    validator.audit_tls_metadata(
        endpoint_domain="legacy-node.cyberborsod.local", 
        cipher_algorithm="md5", 
        expiration_date_str="2026-01-10"
    )
    print("=========================================================")
