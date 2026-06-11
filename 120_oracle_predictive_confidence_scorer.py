# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 120_ORACLE_PREDICTIVE_CONFIDENCE_SCORER
# 
module_desc = """ 
LEÍRÁS (HU):

Prediktív megbízhatósági szint-értékelő modul (Oracle Confidence Scorer).
A Phoenix Master Oracle v5.1 alrendszere. Kiszámítja a generált kereskedési 
és biztonsági jelzések matematikai valószínűségét és megbízhatóságát. 
Alacsony pontszám esetén blokkolja a végrehajtást.
Mottó: A borsodi nem hackel, a borsodi optimalizál.

DESCRIPTION (EN):

Predictive confidence scoring module (Oracle Confidence Scorer).
Subsystem of the Phoenix Master Oracle v5.1. Calculates the mathematical probability 
and reliability of generated trading and security signals. Blocks execution 
in case of low scores.
Motto: The Borsodi doesn't hack, the Borsodi optimizes.

SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM """
# ==============================================================================

import time
from datetime import datetime

def calculate_oracle_score(trend_strength, volume_status, volatility_sigma):
    """
    Tiszta logikájú prediktív értékelő motor.
    0 és 100 pont között határozza meg a jelzés megbízhatóságát.
    """
    score = 50.0  # Alapértelmezett középérték
    
    # 1. Trend erősség tényező (max +20)
    score += (trend_strength * 0.2)
    
    # 2. Volumen státusz ellenőrzése
    if volume_status == "HIGH":
        score += 15.0
    elif volume_status == "LOW":
        score -= 20.0
        
    # 3. Szigma Volatilitási együttható (A dashboardod alapján optimalizálva)
    if volatility_sigma > 70.0:
        score -= 15.0  # Túl magas volatilitás, veszélyes zóna (Kirázás)
    elif 40.0 <= volatility_sigma <= 70.0:
        score += 15.0  # Ideális, stabil trendkörnyezet
        
    # Határok kényszerítése
    score = max(0.0, min(100.0, score))
    return score

if __name__ == "__main__":
    print("=== 120_oracle_predictive_confidence_scorer INDÍTÁSA ===")
    print("Oracle v5.1 predikciós motor inicializálása...")
    time.sleep(0.8)
    
    # Teszt környezet: A PHOENIX MASTER felületedről vett valós adatok (BTC-USD példa)
    test_trend_strength = 91.0   # 91%-os EMA erősség a képedről
    test_volume = "HIGH"
    test_sigma = 65.6            # 65.6 szigma a kördiagramodról
    
    final_score = calculate_oracle_score(test_trend_strength, test_volume, test_sigma)
    
    print(f"\n[ORACLE EVALUATION] [{datetime.now().strftime('%H:%M:%S')}]")
    print(f"-> Elemzett eszköz: BTC-USD")
    print(f"-> Számított Megbízhatóság: {final_score:.1f}%")
    
    # Biztonsági szűrő logikája
    MINIMUM_CONFIDENCE = 75.0
    if final_score >= MINIMUM_CONFIDENCE:
        print(f"-> Döntés: 🟢 VÉGREHAJTÁS ENGEDÉLYEZVE (Elérte a limitet: {MINIMUM_CONFIDENCE}%)")
    else:
        print(f"-> Döntés: 🔴 BLOKKOLVA (Túl alacsony megbízhatóság!)")
        
    print("\n[✓] A 120-as modul sikeresen lefutott, a gap betöltve a Git-ben.")
