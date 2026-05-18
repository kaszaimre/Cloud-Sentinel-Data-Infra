# ==============================================================================
# FÁJL NÉV: 089_git_repository_path_resolver.py
# SORSZÁM: 089
#
# LEÍRÁS ÉS FELADAT:
# Git Repozitórium Útvonal-ellenőrző és Validáló (Repository Path Resolver) modul.
# Automatikusan ellenőrzi az aktuális munkakönyvtárat a 5TB-os pipeline indítása 
# és a Git parancsok kiadása előtt. Megvizsgálja a rejtett .git mappa jelenlétét. 
# Ha a felhasználó rossz alkönyvtárban áll (pl. nem inicializált mappában), 
# figyelmeztetést dob, és megkeresi a szülőkönyvtárakban a helyes Git gyökeret.
# ==============================================================================

import os
import sys

class GitRepositoryPathResolver:
    def __init__(self):
        self.current_working_dir = os.getcwd()

    def verify_git_root_compliance(self):
        print("=========================================================")
        print("   CYBER-BORSOD INFRA -> GIT REPOSITORY PATH RESOLVER    ")
        print("=========================================================")
        print(f"[*] Scanning active workspace directory: {self.current_working_dir}")
        
        target_path = self.current_working_dir
        is_valid_git_repo = False
        
        # Ellenőrizzük, hogy a rejtett .git mappa létezik-e az aktuális helyen
        if os.path.exists(os.path.join(target_path, ".git")):
            is_valid_git_repo = True
        else:
            print("  [🚨 PATH MISALIGNMENT] Active directory is not a verified Git repository!")
            print("    [!] Threat: Executing git commands here will trigger fatal shell tracking errors.")
            
            # Megpróbáljuk megkeresni a szülőkönyvtárban (egy szinttel feljebb)
            parent_path = os.path.dirname(target_path)
            if os.path.exists(os.path.join(parent_path, ".git")):
                print(f"    [🟢 RESOLVED] Found valid Git root deployment zone at: {parent_path}")
                print(f"    [🛡️ ACTION] Recommendation: Execute 'cd ..' in your terminal interface.")
                is_valid_git_repo = False
                
        print("-" * 57)
        if is_valid_git_repo:
            print("[🟢 COMPLIANT] Working directory structure verified. Git operations cleared.")
            return True
        else:
            print("[❌ ACCESS LOCKED] Adjust terminal paths before structural sync loops.")
            return False

if __name__ == "__main__":
    resolver = GitRepositoryPathResolver()
    resolver.verify_git_root_compliance()
    print("=========================================================")
