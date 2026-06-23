# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 175_PHOENIX_MARKET_SENTIMENT_TRACKER.py
# 
module_desc = """ 
LEÍRÁS (HU):

Piaci hangulat-követő és pszichológiai anomália mérő modul (Sentiment Tracker).
A Phoenix Master Oracle v5.1 új generációs adatszűrője. Monitorozza az extrém 
piaci félelmet és mohóságot (Fear & Greed Index), megvédve a rendszert a 
lakossági pánik és a FOMO okozta hirtelen piaci kirázásoktól.
Mottó: A borsodi nem hackel, a borsodi optimalizál.

DESCRIPTION (EN):

Market sentiment tracker and psychological anomaly measurement module.
The next-gen data filter of the Phoenix Master Oracle v5.1. Monitors extreme 
market fear and greed (Fear & Greed Index), protecting the system from sudden 
market shakeouts caused by retail panic and FOMO.
Motto: The Borsodi doesn't hack, the Borsodi optimizes.

SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM """
# ==============================================================================

import time
from datetime import datetime

def analyze_market_sentiment(fear_greed_score):
    """
    Tiszta logikájú piac-pszichológiai szűrőrendszer.
    0-100 közötti index alapján határozza meg a kockázati szinteket.
    """
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [SENTIMENT] Globális piaci hangulat elemzése...")
    time.sleep(0.4)
    
    if fear_greed_score >= 85:
        return "🚨 EXTRÉM MOHÓSÁG (FOMO ZÓNA) - Fokozott kirázás veszély! Kereskedési méret csökkentése kötelező."
    elif fear_greed_score <= 15:
        return "😱 EXTRÉM FÉLELEM (PÁNIK ZÓNA) - Likviditási kapituláció lehetséges. Fokozott óvatosság."
    else:
        return "🟢 STABIL HANGULAT - A lakossági pszichológia egyensúlyban van. Végrehajtás engedélyezve."

if __name__ == "__main__":
    print("=== 172_phoenix_market_sentiment_tracker INDÍTÁSA ===")
    time.sleep(0.5)
    
    # Teszt környezet: Szimulálunk egy túlhevült, 88-as mohósági indexet a kriptopiacon (FOMO)
    current_fear_greed = 88
    
    sentiment_report = analyze_market_sentiment(current_fear_greed)
    
    print(f"\n[SENTIMENT REPORT] [{datetime.now().strftime('%H:%M:%S')}]")
    print(f"-> Vizsgált index:     Fear & Greed Index")
    print(f"-> Aktuális érték:     {current_fear_greed} / 100")
    print("-" * 65)
    print(f"-> Oracle értékelés:   {sentiment_report}")
    print("-> T800 Kernel státusz: [✓] SENTIMENT SCANNER OPERATIONAL")
    
    print("\n[✓] A 172-es modul sikeresen lefutott, az új generációs blokk tovább bővült.")
