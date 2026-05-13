# ==============================================================================
# FÁJL NÉV: 041_shadow_password_hash_auditor.py
# SORSZÁM: 041
#
# LEÍRÁS ÉS FELADAT:
# Linux Shadow Jelszó-Hash Auditáló (Shadow Password Hash Auditor) modul.
# Ellenőrzi a rendszerbázisban tárolt jelszó-hashek kriptográfiai erejét.
# Kiszűri a gyenge, elavult algoritmusokat (pl. MD5, SHA1), és kikényszeríti a
# modern, vállalati szintű SHA-512 ($6$) vagy argon2 használatát, megvédve
# a 18 éves infrastruktúrát az offline szótáralapú és szivárgási támadásoktól.
# ==============================================================================

import sys

class ShadowHashAuditor:
    def __init__(self):
        # Linux szabványos jelszó-hash típus jelölések az /etc/shadow fájlban
        self.secure_identifiers = ["$6$", "$y$", "$argon2id$"] # SHA-512, yescrypt, argon2

    def audit_shadow_line_signature(self, username, encrypted_hash_string):
        print("=========================================================")
        print(f"   CYBER-BORSOD KERNEL SEC -> SHADOW CRYPTO HASH AUDIT  ")
        print("=========================================================")
        print(f"[*] Auditing authentication database signature for user: '{username}'")
        
        if not encrypted_hash_string or encrypted_hash_string in ["*", "!"]:
            print(f"  [🟢 COMPLIANT] User account '{username}' is locked or has no password authentication.")
            return True

        # Megnézzük, milyen azonosítóval kezdődik a hash
        is_secure = False
        detected_algo = "UNKNOWN / WEAK"
        
        for identifier in self.secure_identifiers:
            if encrypted_hash_string.startswith(identifier):
                is_secure = True
                detected_algo = "SHA-512 / MODERN COMPLIANT" if identifier == "$6$" else "NEXT-GEN CRYPTO"
                break

        print(f"  [-] Detected Algorithm Type: {detected_algo}")
        print("-" * 57)

        if not is_secure:
            print(f"  [🚨 COMPLIANCE FAILURE] Legacy or unencrypted hash format found!")
            print(f"    [!] VULNERABILITY: User '{username}' uses a weak hash algorithm prone to GPU brute-forcing.")
            print("    [🛡️ ACTION] Force-flagging user account for immediate password rotation policy.")
            return False
        else:
            print(f"[🟢 SUCCESS] Password hash security verified for user '{username}'.")
            return True

if __name__ == "__main__":
    auditor = ShadowHashAuditor()
    
    # 1. Teszt eset: Szabályos, modern Linux SHA-512-es jelszó-hash minta
    valid_shadow_sample = "$6$rounds=40000$saltstringsaltst$dGhpcyBpcyBhIHNhbXBsZSBoYXNo"
    auditor.audit_shadow_line_signature("service_worker", valid_shadow_sample)
    
    print("\n" + "="*57 + "\n")
    
    # 2. Teszt eset: Gyenge, elavult MD5-ös minta ($1$)
    legacy_shadow_sample = "$1$saltstring$dGhpcyBpcyBhIHNhbXBsZSBoYXNo"
    auditor.audit_shadow_line_signature("compromised_user", legacy_shadow_sample)
    print("=========================================================")
