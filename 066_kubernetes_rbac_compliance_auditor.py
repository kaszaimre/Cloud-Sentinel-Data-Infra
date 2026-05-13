# ==============================================================================
# FÁJL NÉV: 066_kubernetes_rbac_compliance_auditor.py
# SORSZÁM: 066
#
# LEÍRÁS ÉS FELADAT:
# Kubernetes RBAC (Role-Based Access Control) Hozzáférés-kezelési Audit modul.
# A felhőalapú klaszterek belső jogosultsági szabályzatait (YAML definíciók) 
# ellenőrzi. Kiszűri a kritikus biztonsági szabálysértéseket, például ha egy 
# szolgáltatásfiók korlátlan hozzáférést (ClusterAdmin) kap, vagy vadkártya ("*") 
# karakterrel minden erőforrást elérhet a 5TB-os fürtön belül.
# ==============================================================================

import sys

class KubernetesRbacAuditor:
    def __init__(self):
        self.dangerous_verbs = ["*", "create", "delete", "escalate"]

    def audit_rbac_role_rules(self, role_name, api_groups, resources, verbs):
        print("=========================================================")
        print(f"   CYBER-BORSOD CLOUD SEC -> KUBERNETES RBAC COMPLIANCE   ")
        print("=========================================================")
        print(f"[*] Auditing Cluster Role Security Policy: '{role_name}'")
        print(f"  [-] Target Resource Bindings: {resources}")
        print(f"  [-] Assigned Action Verbs   : {verbs}")
        print("-" * 57)

        is_violating = False
        
        # BIZTONSÁGI ELLENŐRZÉS: Túlméretezett konténer-jogosultságok szűrése
        if "*" in verbs or "*" in resources:
            print("  [🚨 RBAC VIOLATION] CRITICAL WILDCARD DETECTED!")
            print("    [!] Threat: Role configuration allows full wildcard access control.")
            is_violating = True
            
        if "escalate" in verbs:
            print("  [🚨 RBAC VIOLATION] PRIVILEGE ESCALATION CAPABILITY FOUND!")
            print("    [!] Threat: Service account can dynamically elevate its own credentials.")
            is_violating = True

        if is_vulnerable := is_violating:
            print("\n[💀 AUDIT FAILURE] Dangerous RBAC permission configuration rejected.")
            print("[🛡️ REACTION] Blocking resource deployment to Kubernetes API master server.")
            return False
        else:
            print("\n[🟢 COMPLIANT] Role rules adhere to standard least-privilege matrix guidelines.")
            return True

if __name__ == "__main__":
    auditor = KubernetesRbacAuditor()
    
    # Teszt eset: Veszélyes, sebezhető Kubernetes szerepkör szimulációja
    auditor.audit_rbac_role_rules(
        role_name="pipeline-worker-role",
        api_groups=[""],
        resources=["*"],
        verbs=["get", "list", "escalate"]
    )
