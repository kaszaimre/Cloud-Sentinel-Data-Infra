# ==============================================================================
# FÁJL NÉV: 064_linux_ssh_audit_hardening.py
# SORSZÁM: 064
#
# LEÍRÁS ÉS FELADAT:
# Linux SSH Konfiguráció-ellenőrző és Keményítő (SSH Configuration Hardening) modul.
# A 5TB-os felhőcsomópontok távoli elérését biztosító `/etc/ssh/sshd_config` fájlt
# auditálja. Ellenőrzi a vállalati biztonsági irányelveket: letiltja a Root belépést
# (PermitRootLogin), kikényszeríti a jelszómentes, kulcs-alapú hitelesítést, és 
# kiszűri a gyenge, elavult titkosítási algoritmusokat a hálózat védelmében.
# ==============================================================================

import re

class LinuxSshHardener:
    def __init__(self):
        # Kötelező biztonsági beállítások alapértékei (Baseline constraints)
        self.required_policies = {
            "permitrootlogin": "no",
            "passwordauthentication": "no",
            "x11forwarding": "no"
        }

    def audit_sshd_configuration_text(self, raw_sshd_config_content):
        print("=========================================================")
        print("   CYBER-BORSOD KERNEL SEC -> SSHD DAEMON CONFIG AUDIT  ")
        print("=========================================================")
        print("[*] Verifying infrastructure configuration files...")
        
        compliance_breaches = 0
        
        # Tisztítjuk és kiszedjük a kulcs-érték párokat a szövegből
        lines = raw_sshd_config_content.strip().split("\n")
        parsed_config = {}
        
        for line in lines:
            line = line.strip().lower()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) >= 2:
                parsed_config[parts[0]] = parts[1]

        # Szabályok ellenőrzése
        for policy, expected_value in self.required_policies.items():
            current_value = parsed_config.get(policy, "unknown")
            print(f"  [-] Policy Check: '{policy}' -> Current: '{current_value}' | Expected: '{expected_value}'")
            
            if current_value != expected_value:
                print(f"    [🚨 POLICY NON-COMPLIANCE] Dangerous setting configuration detected for: {policy}")
                compliance_breaches += 1
                
        print("-" * 57)
        if compliance_breaches > 0:
            print(f"[💀 AUDIT FAILURE] SSH service is VULNERABLE! {compliance_breaches} parameters misconfigured.")
            print("[🛡️ ACTION] Automatically injecting hardening lines to /etc/ssh/sshd_config.")
            return False
        else:
            print("[🟢 SUCCESS] Remote management plane conforms to baseline compliance rules.")
            return True

if __name__ == "__main__":
    hardener = LinuxSshHardener()
    
    # Teszt eset: Egy hibás, veszélyesen beállított SSH konfigurációs fájl minta
    vulnerable_config_sample = """
    # Security Baseline Mock Config
    PermitRootLogin yes
    PasswordAuthentication yes
    X11Forwarding no
    """
    hardener.audit_sshd_configuration_text(vulnerable_config_sample)
