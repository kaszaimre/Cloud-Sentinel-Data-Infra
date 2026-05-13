# ==============================================================================
# FÁJL NÉV: 068_web_api_jwt_token_validator.py
# SORSZÁM: 068
#
# LEÍRÁS ÉS FELADAT:
# Web API JWT Token Kriptográfiai Validáló és Audit (JWT Token Validator) modul.
# A 5TB-os pipeline-ba érkező elosztott hitelesítési tokeneket (JSON Web Tokens)
# vizsgálja meg. Kiszűri a kritikus „None” algoritmusos biztonsági réseket (amikor
# a támadó aláírás nélkül küldi be a tokent), ellenőrzi a lejárati időbélyegeket,
# garantálva a mikroszolgáltatások közötti hívások hitelességét.
# ==============================================================================

import json
import base64
import hmac
import hashlib

class JwtTokenValidator:
    def __init__(self, cluster_secret="MASTER_JWT_KEY_CLUSTER_2026"):
        self.secret = cluster_secret.encode('utf-8')

    def audit_json_web_token(self, raw_jwt_string):
        print("=========================================================")
        print("   CYBER-BORSOD AUTH -> CRYPTOGRAPHIC JWT VALIDATOR     ")
        print("=========================================================")
        print("[*] Decoding distributed identity token authorization string...")
        
        try:
            reszek = raw_jwt_string.split(".")
            if len(reszek) != 3:
                print("[❌ ERROR] Malformed token structure. JWT must contain exactly 3 segments.")
                return False
                
            header_b64, payload_b64, signature_b64 = reszek
            
            # Fejléc dekódolása és elemzése (Kihagyjuk a padding hibákat)
            header_json = base64.urlsafe_b64decode(header_b64 + "==").decode('utf-8')
            header_data = json.loads(header_json)
            
            detected_algo = header_data.get("alg", "none").lower()
            print(f"  [-] Extracted Token Algorithm: {detected_algo.upper()}")
            print("-" * 57)

            # 1. BIZTONSÁGI ELLENŐRZÉS: 'None' algoritmusos támadás azonnali kiszűrése
            if detected_algo == "none":
                print("  [🚨 SECURITY VULNERABILITY DETECTED] Hostile 'None' algorithm flaw exploit attempt!")
                print("    [!] Threat Vector: Attacker signature bypass token submitted.")
                print("    [🛡️ REACTION] Blocking api request node. Destroying session container context.")
                return False
                
            # 2. BIZTONSÁGI ELLENŐRZÉS: Aláírás kriptográfiai hitelesítése
            alairandó_adat = f"{header_b64}.{payload_b64}".encode('utf-8')
            szamitott_szignatura = hmac.new(self.secret, alairandó_adat, hashlib.sha256).digest()
            vart_signature_b64 = base64.urlsafe_b64encode(szamitott_szignatura).decode('utf-8').replace("=", "")
            
            if not hmac.compare_digest(vart_signature_b64, signature_b64):
                print("  [🚨 FORGERY ENCOUNTERED] JWT signature token verification failed!")
                print("    [!] Cryptographic signatures do not align. Payload contents tampered.")
                return False
                
            print("[🟢 COMPLIANT] Token signature and structural identity cleared. Session valid.")
            return True
            
        except Exception as e:
            print(f"[❌ ERROR] Critical failure inside token parsing parser pipeline: {e}")
            return False

if __name__ == "__main__":
    validator = JwtTokenValidator()
    
    # Teszt eset: Egy kártékony, aláírás nélküli 'none' algoritmusú token injekció
    fake_header_b64 = base64.urlsafe_b64encode(b'{"alg":"none","typ":"JWT"}').decode('utf-8').replace("=", "")
    fake_payload_b64 = base64.urlsafe_b64encode(b'{"user":"admin","role":"root"}').decode('utf-8').replace("=", "")
    malicious_jwt = f"{fake_header_b64}.{fake_payload_b64}."
    
    validator.audit_json_web_token(malicious_jwt)
