import matplotlib.pyplot as plt

# BORSODI BRIGÁD - 6. DIMENZIÓS DIAGRAM GENERÁTOR
# Adatok a 170-es és 185-ös gátakról!
napok = ['1. Nap', '2. Nap', '3. Nap', '4. Nap', '5. Nap']
eth_arak = [3500, 3550, 3620, 3700, 3850]
xrp_arak = [0.50, 0.52, 0.55, 0.61, 0.75]
shib_egetes = [5, 8, 12, 25, 40] # Elégetett milliók

# 1. Grafikon stílusának beállítása (Sötét, igazi War Room stílus)
plt.style.use('dark_background')
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))
fig.suptitle('🌍 BORSODI BRIGÁD - PIACI HELYZETKÉP 🌍', fontsize=16, fontweight='bold', color='#00ff00')

# 2. ETH Vonal (A Mag Hízása - Zöld vonal)
ax1.plot(napok, eth_arak, color='#00ff00', marker='o', linewidth=2, markersize=8)
ax1.set_title('💎 ETH (A Mag Hízása)', color='white')
ax1.set_ylabel('Árfolyam (USD)')
ax1.grid(True, linestyle='--', alpha=0.3)

# 3. XRP Vonal (Kitörés a Gátról - Kék vonal)
ax2.plot(napok, xrp_arak, color='#00ffff', marker='s', linewidth=2, markersize=8)
ax2.set_title('🌊 XRP (Kitörés a Gátról)', color='white')
ax2.set_ylabel('Árfolyam (USD)')
ax2.grid(True, linestyle='--', alpha=0.3)

# 4. SHIB Oszlopdiagram (A Pörkölés - Piros oszlopok)
ax3.bar(napok, shib_egetes, color='#ff3333', alpha=0.8)
ax3.set_title('🔥 SHIB (Elégetett Milliók)', color='white')
ax3.set_ylabel('Elégetett Mennyiség')
ax3.grid(True, linestyle='--', alpha=0.3)

# 5. Elrendezés igazítása és MENTÉS KÉPKÉNT
plt.tight_layout()
kep_neve = 'Borsodi_Brigad_Diagram.png'
plt.savefig(kep_neve, dpi=300) # Itt menti el a képet a mappádba!
print(f"JELENTÉS: Diagram elmentve '{kep_neve}' néven! FASA ÉS KÉSZ!")

# 6. Megjelenítés a képernyőn is
plt.show()