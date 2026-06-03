from pathlib import Path
import re

def list_and_extract_info():
    # A projekt könyvtárának elérése
    base_dir = Path('.')
    
    # Kigyűjtjük az összes .py fájlt, ami a mintázatodra illik (pl. 088_... .py)
    # A .glob('*_*.py') automatikusan megtalálja az összeset, 
    # nem kell tartományokkal (range) szenvedni.
    files = sorted(base_dir.glob('*_*.py'))
    
    print(f"--- Moduljegyzék ({len(files)} fájl található) ---")
    
    for file in files:
        # A fájl tartalma alapján kinyerjük a leírást (mint a 088_... scriptnél)
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Megkeressük a LEÍRÁS sort
                match = re.search(r'# LEÍRÁS ÉS FELADAT:\n# (.*)', content)
                description = match.group(1) if match else "Nincs leírás."
                
                # Kiírjuk a README-be illeszthető formátumban
                print(f"| {file.name} | {description} |")
        except Exception as e:
            print(f"| {file.name} | Hiba a fájl olvasásakor: {e} |")

if __name__ == "__main__":
    list_and_extract_info()
