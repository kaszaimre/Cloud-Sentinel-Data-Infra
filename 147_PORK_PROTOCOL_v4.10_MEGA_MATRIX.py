#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
PROJEKT: 147_PORK_PROTOCOL_v4.10_MEGA_MATRIX
LEÍRÁS (HU):
10-in-1 stratégiai vezérlőpult a Rákoscsaba Bázis számára. Integrált
volatilitási logikával és dinamikus szignál-generátorral.
Minden modul (Scalp, Whaler, Divergence) egyetlen felületen.

DESCRIPTION (EN):
10-in-1 strategic dashboard for the Rákoscsaba Base. Integrated with
volatility logic and dynamic signal generation. 
All modules (Scalp, Whaler, Divergence) available on a single interface.

SZERZŐ: Tábornok | BORSODI WAR ROOM
================================================================================
"""

# ==============================================================================
# 🌌 CYBER-BORSOD NODE 47-A: PORK PROTOCOL v4.10 - 10-IN-1 MEGA MATRIX PANEL
# 🚀 PROTOCOL: UNIVERSAL TOUCH INTERFACE WITH 10 STRATEGIC VARIATIONS
# 🛠️ DEVELOPER: T800 Data-Butcher & The Commander (49er MMA/Judo Master)
# 🎯 ARSENAL FILE: 147_pork_protocol_mega_panel.py
# ==============================================================================

import tkinter as tk
from tkinter import ttk

# --- A 10 KÜLÖNBÖZŐ HARCI VERZIÓ MATEMATIKAI LOGIKÁJA ---
def run_version_logic(v_name, btc, c10, c60, adx, pdi, mdi):
    # Alap volatilitási faktor
    vf = max(0.015, min(0.035, adx / 1500))
    sl_offset = btc * vf
    
    # Alap szinkron feltételek
    is_bull = (c10 > 0) and (c60 > 0) and (pdi > mdi)
    is_bear = (c10 < 0) and (c60 < 0) and (mdi > pdi)
    
    # 1. VERZIÓ: Standard v3.7 Direkciós Panel
    if v_name == "1. STANDARD DIREKCIÓS PANEL (v3.7)":
        if is_bull and adx > 25: return "🟢 BUY", -sl_offset, sl_offset * 1.35
        if is_bear and adx > 25: return "🔴 SELL", sl_offset, -sl_offset * 1.35
        return "🟡 HOLD (Divergencia)", 0, 0

    # 2. VERZIÓ: Ultra-Scalp Mód (Szűk SL, Gyors TP kis ADX-nél is)
    elif v_name == "2. ULTRA-SCALP PROTOCOL":
        short_sl = btc * 0.005 # Fix 0.5% szűk stop
        if c10 > 0 and pdi > mdi: return "🟢 SCALP BUY", -short_sl, short_sl * 2.0
        if c10 < 0 and mdi > pdi: return "🔴 SCALP SELL", short_sl, -short_sl * 2.0
        return "🟡 HOLD", 0, 0

    # 3. VERZIÓ: Bálna-Vadász Mód (Csak extrém magas ADX > 40-nél lép be)
    elif v_name == "3. WHALE HUNTER PRO":
        if adx > 40 and is_bull: return "🟢 WHALE BUY", -sl_offset * 1.5, sl_offset * 3.0
        if adx > 40 and is_bear: return "🔴 WHALE SELL", sl_offset * 1.5, -sl_offset * 3.0
        return "🟡 HOLD (Gyenge trend a bálnáknak)", 0, 0

    # 4. VERZIÓ: Sakkmatt Zóna Szűrő (Spinning Top és oldalazás kimenet)
    elif v_name == "4. CHECKMATE ZONE FILTER":
        if adx < 20 or (abs(c10) < 50 and abs(c60) < 50):
            return "⚠️ SAKKMATT (Pangó piac, oldalazás)", 0, 0
        return "🟢 AKTÍV PIAC (Nincs szűkület)", 0, 0

    # 5. VERZIÓ: Divergencia Mester (Ellentétes CCI10/60 horgony)
    elif v_name == "5. DIVERGENCE MASTER":
        if c10 > 100 and c60 < -50: return "🔥 REBOUND BUY (Fordulat alulról)", -sl_offset, sl_offset * 2.5
        if c10 < -100 and c60 > 50: return "💥 REBOUND SELL (Fordulat felülről)", sl_offset, -sl_offset * 2.5
        return "🟡 HOLD (Nincs tiszta divergencia)", 0, 0

    # 6. VERZIÓ: Trend-Erő Fuzzer (Tisztán ADX alapú kockázatkezelés)
    elif v_name == "6. TREND-STRENGTH FUZZER":
        dynamic_rrr = 1.0 + (adx / 100)
        if is_bull: return "🟢 FUZZER BUY", -sl_offset, sl_offset * dynamic_rrr
        if is_bear: return "🔴 FUZZER SELL", sl_offset, -sl_offset * dynamic_rrr
        return "🟡 HOLD", 0, 0

    # 7. VERZIÓ: DI Kereszteződési Csapda (Csak a DI0+ / DI- törésre figyel)
    elif v_name == "7. DI CROSSOVER TRAP":
        if pdi > mdi + 15: return "🟢 DI CROSS BUY", -sl_offset, sl_offset * 1.5
        if mdi > pdi + 15: return "🔴 DI CROSS SELL", sl_offset, -sl_offset * 1.5
        return "🟡 HOLD (Nincs DI szakadás)", 0, 0

    # 8. VERZIÓ: Kamatos-Kamat Szorzó (Biztonsági tőkemegóvás)
    elif v_name == "8. COMPOUND PROTECTOR":
        safe_sl = btc * 0.02 # Fix 2% biztonsági fék
        if is_bull and adx > 30: return "🟢 SAFE BUY", -safe_sl, safe_sl * 1.5
        if is_bear and adx > 30: return "🔴 SAFE SELL", safe_sl, -safe_sl * 1.5
        return "🟡 HOLD", 0, 0

    # 9. VERZIÓ: Nitro Pálesz Momentum (Gyorsulási ráta ha CCI10 > 200)
    elif v_name == "9. NITRO MOMENTUM ENGINE":
        if c10 > 200: return "🚀 NITRO BUY (Extrém lendület!)", -sl_offset * 0.8, sl_offset * 2.0
        if c10 < -200: return "📉 NITRO SELL (Extrém pánik!)", sl_offset * 0.8, -sl_offset * 2.0
        return "🟡 HOLD (Normál sáv)", 0, 0

    # 10. VERZIÓ: Borsodi Finanszírozó Horgony (Hosszú távú tartás)
    elif v_name == "10. BORSOD INVEST ANCHOR":
        long_sl = btc * 0.05 # 5% stratégiai stop
        if c60 > 0 and pdi > mdi: return "👑 INVEST BUY (Hosszú táv)", -long_sl, long_sl * 4.0
        if c60 < 0 and mdi > pdi: return "👑 INVEST SELL (Hosszú táv)", long_sl, -long_sl * 4.0
        return "🟡 HOLD", 0, 0

    return "🟡 HOLD", 0, 0

# --- GRAFIKUS MOTOR INDÍTÁSA ---
def update_calculation():
    try:
        btc = float(entry_btc.get())
        c10 = float(entry_cci10.get())
        c60 = float(entry_cci60.get())
        adx = float(entry_adx.get())
        pdi = float(entry_pdi.get())
        mdi = float(entry_mdi.get())
        selected_version = combo_version.get()
    except ValueError:
        lbl_signal.config(text="[-] HIBA: Ervenytelen szamformatum!", foreground="#FF3333")
        return

    sig, sl, tp = run_version_logic(selected_version, btc, c10, c60, adx, pdi, mdi)
    
    # Színbeállítás a szignál alapján
    sig_color = "#33FF33" if "BUY" in sig else "#FF3333" if "SELL" in sig else "#FFFF33"
    if "SAKKMATT" in sig: sig_color = "#FF9900"
        
    lbl_signal.config(text=f"[+] {sig}", foreground=sig_color)
    lbl_sl.config(text=f"SL: {round(sl, 2)} USD (Cel: {round(btc + sl, 2) if sl != 0 else 0})")
    lbl_tp.config(text=f"TP: {round(tp, 2)} USD (Cel: {round(btc + tp, 2) if tp != 0 else 0})")

def reset_all():
    entry_btc.delete(0, tk.END)
    entry_cci10.delete(0, tk.END)
    entry_cci60.delete(0, tk.END)
    entry_adx.delete(0, tk.END)
    entry_pdi.delete(0, tk.END)
    entry_mdi.delete(0, tk.END)
    
    entry_btc.insert(0, "76990.0")
    entry_cci10.insert(0, "-100")
    entry_cci60.insert(0, "23")
    entry_adx.insert(0, "28")
    entry_pdi.insert(0, "12")
    entry_mdi.insert(0, "20")
    
    lbl_signal.config(text="[*] JELZES: Reset kesz. Varunk a szamitasra...", foreground="#A0AAB5")
    lbl_sl.config(text="Javasolt Stop Loss   (SL): 0.00 USD")
    lbl_tp.config(text="Javasolt Take Profit (TP): 0.00 USD")
    entry_btc.focus_set()

# GUI Felépítése
root = tk.Tk()
root.title("🦾 CYBER-BORSOD v4.10 MEGA MATRIX")
root.geometry("550x630")
root.configure(bg="#0D0F12")

# Verzióválasztó Felső Sáv
lbl_ver = tk.Label(root, text="🔥 STRATÉGIAI MODUL KIVÁLASZTÁSA:", bg="#0D0F12", fg="#FFFF33", font=("Courier New", 10, "bold"))
lbl_ver.pack(pady=(10,0))

versions_list = [
    "1. STANDARD DIREKCIÓS PANEL (v3.7)",
    "2. ULTRA-SCALP PROTOCOL",
    "3. WHALE HUNTER PRO",
    "4. CHECKMATE ZONE FILTER",
    "5. DIVERGENCE MASTER",
    "6. TREND-STRENGTH FUZZER",
    "7. DI CROSSOVER TRAP",
    "8. COMPOUND PROTECTOR",
    "9. NITRO MOMENTUM ENGINE",
    "10. BORSOD INVEST ANCHOR"
]

combo_version = ttk.Combobox(root, values=versions_list, state="readonly", width=40, font=("Courier New", 10, "bold"))
combo_version.set(versions_list[0]) # Alapértelmezett a v3.7
combo_version.pack(pady=5)
combo_version.bind("<<ComboboxSelected>>", lambda e: update_calculation())

frame_input = tk.Frame(root, bg="#0D0F12")
frame_input.pack(pady=5, padx=10, fill="x")
frame_input.columnconfigure(1, weight=1)

def create_row(text, val, row):
    tk.Label(frame_input, text=text, bg="#0D0F12", fg="#A0AAB5", font=("Courier New", 10, "bold")).grid(row=row, column=0, padx=5, pady=4, sticky="w")
    e = tk.Entry(frame_input, bg="#161A22", fg="#33FF33", font=("Courier New", 11, "bold"), insertbackground="#33FF33")
    e.insert(0, val)
    e.grid(row=row, column=1, padx=5, pady=4, sticky="ew")
    e.bind("<FocusIn>", lambda event: e.selection_range(0, tk.END))
    return e

entry_btc   = create_row("-> AR (Manualis):", "76990.0", 0)
entry_cci10 = create_row("-> CCI(10):", "-100", 1)
entry_cci60 = create_row("-> CCI(60):", "23", 2)
entry_adx   = create_row("-> ADX(14):", "28", 3)
entry_pdi   = create_row("-> +DI (Bika):", "12", 4)
entry_mdi   = create_row("-> -DI (Medve):", "20", 5)

frame_buttons = tk.Frame(root, bg="#0D0F12")
frame_buttons.pack(pady=10, fill="x", padx=20)
frame_buttons.columnconfigure(0, weight=1)
frame_buttons.columnconfigure(1, weight=1)

btn_calc = tk.Button(frame_buttons, text="CALCULATE", command=update_calculation, bg="#161A22", fg="#33FF33", font=("Courier New", 10, "bold"), relief="flat", bd=2, highlightbackground="#33FF33", highlightthickness=1)
btn_calc.grid(row=0, column=0, padx=5, ipady=6, sticky="ew")

btn_reset = tk.Button(frame_buttons, text="RELOAD / RESET", command=reset_all, bg="#161A22", fg="#FFFF33", font=("Courier New", 10, "bold"), relief="flat", bd=2, highlightbackground="#FFFF33", highlightthickness=1)
btn_reset.grid(row=0, column=1, padx=5, ipady=6, sticky="ew")

frame_output = tk.LabelFrame(root, text=" [ KIERTEKELES MATRIX ] ", bg="#0D0F12", fg="#A0AAB5", font=("Courier New", 10, "bold"), padx=10, pady=10, bd=1)
frame_output.pack(fill="both", expand=True, padx=20, pady=5)

lbl_signal = tk.Label(frame_output, text="[*] JELZES: Varunk az adatokra...", bg="#0D0F12", fg="#FFFF33", font=("Courier New", 11, "bold"))
lbl_signal.pack(anchor="w", pady=2)

lbl_sl = tk.Label(frame_output, text="Javasolt Stop Loss   (SL): 0.00 USD", bg="#0D0F12", fg="#A0AAB5", font=("Courier New", 10))
lbl_sl.pack(anchor="w", pady=2)

lbl_tp = tk.Label(frame_output, text="Javasolt Take Profit (TP): 0.00 USD", bg="#0D0F12", fg="#A0AAB5", font=("Courier New", 10))
lbl_tp.pack(anchor="w", pady=2)

lbl_footer = tk.Label(root, text="[Program finished | Mega Matrix Active]", bg="#0D0F12", fg="#505A65", font=("Courier New", 9))
lbl_footer.pack(side="bottom", pady=5)

entry_btc.focus_set()
root.mainloop()
