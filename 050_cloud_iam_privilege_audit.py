# ==============================================================================
# FÁJL NÉV: 050_cloud_iam_privilege_audit.py
# SORSZÁM: 050
#
# LEÍRÁS ÉS FELADAT:
# Felhő Alapú Identitás- és Hozzáférés-kezelési (IAM) Compliance és Audit modul.
# A 5TB-os felhőcsomópontok és szolgáltatásfiókok (Service Accounts) kulcsait, 
# jogosultsági szintjeit vizsgálja a "Legkisebb Jogosultság Elve" (Principle of 
# Least Privilege) alapján. Automatikusan kiszűri a túlméretezett, veszélyes 
# adminisztrátori jogköröket (pl. '*' vagy Owner), megelőzve az infrastruktúra 
# teljes kompromittálódását egy esetleges kulcsszivárgás esetén.
# ==============================================================================

import sys

class CloudIamAuditor:
    def __init__(self):
        self.critical_overprivileged_roles = ["owner", "admin", "storage.admin", "*"]

    def audit_iam_policy_statement(self, service_account_email, assigned_role, resource_boundary):
        print("=========================================================")
        print("   CYBER-BORSOD CLOUD SEC -> IAM COMPLIANCE AUDIT CORE   ")
        print("=========================================================")
        print(f"[*] Auditing Access Controls for Identity: {service_account_email}")
        print(f"[*] Assigned Role Capability        : {assigned_role.upper()}")
        print(f"[*] Resource Boundary Scope         : {resource_boundary}")
        print("-" * 57)

        # 1. BIZTONSÁGI ELLENŐRZÉS: Túlméretezett jogkörök és vadkártyák (*) szűrése
        is_overprivileged = False
        for dangerous_role in self.critical_overprivileged_roles:
            if dangerous_role in assigned_role.lower() or resource_boundary == "*":
                is_overprivileged = True
                break

        if is_overprivileged:
            print("  [🚨 IAM VIOLATION] OVERPRIVILEGED CLOUD ACCOUNT DETECTED!")
            print(f"    [!] RISK: Service Account breaches least-privilege compliance guidelines.")
            print("    [🛡️ ACTION] Flagging policy for automated IAM rolling degradation.")
            return False
        else:
            print("[🟢 COMPLIANT] Identity policy restricted to tight operational context. Safe.")
            return True

if __name__ == "__main__":
    auditor = CloudIamAuditor()
    
    # 1. Teszt eset: Veszélyes, túl nagy jogkörrel rendelkező fiók
    auditor.audit_iam_policy_statement(
        service_account_email="pipeline-worker@://gserviceaccount.com",
        assigned_role="roles/owner",
        resource_boundary="*"
    )
    
    print("\n" + "="*57 + "\n")
    
    # 2. Teszt eset: Szabályos, szigorúan korlátozott szolgáltatásfiók
    auditor.audit_iam_policy_statement(
        service_account_email="telemetry-writer@://gserviceaccount.com",
        assigned_role="roles/storage.objectCreator",
        resource_boundary="buckets/raw_market_data_2026"
    )
    print("=========================================================")
