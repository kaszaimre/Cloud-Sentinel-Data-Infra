#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
# PROJEKT: 143_CYBER_BORSOD_MATRIX_LOOP
# 
# LEÍRÁS (HU):
# Vizuális mátrix-hurok animáció az operátori terminál álcázására. 
# A kód ASCII-optimalizált, így minden mobil terminálban stabilan fut.
#
# DESCRIPTION (EN):
# Visual matrix-loop animation for operator terminal obfuscation.
# ASCII-optimized for stable execution in all mobile terminals.
#
# SZERZŐ: Tábornok | BORSODI WAR ROOM
================================================================================
"""

import time
import sys
import random

def matrix_loop_animation():
    print("\n" + "=" * 65)
    print("[FIGYELMEZTETÉS] Rekurzív beloopoltatás elindítva!")
    print("[INFO] Megszakításhoz nyomjon CTRL + C gombot.")
    print("=" * 65)
    time.sleep(2)

    # ASCII-optimalizált karakterkészlet
    chars = ["#", "@", "1", "0", " ", "BORSOD", "KOD", "SIGMA"]
    
    try:
        while True:
            line = "".join(random.choice(chars) for _ in range(30))
            sys.stdout.write(f"\033[32m {line} \033[0m\n")
            sys.stdout.flush()
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n\n" + "=" * 65)
        print("[OK] Hurok sikeresen megszakítva. Biztonsági mag lezárva.")
        print("=" * 65)

if __name__ == "__main__":
    matrix_loop_animation()
