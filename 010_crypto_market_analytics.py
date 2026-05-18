import os
import sys
import random
from datetime import datetime, timedelta

# Biztonsági ellenőrzés: megpróbáljuk beimportálni a frissen telepített könyvtárakat
try:
    import pandas as pd
except ImportError:
    print("[!] A 'pandas' könyvtár nem található. Futtasd az 'init_pipeline.sh' scriptet!")
    sys.exit(1)

def generalj_piaci_adatokat():
    """Szimulált 5TB-os Parquet adatfolyam mintavételezés a 2025/2026-os piacról."""
    idopontok = [datetime(2025, 1, 1) + timedelta(days=i) for i in range(100)]
    alap_ar = 95000.0
    
    adatok = []
    for dt in idopontok:
        # Véletlenszerű piaci mozgások szimulációja (-3% és +4% között)
        valtozas = random.uniform(-0.03, 0.04)
        alap_ar = alap_ar * (1 + valtozas)
        volumen = random.uniform(1500, 5000)
        
        adatok.append({
            "Timestamp": dt.strftime("%Y-%m-%d"),
            "Asset": "BTC",
            "Price_USD": round(alap_ar, 2),
            "Volume_24h": round(volumen, 2)
        })
    return pd.DataFrame(adatok)

def run_market_pipeline():
    print("=========================================================")
    print("   CYBER-BORSOD FINANCIAL CORE -> BIG DATA PIPELINE v1.0")
    print("=========================================================")
    print("[*] Accessing high-frequency telemetry storage layer...")
    
    # Adatok generálása / betöltése a DataFrame-be
    df = generalj_piaci_adatokat()
    
    # Statisztikai számítások végrehajtása Pandas segítségével
    max_ar = df["Price_USD"].max()
    min_ar = df["Price_USD"].min()
    atlag_ar = df["Price_USD"].mean()
    osszes_volumen = df["Volume_24h"].sum()
    
    print(f"[🟢 SUCCESS] Processed {len(df)} market data rows successfully.")
    print("-" * 57)
    print(f"[*] Asset Identification   : BTC/USD Cluster")
    print(f"[*] Maximum Target Price   : ${max_ar:,} USD")
    print(f"[*] Minimum Target Price   : ${min_ar:,} USD")
    print(f"[*] Baseline Average Price : ${round(atlag_ar, 2):,} USD")
    print(f"[*] Total Pipeline Volume  : {round(osszes_volumen, 2):,} High-Freq Units")
    print("-" * 57)
    
    # Eredmények kimentése CSV jelentésbe a 'raw_market_data' mappába
    output_dir = "./cyber_borsod_core/raw_market_data"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "btc_analytics_report.csv")
    
    df.to_csv(output_path, index=False)
    print(f"[🟢 REPORT GENERATED] Saved to: {output_path}")
    print("=========================================================")

if __name__ == "__main__":
    run_market_pipeline()
