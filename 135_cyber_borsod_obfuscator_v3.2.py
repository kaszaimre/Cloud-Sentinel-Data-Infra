#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================================
#   CYBER-BORSOD SECURITY CORE - PURE PYTHON LIVE NEWS OBFUSCATOR v3.2 (SSL BYPASS)
#   
#   LEÍRÁS (HU):
#   Ez a modul a v3.1 mobil-optimalizált, golyóálló változata. Tartalmaz egy beépített
#   SSL kontextus-kerülő áramkört, amely megakadályozza, hogy az Android/Termux
#   tanúsítvány-hibák miatt a kód lefagyjon az élő Google News RSS letöltése közben.
#   Ha a hálózat megszakad, az azonnali helyi tartalék rendszer lép életbe.
#   
#   DESCRIPTION (EN):
#   This module is the mobile-optimized, bulletproof version of v3.1. It features an
#   embedded SSL context bypass circuit to prevent Android/Termux certificate errors
#   from freezing the code during the live Google News RSS fetch. If the network
#   fails, the immediate local fallback system takes over automatically.
# ======================================================================================

import os
import random
import urllib.request
import xml.etree.ElementTree as ET
import ssl

def get_live_sports_noise():
    """Élő sporthírek letöltése SSL kerülővel / Fetching live sports news with SSL bypass"""
    print("[FETCH] Élő sporthírek lekérése a Google felhőből...")
    url = "https://google.com"
    
    try:
        # Védelmi vonal 1: SSL tanúsítvány ellenőrzés kikapcsolása a mobilhoz
        # Defense Line 1: Disabling SSL certificate verification for mobile
        context = ssl._create_unverified_context()
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=context, timeout=3) as response:
            xml_data = response.read()
        
        root = ET.fromstring(xml_data)
        titles = []
        for item in root.findall('.//item'):
            title = item.find('title').text
            if " - " in title:
                title = title.rsplit(" - ", 1)[0]
            titles.append(title)
            
        if titles:
            print(f"[OK] {len(titles)} élő hír sikeresen letöltve.")
            return titles
    except Exception as e:
        # Védelmi vonal 2: Ha hiba van, nem fagyunk ki, hanem azonnal átváltunk a helyi generátorra
        # Defense Line 2: If an error occurs, we don't freeze, we switch to local generator
        print(f"[WARN] Hálózati kapu zárva ({e}). Helyi álcázó modul aktiválva.")
    
    return [
        "Szoboszlai Dominik kőkemény bombagóllal döntötte el a hétvégi rangadót",
        "A magyar válogatott gőzerővel és taktikai fegyelemmel készül a meccsre",
        "Szenzációs átigazolási hírek és robbanásszerű bejelentések érkeztek a klubtól",
        "A szövetségi kapitány szerint a csapat készen áll a kiber-szintű összecsapásra"
    ]

def generate_live_camouflage(secret_message):
    """Álcázó szöveg összefűzése / Combining camouflage text"""
    news_pool = get_live_sports_noise()
    random.shuffle(news_pool)
    
    selected_news = news_pool[:4]
    mid = len(selected_news) // 2
    selected_news.insert(mid, f" {secret_message} ")
    
    return ". ".join(selected_news)

# --- FUTTATÁS ---
if __name__ == "__main__":
    print("=" * 55)
    print("   [+] CYBER-BORSOD PURE OBFUSCATION ENGINE v3.2 [+]   ")
    print("=" * 55)
    
    nyers_titok = "MINDENKI ANYJA IS ÁTMENT A SZŰRŐN"
    biztonsagi_szoveg = generate_live_camouflage(nyers_titok)
    
    print("\n" + "-" * 55)
    print("[RESULT] A Puzi Botoknak szánt, élő hírekkel védett szöveg:")
    print("-" * 55)
    print(biztonsagi_szoveg)
    print("-" * 55 + "\n")
    
    fajl_nev = "foci_live_news.log"
    try:
        with open(fajl_nev, "w", encoding="utf-8") as f:
            f.write(biztonsagi_szoveg)
        print(f"[SUCCESS] Az álcázott szöveges fájl elmentve: {fajl_nev}")
    except Exception as e:
        print(f"[ERROR] Fájlmentési hiba: {e}")
        
    print("=" * 55)
 
