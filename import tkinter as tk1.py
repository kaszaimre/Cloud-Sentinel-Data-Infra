import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

# 1. Betöltés és előkészítés
try:
    df = pd.read_csv('Borsodi_Majomfa_Teremtes_V2.csv')
    # Ha még nincs 'Gyozelem' oszlop, létrehozzuk 0 értékkel
    if 'Gyozelem' not in df.columns:
        df['Gyozelem'] = 0
except:
    messagebox.showerror("Hiba", "A CSV fájl nem található!")

def mentés_és_játék(jatekos_tipp):
    global df # Hogy a függvényen kívüli táblázatot is tudjuk módosítani
    
    gep_tipp = random.choice(["kő", "papír", "olló"])
    
    # Csak az elitekből választunk
    elite_indexek = df[df['Kikelesi_Sebesseg_Nap'] <= 15].index
    valasztott_index = random.choice(elite_indexek)
    kivalasztott = df.loc[valasztott_index]
    
    eredmeny_szoveg = ""
    
    if jatekos_tipp == gep_tipp:
        eredmeny_szoveg = f"DÖNTETLEN!\nMindketten {gep_tipp}-t dobtatok."
    elif (jatekos_tipp == "kő" and gep_tipp == "olló") or \
         (jatekos_tipp == "papír" and gep_tipp == "kő") or \
         (jatekos_tipp == "olló" and gep_tipp == "papír"):
        
        # --- ADATMENTÉS LOGIKA ---
        df.at[valasztott_index, 'Gyozelem'] += 1 # Adunk egy pontot az egységnek
        df.to_csv('Borsodi_Majomfa_Teremtes_V2.csv', index=False) # Elmentjük a fájlt
        # -------------------------
        
        uj_pont = df.at[valasztott_index, 'Gyozelem']
        eredmeny_szoveg = f"GYŐZELEM! 🎉\n{kivalasztott['Azonosito']} lezúzta a gépet!\nÖsszes győzelme: {uj_pont}\nOSS!"
    else:
        eredmeny_szoveg = f"VESZTESÉG... 😢\nA gép ({gep_tipp}) nyert."

    messagebox.showinfo("Borsodi Csata", eredmeny_szoveg)

# --- INNENTŐL A GUI RÉSZ UGYANAZ ---
root = tk.Tk()
root.title("Borsodi Brigád - Adatmentő Kiadás")
root.geometry("400x300")

tk.Label(root, text="BORSODI BRIGÁD ADATBÁZIS", font=("Arial", 14, "bold")).pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Button(frame, text="KŐ", width=10, command=lambda: mentés_és_játék("kő")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="PAPÍR", width=10, command=lambda: mentés_és_játék("papír")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="OLLÓ", width=10, command=lambda: mentés_és_játék("olló")).grid(row=0, column=2, padx=5)

root.mainloop()