import numpy as np

def pre_explosion_radar_v2(prices, volumes, spy_prices, sector_prices, has_catalyst=False):
    # --- 1. GOLYÓÁLLÓ ADATELLENŐRZÉS (Minden idősor hossza kritikus) ---
    if min(len(prices), len(volumes), len(spy_prices), len(sector_prices)) < 200:
        return "Kevés adat. Minimum 200 gyertya kell minden idősorból, különben fejreáll a rendszer!"

    # Átalakítás NumPy tömbökké
    prices = np.array(prices, dtype=float)
    volumes = np.array(volumes, dtype=float)
    spy_prices = np.array(spy_prices, dtype=float)
    sector_prices = np.array(sector_prices, dtype=float)

    score = 0
    utolso_ar = prices[-1]
    
    # --- 2. RELATÍV ERŐ VS SPY (20 PONT) ---
    stock_return_20d = (prices[-1] - prices[-20]) / prices[-20]
    spy_return_20d = (spy_prices[-1] - spy_prices[-20]) / spy_prices[-20]
    if stock_return_20d > spy_return_20d:
        score += 20

    # --- 3. EGZAKT VOLATILITÁS-KOMPRESSZIÓ HOZAMOKON (20 PONT) ---
    # Tiszta hozamszámítás a torzítások ellen
    returns = np.diff(prices) / prices[:-1]
    
    # Recent (utolsó 20 nap) vs Historical (korábbi 100 nap, az utolsó 20 nélkül)
    recent_vol = np.std(returns[-20:])
    historical_vol = np.std(returns[-120:-20])
    
    if historical_vol > 0 and recent_vol < historical_vol * 0.7:
        score += 20

    # --- 4. VOLUMEN-AKUMULÁCIÓ (20 PONT) ---
    # Fel napokon nagyobb-e a volumen, mint a le napokon az utolsó 20 napban
    price_diffs = np.diff(prices[-20:])
    recent_volumes = volumes[-19:]
    up_volume = np.sum(recent_volumes[price_diffs > 0])
    down_volume = np.sum(recent_volumes[price_diffs < 0])
    if up_volume > down_volume:
        score += 20

    # --- 5. SZERKEZETI BÁZIS / MOZGÓÁTLAGOK (15 PONT) ---
    ma50 = prices[-50:].mean()
    ma200 = prices[-200:].mean()
    if utolso_ar > ma50 and ma50 > ma200:
        score += 15

    # --- 6. SZEKTOR ERŐSÖDÉS (10 PONT) ---
    sector_return_20d = (sector_prices[-1] - sector_prices[-20]) / sector_prices[-20]
    if sector_return_20d > 0:
        score += 10

    # --- 7. KATALIZÁTOR / KÉZI EVENT CSATORNA (10 PONT) ---
    if has_catalyst:
        score += 10

    # --- 8. EMELKEDŐ MÉLYPONTOK ALAP-ELLENŐRZÉSE (5 PONT) ---
    lows = [prices[-20:].min(), prices[-50:-20].min()]
    if lows[0] > lows[1]:
        score += 5

    # --- PARANCSNOKI JELENTÉS KIADÁSA ---
    print(f"=== PARANCSNOKI JELENTÉS | SCORE: {score}/100 ===")
    print(f"Utolsó ár: {utolso_ar:.2f} | Recent Vol: {recent_vol*100:.2f}% | Hist Vol: {historical_vol*100:.2f}%")
    
    if score >= 90:
        return "🚨 RADAR ALERT! A disznó még nem repül, de már gyanúsan nézi a kifutópályát. Breakout + Volume megerősítésre várunk (Setup Confirmed)!"
    elif score >= 80:
        return "👀 WATCHLIST! Nyomásépülés detektálva a silóban. Folyamatos megfigyelés elrendelve."
    else:
        return "A chart alszik. Nincs kritikus feszültség."

# Teszt futtatás
print("Golyóálló Pre-Explosion Radar v2 sikeresen betöltve.")
