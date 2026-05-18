# ==============================================================================
# FÁJL NÉV: 126_auto_infrastructure_indexer.py
# SORSZÁM: 126
#
# LEÍRÁS ÉS FELADAT:
# Automatikus Infrastruktúra Indexelő és README Dokumentáció Generáló modul.
# Végigpásztázza az aktuális munkakönyvtárat, kigyűjti az összes .py fájlt,
# és a kódok belső fejléc-kommentjeiből automatikusan felépít egy tiszta,
# átlátható Markdown táblázatot a GitHub főoldalára. Így egyetlen pillantásból
# tudni lehet, melyik sorszámú modul miért felel a rendszerben.
# ==============================================================================

import os
import re

class AutoInfrastructureIndexer:
    def __init__(self):
        self.output_readme = "README.md"

    def parse_header_description(self, file_path):
        """Kiolvassa a fájl fejlécéből a leírást."""
        description = "Nincs rögzített leírás."
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Megkeressük a LEÍRÁS ÉS FELADAT blokkot a kommentekben
                match = re.search(r"LEÍRÁS ÉS FELADAT:(.*?)(====|# ---)", content, re.DOTALL | re.IGNORECASE)
                if match:
                    description = match.group(1).replace("#", "").strip()
                    # Egysorossá alakítjuk a táblázat kedvéért
                    description = " ".join(description.split())
        except Exception:
            pass
        return description

    def generate_system_map(self):
        print("=========================================================")
        print("   PURE LOGIC CORE -> AUTO INFRASTRUCTURE INDEXER       ")
        print("=========================================================")
        print("[*] Scanning workspace for Python infrastructure nodes...")
        
        py_files = sorted([f for f in os.listdir(".") if f.endswith(".py")])
        
        if not py_files:
            print("[❌ ERROR] No Python architecture files found in this path.")
            return False

        try:
            with open(self.output_readme, "w", encoding="utf-8") as f:
                # GitHub főoldali látványos fejléc
                f.write("# 🛡️ Cloud-Sentinel-Data-Infra\n\n")
                f.write("Nagyvállalati szintű elosztott adatinfrastruktúra és kiberbiztonsági rendszer.\n\n")
                f.write("## 🗂️ Automatizált Rendszertérkép és Moduljegyzék\n\n")
                
                # Markdown táblázat struktúra legenerálása
                f.write("| Sorszám / Fájlnév | Funkcionális Rendszerleírás |\n")
                f.write("| :--- | :--- |\n")
                
                for file_name in py_files:
                    # Kihagyjuk magát az indexelőt a listából
                    if file_name == "126_auto_infrastructure_indexer.py":
                        continue
                    desc = self.parse_header_description(file_name)
                    f.write(f"| `{file_name}` | {desc} |\n")
                    
            print(f"  [🟢 SUCCESS] Master '{self.output_readme}' successfully compiled.")
            print(f"    [-] Total mapped architectural nodes: {len(py_files) - 1}")
        except Exception as e:
            print(f"  [❌ CRITICAL] Documentation bridge pipeline broken: {e}")

if __name__ == "__main__":
    indexer = AutoInfrastructureIndexer()
    indexer.generate_system_map()
    print("=========================================================")
