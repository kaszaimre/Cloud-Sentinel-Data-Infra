import pandas as pd
import random

# 1. Beállítások
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

try:
    # 2. Adatok betöltése
    df = pd.read_csv('Borsodi_Majomfa_Teremtes_V2.csv')
    
    # Csak az elitek
    elite_egységek = df[df['Kikelesi_Sebesseg_Nap'] <= 15]
    kivalasztott = elite_egységek.sample(1).iloc[0]
    
    # 3. Kiírás (Itt figyelj, hogy Profit_Szint legyen!)
    print(f"--- CSATA INDUL: {kivalasztott['Azonosito']} AKCIÓBAN! ---")
    print(f"Profit szint: {kivalasztott['Profit_Szint']} | Aratás: {kivalasztott['Varhato_Aratas']}")
    print("-" * 40)

    # 4. Játék rész
    lehetosegek = ["kő", "papír", "olló"]
    gep_dobasa = random.choice(lehetosegek)
    
    jatekos_dobasa = input("Válassz fegyvert (kő/papír/olló): ").lower()

    if jatekos_dobasa in lehetosegek:
        print(f"\n{kivalasztott['Azonosito']} dobása: {jatekos_dobasa}")
        print(f"Ellenség dobása: {gep_dobasa}")

        if jatekos_dobasa == gep_dobasa:
            print("DÖNTETLEN! A táskli elmarad.")
        elif (jatekos_dobasa == "kő" and gep_dobasa == "olló") or \
             (jatekos_dobasa == "papír" and gep_dobasa == "kő") or \
             (jatekos_dobasa == "olló" and gep_dobasa == "papír"):
            print(f"GYŐZELEM! {kivalasztott['Azonosito']} BRUTÁLISAN LEZÚZTA! OSS!")
        else:
            print("VESZTESÉG... A Nagy Majom elszomorodott.")
    else:
        print("Hibás fegyver! A brigád nem érti a parancsot.")

except Exception as e:
    print(f"HIBA történt: {e}")

print("\nFASA ÉS KÉSZ!")