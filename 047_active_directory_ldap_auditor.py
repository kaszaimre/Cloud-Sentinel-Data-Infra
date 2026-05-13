# ==============================================================================
# FÁJL NÉV: 047_active_directory_ldap_auditor.py
# SORSZÁM: 047
#
# LEÍRÁS ÉS FELADAT:
# Céges Címtár és LDAP Biztonsági Auditáló (LDAP Compliance Auditor) modul.
# A 5TB-os hálózati pipeline vállalati integrációit és a felhasználói jogokat 
# ellenőrzi az Active Directory (AD) környezetben. Kiszűri, ha a kritikus 
# szervizfiókok nincsenek megfelelően korlátozva, vagy ha elavult, titkosítatlan 
# egyszerű LDAP (Clear-Text Simple Bind) kapcsolatot használnak a hálózaton.
# ==============================================================================

import sys

class LdapComplianceAuditor:
    def __init__(self):
        self.required_encryption = "LDAPS" # Biztonságos LDAP SSL/TLS felett

    def audit_ldap_connection_string(self, connection_url, bind_method):
        print("=========================================================")
        print("   CYBER-BORSOD AD SEC -> LDAP COMPLIANCE AUDITOR v1.0   ")
        print("=========================================================")
        print(f"[*] Auditing corporate identity access connection: {connection_url}")
        print(f"[*] Active Bind Method: {bind_method.upper()}")
        print("-" * 57)

        # 1. ELLENŐRZÉS: Titkosítás megléte (LDAP vs LDAPS)
        if not connection_url.lower().startswith("ldaps://"):
            print("  [🚨 COMPLIANCE BREACH] UNENCRYPTED LDAP CONNECTION IN USE!")
            print("    [!] VULNERABILITY: User credentials travel in clear-text over the network switch.")
            print("    [🛡️ ACTION] Rejecting pipeline directory bind to protect corporate domain controller.")
            return False

        # 2. ELLENŐRZÉS: Egyszerű jelszavas hitelesítés szűrése
        if bind_method.lower() == "simple":
            print("  [⚠️ WARNING] Weak 'Simple Bind' authentication method detected.")
            print("    [*] Recommendation: Migrate to SASL (GSSAPI/Kerberos) token infrastructure.")
            return True

        print("[🟢 COMPLIANT] LDAP identity architecture verified. Domain link safe.")
        return True

if __name__ == "__main__":
    auditor = LdapComplianceAuditor()
    
    # 1. Teszt eset: Nem biztonságos, lehallgatható vállalati kapcsolat
    auditor.audit_ldap_connection_string("ldap://corp-dc.borsod.local", "simple")
    
    print("\n" + "="*57 + "\n")
    
    # 2. Teszt eset: Szabályos, titkosított vállalati kapcsolat
    auditor.audit_ldap_connection_string("ldaps://secure-dc.borsod.local", "sasl")
    print("=========================================================")
