import tkinter as tk
from tkinter import messagebox
import time
import random

def indit_szimulacio():
    # Gomb kikapcsolása, amíg fut a motor
    gomb.config(state=tk.DISABLED)
    szoveg_doboz.delete(1.0, tk.END)
    szoveg_doboz.insert(tk.END, "🐕 SHIB PÖRKÖLT MOTOR INDÍTÁSA...\n")
    szoveg_doboz.insert(tk.END, "-"*45 + "\n")
    root.update() # Ablak frissítése azonnal
    time.sleep(1) # Kis késleltetés a drámai hatásért

    arfolyam = 0.000010
    egetett_osszesen = 0

    # Ez a ciklus az, ami "lefut", kipörgeti a napokat
    for nap in range(1, 6):
        egetes = random.randint(1, 10) # 1-10 millió SHIB
        egetett_osszesen += egetes
        arfolyam += random.uniform(0.000001, 0.000005)
        
        sor = f"Nap {nap}: 🔥 {egetes} Millió SHIB elégetve! | Ár: {arfolyam:.6f} $\n"
        szoveg_doboz.insert(tk.END, sor)
        szoveg_doboz.see(tk.END) # Automatikus görgetés lefelé
        root.update() # Láthatóvá teszi az új sort azonnal
        time.sleep(1) # 1 másodperc szünet, így látszik az "animáció"

    szoveg_doboz.insert(tk.END, "-"*45 + "\n")
    szoveg_doboz.insert(tk.END, f"ÖSSZESEN ELÉGETVE: {egetett_osszesen} Millió SHIB\n")
    szoveg_doboz.insert(tk.END, "CÉL: A HOLD! 🚀 JOL VAGZUNK!\n")
    root.update()
    
    # Felugró ablak a végén
    messagebox.showinfo("Szimuláció Vége", f"A pörkölés befejeződött!\nZáró árfolyam: {arfolyam:.6f} $")
    gomb.config(state=tk.NORMAL) # Gomb visszakapcsolása

# --- ABLAK (GUI) LÉTREHOZÁSA ---
root = tk.Tk()
root.title("Borsodi Brigád - SHIB Motor")
root.geometry("500x350")
root.configure(bg="#2c3e50")

# Cím
cim = tk.Label(root, text="🔥 SHIB PÖRKÖLT MOTOR 🔥", fg="white", bg="#2c3e50", font=("Arial", 16, "bold"))
cim.pack(pady=10)

# Indító Gomb
gomb = tk.Button(root, text="MOTOR INDÍTÁSA", bg="#e74c3c", fg="white", font=("Arial", 12, "bold"), command=indit_szimulacio)
gomb.pack(pady=10)

# Fekete "Hacker" Szövegdoboz, ahova kiírja az adatokat
szoveg_doboz = tk.Text(root, height=10, width=55, bg="black", fg="#00ff00", font=("Courier", 10))
szoveg_doboz.pack(pady=10)

root.mainloop()