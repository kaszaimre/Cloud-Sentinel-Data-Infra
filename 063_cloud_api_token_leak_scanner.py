# ==============================================================================
# FÁJL NÉV: 063_cloud_api_token_leak_scanner.py
# SORSZÁM: 063
#
# LEÍRÁS ÉS FELADAT:
# Felhő API Kulcs- és Kiszivárgás-szűrő (API Token Leak Scanner) modul.
# A 5TB-os pipeline-ba kerülő nyers naplófájlokat, konfigurációkat vagy kódrészleteket
# szkenneli a beküldés előtt. Reguláris kifejezésekkel (Regex) automatikusan kiszűri
# és blokkolja, ha egy fejlesztő véletlenül éles felhő jelszót (pl. Google OAuth, 
# AWS Access Key, Slack Webhook) felejtett a szövegekben, megelőzve a szivárgást.
# ==============================================================================

import re

class CloudTokenLeakScanner:
    def __init__(self):
        # Kritikus felhő szolgáltatói API kulcsok regex mintái (Feketelista)
        self.leak_signatures = {
            "Google OAuth Client": r"AIzaSy[a-zA-Z0-9\-_]{33}",
            "AWS Access Key ID"  : r"AKIA[A-Z0-9]{16}",
            "Generic Bearer Token": r"bearer\s+[a-zA-Z0-9_\-\.]{20,}",
            "GitHub Personal Token": r"ghp_[a-zA-Z0-9]{36}"
        }

    def scan_buffer_for_secrets(self, raw_text_buffer):
        print("=========================================================")
        print("   CYBER-BORSOD CLOUD SEC -> TOKEN LEAK DETECTION RECON  ")
        print("=========================================================")
        print("[*] Auditing outbound stream segments for accidental hardcoded secrets...")
        
        leak_detected = False
        
        for credential_type, regex_pattern in self.leak_signatures.items():
            match = re.search(regex_pattern, raw_text_buffer)
            if match:
                print(f"  [🚨 COMPLIANCE VIOLATION] CRITICAL SECRET LEAK IDENTIFIED!")
                print(f"    [!] Threat Type   : {credential_type}")
                print(f"    [!] Leaked Payload: {match.group()[:10]}... [REDACTED]")
                print("    [🛡️ REACTION] Blocking git staging area / pipeline file ingestion.")
                leak_detected = True
                
        if not leak_detected:
            print("[🟢 COMPLIANT] Codebase buffer is sterile. No hardcoded cloud secrets exposed.")
            
        print("=========================================================")
        return not leak_detected

if __name__ == "__main__":
    scanner = CloudTokenLeakScanner()
    
    # Teszt eset: Egy véletlenül bennehagyott Google API kulcs a kódban
    bad_code_sample = "config = {'api_key': 'AIasdfasdfasdfasdfasdfasdfasdfasd', 'timeout': 30}"
    scanner.scan_buffer_for_secrets(bad_code_sample)
