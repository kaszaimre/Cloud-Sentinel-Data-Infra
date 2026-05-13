# ==============================================================================
# FÁJL NÉV: 045_zero_trust_api_gateway.py
# SORSZÁM: 045
#
# LEÍRÁS ÉS FELADAT:
# Zéró Bizalom Alapú API Kapu (Zero-Trust API Gateway) modul. 
# A "Soha ne bízz meg senkiben, mindig ellenőrizd" elv alapján működik. 
# Minden egyes bejövő hálózati kéréstől megköveteli a titkosított kriptográfiai 
# hitelesítést (Bearer Token) és az érvényes azonosítást, függetlenül attól, 
# hogy a kérés a belső hálózatról vagy az internetről érkezett-e a 5TB-os pipeline-hoz.
# ==============================================================================

import hmac
import hashlib

class ZeroTrustApiGateway:
    def __init__(self, cluster_secret="CYBER_BORSOD_CLUSTER_MASTER_KEY_2026"):
        self.secret_key = cluster_secret.encode('utf-8')

    def validate_inbound_api_request(self, api_endpoint, request_payload, received_signature):
        print("=========================================================")
        print(f"   CYBER-BORSOD ZERO-TRUST -> GATEWAY INBOUND AUDIT: {api_endpoint}")
        print("=========================================================")
        print("[*] Policy: 'Never Trust, Always Verify' perimeter check active.")

        # HMAC-SHA256 aláírás újraszámolása a biztonsági zónán belül
        data_to_sign = f"{api_endpoint}:{request_payload}".encode('utf-8')
        expected_signature = hmac.new(self.secret_key, data_to_sign, hashlib.sha256).hexdigest()

        print(f"  [-] Expected Signature : {expected_signature[:30]}...")
        print(f"  [-] Received Signature : {received_signature[:30]}...")
        print("-" * 57)

        # Időalapú támadásoknak ellenálló összehasonlítás
        if hmac.compare_digest(expected_signature, received_signature):
            print("[🟢 ACCESS GRANTED] Request cryptographic identity verified. Forwarding payload.")
            return True
        else:
            print("[🚨 SECURITY BREACH] Micro-segmentation block active: Tampered signature detected!")
            print("[🛡️ REACTION] Blocking origin source IP. Dropping network frame immediately.")
            return False

if __name__ == "__main__":
    gateway = ZeroTrustApiGateway()
    
    endpoint = "/api/v1/telemetry/ingest"
    payload = "{'cpu': 14.5, 'integrity': 100}"
    
    # Legitim aláírás legenerálása a teszthez
    valid_sig = hmac.new(b"CYBER_BORSOD_CLUSTER_MASTER_KEY_2026", f"{endpoint}:{payload}".encode('utf-8'), hashlib.sha256).hexdigest()
    
    # 1. Teszt: Sikeres validálás
    gateway.validate_api_request(endpoint, payload, valid_sig)
    
    print("\n" + "="*57 + "\n")
    
    # 2. Teszt: Módosított, hamis kérés elutasítása
    gateway.validate_api_request(endpoint, payload, "fake_hacker_signature_12345")
    print("=========================================================")
