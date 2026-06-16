import numpy as np

def pre_explosion_radar(prices, volumes, spy_prices, sector_prices, has_catalyst=False):
    prices = np.array(prices, dtype=float)
    volumes = np.array(volumes, dtype=float)
    spy_prices = np.array(spy_prices, dtype=float)
    sector_prices = np.array(sector_prices, dtype=float)

    if len(prices) < 200:
        return "Kevés adat a 200 napos MA és a szerkezeti bázis elemzéséhez."

    score = 0
    utolso_ar = prices[-1]
    
    # --- 1. RELATÍV ERŐ (20 PONT) ---
    stock_return = (prices[-1] - prices[-20]) / prices[-20]
    spy_return = (spy_prices[-1] - spy_prices[-20]) / spy_prices[-20]
    if stock_return > spy_return:
        score += 20

    # --- 2. VOLATILITÁS-KOMPRESSZIÓ (20 PONT) ---
    # Bollinger Band Width szűkülés detektálás
    std_recent = np.std(prices[-20:])
    std_historical = np.std(prices[-100:])
    if std_recent < std_historical * 0.7:  # Ha a mostani volatilitás 30%-kal kisebb a történelminél
        score += 20

    # --- 3. VOLUMEN-AKUMULÁCIÓ (20 PONT) ---
    # Fel napokon nagyobb-e a volumen, mint a le napokon
    price_diffs = np.diff(prices[-20:])
    recent_volumes = volumes[-19:]
    up_volume = np.sum(recent_volumes[price_diffs > 0])
    down_volume = np.sum(recent_volumes[price_diffs < 0])
    if up_volume > down_volume:
        score += 20

    # --- 4. SZERKEZETI BÁZIS / MOZGÓÁTLAGOK (15 PONT) ---
    ma50 = prices[-50:].mean()
    ma200 = prices[-200:].mean()
    if utolso_ar > ma50 and ma50 > ma200:
        score += 15

    # --- 5. SZEKTOR ERŐSÖDÉS (10 PONT) ---
    sector_return = (sector_prices[-1] - sector_prices[-20]) / sector_prices[-20]
    if sector_return > 0:
        score += 10

    # --- 6. KATALIZÁTOR / NEWS EVENT (10 PONT) ---
    if has_catalyst:
        score += 10

    # --- 7. TISZTA CHARTBÁZIS / MAGASABB MÉLYPONTOK (5 PONT) ---
    lows = [prices[-20:].min(), prices[-50:-20].min()]
    if lows[0] > lows[1]:  # Magasabb mélypont detektálása
        score += 5

    # --- ADATOK KIIRATÁSA ---
    print(f"=== PARANCSNOKI JELENTÉS: {score} PONT ===")
    print(f"Aktuális ár: {utolso_ar:.2f} | MA50: {ma50:.2f} | MA200: {ma200:.2f}")
    
    if score >= 90:
        return "🚨 RIASZTÁS! A silófedél füstöl, a disznón elszakadt a mellény! AKCIÓKÉSZSÉG!"
    elif score >= 80:
        return "👀 FIGYELŐLISTA! Tábornok, itt valami nagyon készül a háttérben..."
    else:
        return "A piac csendes. A Pork Protocol fingott egyet a szerverteremben."

# Teszteléshez üres futtatás:
print("Pre-Explosion Radar Kernel sikeresen betöltve.")
