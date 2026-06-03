# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 160_BORSODI_BRIGAD_STEGANOGRAPHY_LSB
# 
# LEÍRÁS (HU):
# Képalapú információ-elrejtő modul (LSB - Least Significant Bit technika).
# Lehetővé teszi hadi utasítások és bizalmas adatok beágyazását képfájlok 
# pixeladataiba, láthatatlan módon. Bot-biztos operátori csatorna.
# Mottó: "A borsodi nem hackel, a borsodi optimalizál."
#
# DESCRIPTION (EN):
# Image-based data hiding module (LSB - Least Significant Bit technique).
# Enables embedding sensitive instructions and data into image pixel data 
# invisibly. Bot-proof operator channel.
# Motto: "The Borsodi doesn't hack, the Borsodi optimizes."
#
# SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM
# ==============================================================================

import time
from PIL import Image

# Modul specifikáció az automatizált README generátorhoz
module_desc = "160_BORSODI_BRIGAD_STEGANOGRAPHY_LSB"

CYAN    = "\033[1;36m"
GREEN   = "\033[1;32m"
RED     = "\033[1;31m"
RESET   = "\033[0m"

def text_to_bin(text):
    """Átalakítja a szöveget bináris formátumba (0-k és 1-ek)"""
    return ''.join(format(ord(char), '08b') for char in text) + '1111111111111110' # Stoppoló jel

def bin_to_text(binary_string):
    """Visszaalakítja a bináris kódot tiszta szöveggé"""
    bytes_data = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    decoded_text = ""
    for byte in bytes_data:
        if byte == '11111111' or len(byte) < 8: # Ha elérte a lezáró jelet
            break
        decoded_text += chr(int(byte, 2))
    return decoded_text

# ==============================================================================
# FUNKCIÓ: encode_image()
# LEÍRÁS: Beoltja a képet a titkos szöveggel az LSB (legalsó bit) technikával.
# ==============================================================================
def encode_image(image_path, secret_text, output_path):
    print(CYAN + "\n[!] Kép beoltása és pixel-manipuláció indítása...")
    img = Image.open(image_path)
    binary_secret = text_to_bin(secret_text)
    
    # QA ELLENŐRZÉS: Elég pixel van-e a képben a szöveghez?
    if len(binary_secret) > img.width * img.height * 3:
        return RED + "HIBA: Túl hosszú szöveg, nem fér el a kép pixeleiben!" + RESET

    encoded_img = img.copy()
    pixels = encoded_img.load()
    
    bit_idx = 0
    for y in range(img.height):
        for x in range(img.width):
            if bit_idx >= len(binary_secret):
                break
                
            r, g, b = pixels[x, y][:3]
            
            # Módosítjuk a piros, zöld és kék csatornák legalsó bitjét
            if bit_idx < len(binary_secret):
                r = (r & ~1) | int(binary_secret[bit_idx])
                bit_idx += 1
            if bit_idx < len(binary_secret):
                g = (g & ~1) | int(binary_secret[bit_idx])
                bit_idx += 1
            if bit_idx < len(binary_secret):
                b = (b & ~1) | int(binary_secret[bit_idx])
                bit_idx += 1
                
            pixels[x, y] = (r, g, b)
            
    encoded_img.save(output_path)
    return GREEN + f"[✔] SIKER! A titkos kód elrejtve a következő fájlban: {output_path}" + RESET

# ==============================================================================
# FUNKCIÓ: decode_image()
# LEÍRÁS: Kibányássza a pixelek legalsó bitjeiből a bináris adatot, majd szöveggé alakítja.
# ==============================================================================
def decode_image(image_path):
    print(CYAN + "\n[!] Képpontok heurisztikus elemzése és bit-bányászat...")
    img = Image.open(image_path)
    pixels = img.load()
    
    binary_data = ""
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y][:3]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)
            
            # Gyorsított QA ellenőrzés a lezáró jelre (ne olvassa feleslegesen az egész nagy képet)
            if "1111111111111110" in binary_data:
                stop_pos = binary_data.find("1111111111111110")
                return bin_to_text(binary_data[:stop_pos])
                
    return bin_to_text(binary_data)

# ==============================================================================
# FIGYELEM: Használat előtt tegyél be egy 'focista.png' képet a Python fájl mellé!
# ==============================================================================
if __name__ == "__main__":
    # Példa futtatás (Csak cseréld le a fájlneveket a sajátodra!)
    try:
        # 1. KÓDOLÁS TESZT
        # print(encode_image("focista.png", "A VAS NEM FELEJT - BORSOD DISTRICT 352", "titkos_focista.png"))
        
        # 2. DEKÓDOLÁS TESZT
        # uzenet = decode_image("titkos_focista.png")
        # print(GREEN + f"🔓 Megfejtett üzenet a pixelekből: {uzenet}" + RESET)
        pass
    except Exception as e:
        print(RED + f"Hiba történt: {e} (Tegyél be egy igazi .png képet a mappa gyökerébe!)" + RESET)
