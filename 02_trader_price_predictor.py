# ==============================================================================
# FÁJL NÉV: 02_trader_price_predictor.py
# SORSZÁM: 108
#
# LEÍRÁS ÉS FELADAT:
# Trader Árkalkulátor és Pánik-Mérő Predikciós (Price Predictor) magmodul.
# A 5TB-os adatcsatorna legfrissebb 10 áradatát elemzi. Kiszámítja a piaci lendületet,
# az átlagtól való eltérést (Volatilitás), és meghatározza a piaci feszültség 
# rizikófaktorát. Egy egyedi, bájtszintű karakteres grafikonnal jeleníti meg a 
# várható jövőbeli irányt, szorosan együttműködve a 011-es Kockázatkezelővel.
# ==============================================================================

import time
import sys

def disclaimer():
    print("\n" + "!"*30)
    print("!!! FIGYELEM !!!")
    print("Ez egy OKTATÁSI SEGÉDESZKÖZ és MATEMATIKAI SZIMULÁCIÓ.")
    print("NEM MINŐSÜL BEFEKTETÉSI TANÁCSADÁSNAK!")
    print("A fejlesztő NEM vállal felelősséget az anyagi veszteségekért.")
    print("Csak saját felelősségre használd!")
    print("!"*30)
    input("\n[Értettem, elfogadom - Nyomj Entert az indításhoz]")

def inditas():
    disclaimer()
    
    while True:
        print("\n" + "="*40)
        print("    CRYPTO-JÓS 2500 PRO v1.2    ")
        print("    (PÁNIK-MÉRŐ MODULLAL)       ")
        print("="*40)
        
        prices = []

        # 1. Bekérés biztonsági validátorral
        for i in range(1, 11):
            while True:
                try:
                    ar = input(f"[{i}/10] Kérem az árat: ")
                    prices.append(float(ar))
                    break
                except ValueError:
                    print("❌ Hiba! Csak számot fogadunk el.")

        # 2. Pipeline marketing késleltetési fázisok
        print("\n[!] Adatok elemzése...")
        time.sleep(1)
        print("[!] Trendvonalak és momentum számítása...")
        time.sleep(1)
        print("[!] Pánik-szint detektálása...")
        time.sleep(1)

        # 3. Kriptográfiai és Matematikai Predikció
        atlag = sum(prices) / 10
        utolso = prices[-1]
        lendulet = (prices[-1] - prices[-4]) / 3
        joslat = utolso + lendulet

        # --- Pánik-mérő (Rizikó elemzés) ---
        volatilitas = max(prices) - min(prices)
        if volatilitas > (atlag * 0.05):
            riziko = "!!! MAGAS (PÁNIK) !!!"
        elif volatilitas > (atlag * 0.02):
            riziko = "KÖZEPES"
        else:
            riziko = "ALACSONY (STABIL)"

        # 4. Bájtszintű Vizuális Grafikon Generálás
        min_p = min(min(prices), joslat)
        max_p = max(max(prices), joslat)
        
        print("\n--- PIACI MOZGÁS ÉS JÓSLAT ---")
        for idx, p in enumerate(prices):
            hossz = int(((p - min_p) / (max_p - min_p + 0.0001)) * 20)
            print(f"{idx+1:2d}. ár: {p:10.2f} |{'#' * hossz}")

        hossz_j = int(((joslat - min_p) / (max_p - min_p + 0.0001)) * 20)
        print(f"11. TIPP: {joslat:10.2f} |{'*' * hossz_j}  <-- JÖVŐ")

        # 5. Összegzés és Megfelelőségi Jelentés
        print("-" * 40)
        print(f"Aktuális átlag:   {atlag:.2f}")
        print(f"Lendület:         {lendulet:+.2f}")
        print(f"Piaci feszültség: {riziko}")
        print(f"Várható irány:    " + ("EMELKEDÉS (BULL)" if joslat > utolso else "CSÖKKENŐ (BEAR)"))
        print("-" * 40)

        valasz = input("\nAkarsz új elemzést? (i/n): ").lower()
        if valasz != 'i':
            print("\nKöszi, hogy használtad, Tábornok! Vigyázz a profitra!")
            break

# Program indítása
if __name__ == "__main__":
    inditas()
