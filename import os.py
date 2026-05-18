import os
import re

def konyvtar_kicsomagolo(gyujto_fajl_ut):
    """
    Beolvas egyetlen óriási szövegfájlt, és automatikusan
    szétvágja különálló .py fájlokká a megadott szignatúrák alapján.
    """
    if not os.path.exists(gyujto_fajl_ut):
        print(f"[❌] A gyűjtőfájl nem található: {gyujto_fajl_ut}")
        return

    with open(gyujto_fajl_ut, "r", encoding="utf-8") as f:
        tartalom = f.read()

    # Regex minta, ami megkeresi a fájlneveket és a hozzájuk tartozó kódblokkokat
    # Elvárás a gyűjtőfájlban: ### START_FILE: nev.py ... kód ... ### END_FILE
    mintak = re.findall(r"### START_FILE:\s*([a-zA-Z0-9_\-\.]+)\n(.*?)\n### END_FILE", tartalom, re.DOTALL)

    if not mintak:
        print("[!] Nem találhatóak szabványos fájl-szignatúrák a szövegben.")
        return

    print(f"[*] Észlelve: {len(mintak)} automatizált Python modul. Kicsomagolás indítása...")
    
    for fajlnev, kod in mintak:
        # Biztonságos mentés: kiszedjük az esetleges felesleges üres sorokat a kód elejéről/végéről
        tiszta_kod = kod.strip()
        
        with open(fajlnev, "w", encoding="utf-8") as f_out:
            f_out.write(tiszta_kod + "\n")
        print(f"  [🟢 KIMENTVE] -> {fajlnev}")

    print("[🏆 SUCCESS] A tömeges kódmentés és struktúra-helyreállítás lefutott.")

if __name__ == "__main__":
    # Ide gyűjtsd össze az 50 kódodat a telefonról egyetlen txt-be
    konyvtar_kicsomagolo("gemini_all_codes.txt")
