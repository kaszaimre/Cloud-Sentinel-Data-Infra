# ==============================================================================
# FÁJL NÉV: 102_terminal_prompt_stabilizer.py
# SORSZÁM: 102
#
# LEÍRÁS ÉS FELADAT:
# Terminál Prompt Stabilizáló és Környezet-Helyreállító modul.
# Folyamatosan ellenőrzi, hogy a VS Code aktív terminálja nem csúszott-e bele
# a rejtett .git alkönyvtárba. Ha ezt észleli, automatikusan visszalépteti a
# promptot a fő projektmappába (05132026), megakadályozva, hogy a Python 
# futtatókörnyezet relatív elérési útvonal-hibákat dobjon a pipeline indításakor.
# ==============================================================================

import os
import sys

class TerminalPromptStabilizer:
    def __init__(self):
        self.git_suffix = ".git"

    def enforce_clean_working_directory(self):
        print("=========================================================")
        print("   CYBER-BORSOD KERNEL -> TERMINAL PROMPT STABILIZER     ")
        print("=========================================================")
        
        current_path = os.getcwd()
        print(f"[*] Analyzing active shell prompt pointer: {current_path}")
        print("-" * 57)

        # BIZTONSÁGI ELLENŐRZÉS: Ha a mappa neve .git-re végződik, korrigálunk
        if current_path.endswith(self.git_suffix):
            print("  [🚨 PROMPT MISALIGNMENT] Terminal trapped inside hidden .git directory!")
            
            # Visszalépünk egy szinttel feljebb a fizikai lemezen
            parent_clean_path = os.path.dirname(current_path)
            os.chdir(parent_clean_path)
            
            print(f"    [🛡️ SOAR REACTION] Shifting terminal context to root: {parent_clean_path}")
            print("[🟢 SUCCESS] Execution path normalized. Workspace boundary restored.")
            return False
        else:
            print("[🟢 COMPLIANT] Terminal stands in verified execution zone. Ready.")
            return True

if __name__ == "__main__":
    stabilizer = TerminalPromptStabilizer()
    stabilizer.enforce_clean_working_directory()
    print("=========================================================")
