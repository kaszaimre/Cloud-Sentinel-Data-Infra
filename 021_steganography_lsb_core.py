import os
import sys

# Biztonsági ellenőrzés a Pillow (PIL) könyvtárra, amit az init_pipeline.sh rakott fel
try:
    from PIL import Image
except ImportError:
    print("[!] PIL (Pillow) library missing. Run init_pipeline.sh first!")
    sys.exit(1)

def token_titkositas_kepbe(kep_utvonal, titkos_szoveg, kimeneti_utvonal):
    """Elrejti a titkos szöveget a kép pixeljeinek legalsó bitjeiben (LSB steganográfia)."""
    try:
        kep = Image.open(kep_utvonal)
        szoveg_binaris = ''.join(format(ord(i), '08b') for i in titkos_szoveg) + '1111111111111110' # Lezáró flag
        
        pixelek = list(kep.getdata())
        uj_pixelek = []
        szoveg_index = 0
        
        for pixel in pixelek:
            uj_pixel = list(pixel)
            for i in range(3): # Red, Green, Blue csatornák vizsgálata
                if szoveg_index < len(szoveg_binaris):
                    # Kicseréljük a legalsó bitet a szöveg bitjére
                    uj_pixel[i] = (uj_pixel[i] & ~1) | int(szoveg_binaris[szoveg_index])
                    szoveg_index += 1
            uj_pixelek.append(tuple(uj_pixel))
            
        uj_kep = Image.new(kep.mode, kep.size)
        uj_kep.putdata(uj_pixelek)
        uj_kep.save(kimeneti_utvonal)
        print(f"[🟢 SUCCESS] Token successfully obfuscated inside: {kimeneti_utvonal}")
    except Exception as e:
        print(f"[❌ ERROR] Steganography pipeline failed: {e}")

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD SECURITY -> LSB STEGANOGRAPHY ENGINE    ")
    print("=========================================================")
    # Teszt futtatás: Ha nincs igazi képed, a program csak inicializálja a motort
    print("[*] Steganography core status: READY to parse operational tokens.")
    print("=========================================================")
