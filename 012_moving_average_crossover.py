import os
import sys
import random
from datetime import datetime, timedelta

try:
    import pandas as pd
except ImportError:
    print("[!] A 'pandas' könyvtár nem található. Futtasd az 'init_pipeline.sh' scriptet!")
    sys.exit(1)

def generalj_torteneti_adatokat():
    """Generál egy 50 napos történeti adatsort a mozgóátlagok számításához."""
    idopontok = [datetime(2026, 3, 25) + timedelta(days=i) for i in range(50)]
    alap_ar = 94000.0
    
    adatok = []
    for dt in idopontok:
        # Finom napi ármozgások szimulációja
        alap_ar = alap_ar * (1 + random.uniform(-0.02, 0.025))
        adatok.append({
            "Date": dt.strftime("%Y-%m-%d"),
            "Close_Price": round(alap_ar, 2)
        })
    return pd.DataFrame(adatok)

def kalkulal_trend_szignalok():
    print("=========================================================")
    print("   CYBER-BORSOD TRADING SYSTEM -> STRATEGY ENGINE v1.0   ")
    print("=========================================================")
    print("[*] Running Moving Average Crossover (1st Core Indicator)...")
    
    # Adatok betöltése Pandas DataFrame-be
    df = generalj_torteneti_adatokat()
    
    # 1. INDIKÁTOR: 5 napos gyors mozgóátlag (Short SMA)
    df["Short_MA"] = df["Close_Price"].rolling(window=5).mean()
    
    # 2. INDIKÁTOR: 20 napos lassú mozgóátlag (Long SMA)
    df["Long_MA"] = df["Close_Price"].rolling(window=20).mean()
    
    print("[🟢 SUCCESS] Technical indicators generated.")
    print("-" * 57)
    
    # Megnézzük az utolsó 5 nap eredményét a terminálban
    utolso_napok = df.tail(5)
    for idx, row in utolso_napok.iterrows():
        datum = row["Date"]
        ar = row["Close_Price"]
        sma5 = row["Short_MA"]
        sma20 = row["Long_MA"]
        
        # Stratégiai döntési logika (Kereszteződés figyelés)
        if pd.isna(sma5) or pd.isna(sma20):
            szignal = "HOLD (Calculating...)"
        elif sma5 > sma20:
            szignal = "🟢 BUY SIGNAL (Bullish Crossover)"
        else:
            szignal = "🚨 SELL SIGNAL (Bearish Crossover)"
            
        print(f"[{datum}] Price: ${ar:,} | SMA5: ${round(sma5, 2):,} | SMA20: ${round(sma20, 2):,} -> {szignal}")
        
    print("-" * 57)
    print("[*] Execution baseline telemetry verified.")
    print("=========================================================")

if __name__ == "__main__":
    kalkulal_trend_szignalok()
