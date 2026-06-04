#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
PROJEKT: 148_PORK_PROTOCOL_v3.80_UNIVERSAL
LEÍRÁS (HU):
100%-ban manuális grafikus (Tkinter) panel. Bármilyen árfolyamot 
és indikátort beírhatsz, a volatilitás-alapú SL/TP modul azonnal számol.
Stabil, hordozható, offline-képes operátori eszköz.

DESCRIPTION (EN):
100% manual graphical (Tkinter) panel. Inputs are completely free-text, 
triggering the volatility-based SL/TP calculation instantly. 
Stable, portable, offline-capable operator tool.

SZERZŐ: Tábornok | BORSODI WAR ROOM
================================================================================
"""

# ==============================================================================
# 🌌 CYBER-BORSOD NODE 47-A: PORK PROTOCOL v3.80 - UNIVERSAL MATH INTERFACE
# 🚀 PROTOCOL: 100% MANUAL INPUT SYSTEM FOR ANY PRICE & ANY CALCULATION
# 🛠️ DEVELOPER: T800 Data-Butcher & The Commander (49er MMA/Judo Master)
# 🎯 ARSENAL FILE: 148_pork_protocol_v3_80_universal.py
# ==============================================================================
# [HU] LEÍRÁS: 100%-ban manuális grafikus (Tkinter) panel. Bármilyen árfolyamot
#      és indikátort beírhatsz, a volatilitás-alapú SL/TP modul azonnal számol.
# ------------------------------------------------------------------------------
# [EN] DESCRIPTION: 100% manual graphical (Tkinter) panel. Inputs are completely
#      free-text, triggering the volatility-based SL/TP calculation instantly.
# ==============================================================================

import tkinter as tk
from tkinter import ttk

def calculate_signal():
    try:
        # Minden adat 100%-ban manuálisan írható és beolvasható
        btc_price = float(entry_btc.get())
        cci_10 = float(entry_cci10.get())
        cci_60 = float(entry_cci60.get())
        adx_14 = float(entry_adx.get())
        plus_di = float(entry_pdi.get())
        minus_di = float(entry_mdi.get())
    except ValueError:
        lbl_signal.config(text="[-] HIBA: Ervenytelen szamformatum!", foreground="#FF3333")
        lbl_sl.config(text="SL: 0.00 USD")
        lbl_tp.config(text="TP: 0.00 USD")
        return

    # ADX alapú dinamikus volatilitási puffer (bármilyen bázisárhoz igazodik)
    volatility_factor = max(0.015, min(0.035, adx_14 / 1500))
    sl_offset = btc_price * volatility_factor
    
    # Szigorított feltételrendszer: CCI és +DI/-DI együttes szinkronizációja
    is_bullish = (cci_10 > 0) and (cci_60 > 0) and (plus_di > minus_di)
    is_bearish = (cci_10 < 0) and (cci_60 < 0) and (minus_di > plus_di)
    
    if is_bullish and adx_14 > 25:
        lbl_signal.config(text="[+] JELZES: BUY (Minden irany es a DI is felfele all!)", foreground="#33FF33")
        lbl_sl.config(text=f"Javasolt Stop Loss   (SL): -{round(sl_offset, 2)} USD  (Ar: {round(btc_price - sl_offset, 2)})")
        lbl_tp.config(text=f"Javasolt Take Profit (TP): +{round(sl_offset * 1.35, 2)} USD  (Ar: {round(btc_price + (sl_offset * 1.35), 2)})")
    elif is_bearish and adx_14 > 25:
        lbl_signal.config(text="[-] JELZES: SELL (Medve dominancia + DI- megerosites!)", foreground="#FF3333")
        lbl_sl.config(text=f"Javasolt Stop Loss   (SL): +{round(sl_offset, 2)} USD  (Ar: {round(btc_price + sl_offset, 2)})")
        lbl_tp.config(text=f"Javasolt Take Profit (TP): -{round(sl_offset * 1.35, 2)} USD  (Ar: {round(btc_price - (sl_offset * 1.35), 2)})")
    else:
        lbl_signal.config(text="[*] JELZES: HOLD (Divergencia vagy bizonytalan Sakkmatt Zona!)", foreground="#FFFF33")
        lbl_sl.config(text="Javasolt Stop Loss   (SL): 0.00 USD")
        lbl_tp.config(text="Javasolt Take Profit (TP): 0.00 USD")

def reset_fields():
    """Taktikai reload: üríti a mátrixot egy teljesen tiszta, új számításhoz"""
    entry_btc.delete(0, tk.END)
    entry_cci10.delete(0, tk.END)
    entry_cci60.delete(0, tk.END)
    entry_adx.delete(0, tk.END)
    entry_pdi.delete(0, tk.END)
    entry_mdi.delete(0, tk.END)
    
    entry_btc.insert(0, "0.0")
    entry_cci10.insert(0, "0")
    entry_cci60.insert(0, "0")
    entry_adx.insert(0, "0")
    entry_pdi.insert(0, "0")
    entry_mdi.insert(0, "0")
    
    lbl_signal.config(text="[*] JELZES: Varunk a teljesen uj adatokra...", foreground="#A0AAB5")
    lbl_sl.config(text="Javasolt Stop Loss   (SL): 0.00 USD")
    lbl_tp.config(text="Javasolt Take Profit (TP): 0.00 USD")

# GUI Felépítése
root = tk.Tk()
root.title("🦾 CYBER-BORSOD NODE 47-A: PORK PROTOCOL v3.80")
root.geometry("550x580")
root.configure(bg="#0D0F12")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#0D0F12", foreground="#A0AAB5", font=("Courier New", 11, "bold"))
style.configure("TEntry", fieldbackground="#161A22", foreground="#33FF33", font=("Courier New", 11))

lbl_title = tk.Label(root, text="PORK PROTOCOL v3.80 - UNIVERZÁLIS PANEL", bg="#0D0F12", fg="#33FF33", font=("Courier New", 13, "bold"))
lbl_title.pack(pady=15)

frame_input = tk.Frame(root, bg="#0D0F12")
frame_input.pack(pady=10)

def create_input_row(label_text, default_val, row_num):
    ttk.Label(frame_input, text=label_text).grid(row=row_num, column=0, padx=10, pady=6, sticky="w")
    entry = ttk.Entry(frame_input, width=15)
    entry.insert(0, default_val)
    entry.grid(row=row_num, column=1, padx=10, pady=6)
    return entry

# 100%-ban manuális beviteli mezők
entry_btc   = create_input_row("-> AKTUALIS ARFOLYAM (Manualis):", "76990.0", 0)
entry_cci10 = create_input_row("-> CCI(10) erteke:", "-100", 1)
entry_cci60 = create_input_row("-> CCI(60) erteke:", "23", 2)
entry_adx   = create_input_row("-> ADX(14) nyers ero:", "28", 3)
entry_pdi   = create_input_row("-> +DI (Bika ero):", "12", 4)
entry_mdi   = create_input_row("-> -DI (Medve ero):", "20", 5)

frame_buttons = tk.Frame(root, bg="#0D0F12")
frame_buttons.pack(pady=15)

btn_calc = tk.Button(frame_buttons, text="HADMŰVELET INDÍTÁSA", command=calculate_signal, bg="#161A22", fg="#33FF33", activebackground="#33FF33", activeforeground="#0D0F12", font=("Courier New", 10, "bold"), relief="flat", bd=2, highlightbackground="#33FF33", highlightthickness=1)
btn_calc.pack(side="left", padx=10, ipadx=5, ipady=4)

btn_reset = tk.Button(frame_buttons, text="RELOAD / ÚJRAINDÍTÁS", command=reset_fields, bg="#161A22", fg="#FFFF33", activebackground="#FFFF33", activeforeground="#0D0F12", font=("Courier New", 10, "bold"), relief="flat", bd=2, highlightbackground="#FFFF33", highlightthickness=1)
btn_reset.pack(side="left", padx=10, ipadx=5, ipady=4)

frame_output = tk.LabelFrame(root, text=" [ KIERTEKELES MATRIX ] ", bg="#0D0F12", fg="#A0AAB5", font=("Courier New", 10, "bold"), padx=15, pady=15, bd=1)
frame_output.pack(fill="x", padx=30, pady=10)

lbl_signal = ttk.Label(frame_output, text="[*] JELZES: Varunk az adatokra...", font=("Courier New", 11, "bold"))
lbl_signal.pack(anchor="w", pady=4)

lbl_sl = ttk.Label(frame_output, text="Javasolt Stop Loss   (SL): 0.00 USD", font=("Courier New", 10))
lbl_sl.pack(anchor="w", pady=4)

lbl_tp = ttk.Label(frame_output, text="Javasolt Take Profit (TP): 0.00 USD", font=("Courier New", 10))
lbl_tp.pack(anchor="w", pady=4)

lbl_footer = tk.Label(root, text="[Program finished | Node 47-A Active]", bg="#0D0F12", fg="#505A65", font=("Courier New", 9))
lbl_footer.pack(side="bottom", pady=10)

root.mainloop()
