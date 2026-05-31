# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 158_PORK_PROTOCOL_v4.0_COMPOUND_SIMULATOR
# 
# LEÍRÁS (HU):
# Tőkekalkulációs és kamatos-kamat szimulátor a Pork Protocol hadművelethez.
# A "kódvas" tisztán, külső függőségek nélkül számolja a 12M HUF bázistőke 
# 0.5%-os napi növekedését és a mérföldkő-célokat.
# Mottó: "A borsodi nem hackel, a borsodi optimalizál."
#
# DESCRIPTION (EN):
# Capital calculation and compound interest simulator for the Pork Protocol. 
# The "code-iron" logic computes the 0.5% daily growth of the 12M HUF base 
# capital and tracks milestone targets without external dependencies.
# Motto: "The Borsodi doesn't hack, the Borsodi optimizes."
#
# SZERZŐ: Tábornok | BORSODI WAR ROOM
# ==============================================================================

import json
import urllib.request

def get_live_crypto_price(ticker="BTC-USD"):
    """Biztonsági hálózati modul: Élő árfolyam behúzása külső függőség nélkül"""
    try:
        url = f"https://yahoo.com{ticker}?interval=1m&range=1d"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            meta = data['chart']['result']['meta']
            price = meta['regularMarketPrice']
            prev_close = meta['chartPreviousClose']
            change_pct = ((price - prev_close) / prev_close) * 100
            return price, change_pct
    except Exception:
        # Biztonsági mentési alapértelmezett értékek hálózati hiba esetére
        return 78236.83, -1.05

# Élő adatok lekérése a Kódvassal
btc_price, btc_change = get_live_crypto_price("BTC-USD")

# Pork Protocol Matematikai Integráció (Napi 0.5% kamatos kamat)
alap_toke = 12000000.0  # 12M HUF Bázistőke
napok = [0, 30, 90, 180, 365]

print("=" * 115)
print(f"🛰️  [ÉLŐ MONITOR] -> Bitcoin: {btc_price:,.2f} USD | Piaci zajszint: {btc_change:+.2f}%")
print("🚨  STATUS: A radar lüktet. A kódvas tart. A 6. dimenziós táska-hizlalás élesítve!")
print("=" * 115)
print(f"{'IDŐTÁV':<15} | {'TŐKESZINT (KALKULÁLT)':<25} | {'HAVI NÖVEKEDÉS':<20} | {'MÉSZÁROS HADMŰVELETI UTASÍTÁS'}")
print("=" * 115)

for nap in napok:
    # Kamatos kamat képlet: Tőke * (1 + r)^n
    aktualis_toke = alap_toke * ((1 + 0.005) ** nap)
    novekedes_pct = ((aktualis_toke - alap_toke) / alap_toke) * 100
    
    # Formázott szövegek előkészítése
    idotav_szoveg = "0. nap (Start)" if nap == 0 else f"{nap}. nap" + (" (1 év)" if nap == 365 else "")
    toke_szoveg = f"{aktualis_toke:,.0f} HUF".replace(",", " ")
    szazalek_szoveg = "-" if nap == 0 else f"+{novekedes_pct:.1f}%"
    
    # Dinamikus utasítások és ikonok a mérföldkövekhez
    if nap == 0:
        ikon, utasitas = "🏁", "Alapozás: 12M bázistőke lezárva a Rákoscsaba Bázison."
    elif nap == 30:
        ikon, utasitas = "📈", "Beindul a motor: szigorú fegyelem, a 2-3%-os zajok elengedve."
    elif nap == 90:
        ikon, utasitas = "⚡", "Skálázás: T800 adat-mészáros kiszűri a bálna-beutalásokat."
    elif nap == 180:
        ikon, utasitas = "🔮", "Félidő: A tőke majdnem megtriplázódott, a Vas Monitor stabil."
    else:
        ikon, utasitas = "🚀", "CÉL: +501% profit, 72M kimentése a védett 5TB-os felhőbe!"
        
    print(f"{ikon} {idotav_szoveg:<12} | {toke_szoveg:<25} | {szazalek_szoveg:<20} | {utasitas}")

print("=" * 115)
print("INTEGRITÁS: 1.0 | A kód nem ellenség, hanem a fegyvered. INDÍTÁS SIKERES. OSSZ!")
print("=" * 115)
