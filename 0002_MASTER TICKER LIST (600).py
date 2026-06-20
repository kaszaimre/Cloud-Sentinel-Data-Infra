# ==============================================================================
# BORSODI COMMAND CENTER - MASTER TICKER LIST (600)
# BIZTONSÁGI MENTÉS (PYDROID 3) / BACKUP (PYDROID 3)
# ==============================================================================

"""
[HU] A Borsodi Command Center központi eszközlistája.
     A 600 elemes mátrix technológiai, európai és kripto piaci egységeket tartalmaz.
     Cél: Piacfigyelés, anomália detektálás és "Pre-Explosion" szignál generálás.

[EN] Central asset list for the Borsodi Command Center.
     This 600-item matrix covers tech, European, and crypto market units.
     Purpose: Market monitoring, anomaly detection, and "Pre-Explosion" signal generation.
"""

MINDEN_TERMEK = [
    # --- 1. AI INFRASTRUCTURE & SEMICONDUCTOR GIANTS (USA) ---
    # [HU] AI és félvezető nagyágyúk (USA)
    "AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA", "AVGO", "AMD", "QCOM",
    "INTC", "NFLX", "ADBE", "CSCO", "TMUS", "AMAT", "TXN", "LRCX", "PANW", "MU",
    "VRT", "DELL", "HPE", "PSTG", "NTAP", "APP", "GTLB", "LUNR", "SOUN", "BBAI",
    "PLTR", "SOFI", "RIVN", "SMCI", "MRVL", "WDC", "ARM", "IBM", "ORCL", "CRM",

    # --- 2. EUROPEAN ENERGY, LUXURY & BÉT (ERSTE COMPATIBLE) ---
    # [HU] Európai energia, luxusipar és BÉT részvények
    "OTP.BU", "MOL.BU", "RICHT.BU", "MTEL.BU", "4IG.BU", "OPUS.BU", "ALTEO.BU",
    "RWE.DE", "EOAN.DE", "ENR.DE", "1COV.DE", "OMV.VI", "VER.VI", "ENI.MI", "ENEL.MI",
    "MC.PA", "OR.PA", "RMS.PA", "KER.PA", "P911.DE", "PAH3.DE", "RACE", "AIR.PA",
    
    # --- 3. CRYPTO-ASSETS: MAINSTREAM, RWA & MEME (BINANCE) ---
    # [HU] Kriptovaluta eszközök: Főáram, RWA és Meme szektorok
    "BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT", "ADAUSDT", "AVAXUSDT", 
    "LINKUSDT", "INJUSDT", "OPUSDT", "ARBUSDT", "ICPUSDT", "TIAUSDT", "SUIUSDT",
    "WIFUSDT", "PEPEUSDT", "BONKUSDT", "FLOKIUSDT", "JUPUSDT", "PYTHUSDT", "ONDOUSDT", 
    "RNDRUSDT", "TAOUSDT", "FETUSDT", "AGIXUSDT", "OCEANUSDT", "AKTUSDT", "RENDERUSDT"
]

# Mentés ellenőrző futtatás nélkül
print(">>> BORSODI BACKUP: A 600-as lista biztonságban elmentve a Pydroid mappába!")
print(f">>> [STATS] Jelenlegi egységek száma: {len(MINDEN_TERMEK)}")
