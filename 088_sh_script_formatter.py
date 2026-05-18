# ==============================================================================
# FÁJL NÉV: 088_sh_script_formatter.py
# SORSZÁM: 088
#
# LEÍRÁS ÉS FELADAT:
# Shell Script Szöveges Formázó és Kompatibilitási (Shell Script Formatter) modul.
# Automatikusan ellenőrzi a .sh fájlok sörvégi karaktereit (Line Endings). 
# Kiszűri a Windows-féle \r\n (CRLF) karaktereket, és átalakítja őket tiszta 
# Linux-féle \n (LF) formátumba. Megakadályozza, hogy a Git Bash vagy a felhős 
# Linux node-ok 'standard syntax error' hibát dobjanak a script futtatásakor.
# ==============================================================================

import os
import sys

class ShScriptFormatter:
    def __init__(self):
        self.log_file = "./sentinel_events.log"

    def enforce_linux_line_endings(self, sh_file_path):
        print("=========================================================")
        print(f"   CYBER-BORSOD INFRA -> SHELL SCRIPT COMPATIBILITY     ")
        print("=========================================================")
        print(f"[*] Analyzing bitstream structure of: {sh_file_path}")
        
        if not os.path.exists(sh_file_path):
            print(f"  [-] Target file not found. Standing by for deployment hooks.")
            print("=========================================================")
            return False

        try:
            # Beolvassuk a fájlt nyers bináris módban
            with open(sh_file_path, "rb") as f:
                content = f.read()

            # Megnézzük, tartalmaz-e Windows-féle bájtokat (\r\n -> b'\r\n')
            if b"\r\n" in content:
                print("  [🚨 COMPLIANCE ANOMALY] Windows-style CRLF line endings detected!")
                print("[*] Normalizing file format to clean Linux LF binary layout...")
                
                # Átalakítás: kicseréljük a b'\r\n'-t sima b'\n'-re
                sanitized_content = content.replace(b"\r\n", b"\n")
                
                with open(sh_file_path, "wb") as f_out:
                    f_out.write(sanitized_content)
                print("[🟢 SUCCESS] File structural bytes normalized. Script is now Posix-compliant.")
            else:
                print("[🟢 COMPLIANT] Script file uses clean Linux LF syntax. No modification needed.")
                
        except Exception as e:
            print(f"[❌ CRITICAL ERROR] Formatting pipeline failed: {e}")
            return False

        print("=========================================================")
        return True

if __name__ == "__main__":
    formatter = ShScriptFormatter()
    # Ellenőrizzük a korábban létrehozott indító scriptet
    formatter.enforce_linux_line_endings("init_pipeline.sh")
