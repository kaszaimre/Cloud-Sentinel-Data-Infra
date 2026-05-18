import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

# Adatok betöltése (ugyanaz a CSV, amit eddig használtál)
try:
    df = pd.read_csv('Borsodi_Majomfa_Teremtes_V2.csv')
    elitek = df[df['Kikelesi_Sebesseg_Nap'] <= 15]
except:
    # Ha nincs meg a fájl, kreálunk egy alap brigádot, hogy ne omoljon össze
    elitek = pd.DataFrame({'Azonosito': ['Alap Majom'], 'Profit_Szint': ['Kezdő']})

def jatek(jatekos_tipp):
    gep_tipp = random.choice(["kő", "papír", "olló"])
    kivalasztott = elitek.sample(1).iloc[0]
    egyseg_nev = kivalasztott['Azonosito']
    
    eredmeny = ""
    if jatekos_tipp == gep_tipp:
        eredmeny = f"DÖNTETLEN!\n{egyseg_nev} és a gép is {gep_tipp}-t dobott."
    elif (jatekos_tipp == "kő" and gep_tipp == "olló") or \
         (jatekos_tipp == "papír" and gep_tipp == "kő") or \
         (jatekos_tipp == "olló" and gep_tipp == "papír"):
        eredmeny = f"GYŐZELEM! 🎉\n{egyseg_nev} ({jatekos_tipp}) lezúzta a gépet ({gep_tipp})!\nOSS!"
    else:
        eredmeny = f"VESZTESÉG... 😢\nA gép ({gep_tipp}) megverte {egyseg_nev}-t ({jatekos_tipp})."

    # Felugró ablak az eredménnyel
    messagebox.showinfo("Csata Eredmény", eredmeny)

# Ablak létrehozása
root = tk.Tk()
root.title("Borsodi Brigád App")
root.geometry("400x300")
root.configure(bg="#2c3e50")

# Feliratok
tk.Label(root, text="BORSODI BRIGÁD TERMINÁL", fg="white", bg="#2c3e50", font=("Arial", 16, "bold")).pack(pady=20)
tk.Label(root, text="Válassz fegyvert!", fg="#ecf0f1", bg="#2c3e50").pack()

# Gombok
frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=20)

tk.Button(frame, text="KŐ", width=10, height=2, command=lambda: jatek("kő")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="PAPÍR", width=10, height=2, command=lambda: jatek("papír")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="OLLÓ", width=10, height=2, command=lambda: jatek("olló")).grid(row=0, column=2, padx=5)

tk.Label(root, text="FASA ÉS KÉSZ!", fg="gray", bg="#2c3e50").pack(side="bottom", pady=10)

root.mainloop()