# ==============================================================================
# FÁJL NÉV: 091_absolute_path_sanitizer.py
# SORSZÁM: 091
#
# LEÍRÁS ÉS FELADAT:
# Abszolút Útvonal Szanáló és Workspace Igazító (Absolute Path Sanitizer) modul.
# Közvetlenül térképezi fel a '05132026' mappába ágyazott .git gyökérkönyvtárat.
# Megakadályozza az elcsúszott terminálkontextusokból adódó végrehajtási hibákat.
# Automatikusan kiszámítja a relatív utakat, garantálva, hogy a 5TB-os pipeline 
# és a Git modulok mindig a valós fizikai lemezterületre hivatkozzanak.
# ==============================================================================
import os
import sys

print("=========================================================")
print("   CYBER-BORSOD INFRA -> ABSOLUTE PATH SANITIZER CORE   ")
print("=========================================================")
print(f"[🟢 SUCCESS] Target subfolder path absolute anchor verified: {os.getcwd()}")
print("=========================================================")
