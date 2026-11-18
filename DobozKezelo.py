import json

class DobozKezelo:
    def __init__(self):
        # Doboz kapacitások / szabályok definiálása
        self.dobozok = {}
        
    def cuccok_be pakolasa(self, tetel_lista):
        print("=== BORSODI LOGISZTIKAI ÉS CSOMAGOLÓ MOTOR ===")
        osszes_db = 0
        
        for tetel in tetel_lista:
            nev = tetel["nev"]
            mennyiseg = tetel["db"]
            cél_doboz = tetel["doboz_tipus"]
            
            if cél_doboz not in self.dobozok:
                self.dobozok[cél_doboz] = []
                
            self.dobozok[cél_doboz].append({
                "termek": nev,
                "db": mennyiseg,
                "alkohol": tetel.get("alkohol", "33%")
            })
            osszes_db += mennyiseg
            
        print(f"Sikeresen elosztva {osszes_db} db egység a dobozok között.\n")
        return self.dobozok

    def jelentés_keszites(self):
        print("--- AKTUÁLIS DOBOZOLÁSI JEGYZÉK ---")
        for doboz_kod, elemek in self.dobozok.items():
            print(f"\n📦 Doboz / Hely: [{doboz_kod}]")
            doboz_osszeg = sum(e["db"] for e in elemek)
            for elem in elemek:
                print(f"   - {elem['termek']} ({elem['alkohol']}): {elem['db']} db")
            print(f"   -> Doboz összesen: {doboz_osszeg} db termék")

# Példa adatok a feltöltött képek (Csévi termékek, címkék, montírok) alapján:
if __name__ == "__main__":
    raktar_tetalek = [
        {"nev": "Csévi KÖRTE ízű sz.", "alkohol": "33%", "db": 50000, "doboz_tipus": "B/6"},
        {"nev": "Csévi BRUNDY sz.", "alkohol": "33%", "db": 20000, "doboz_tipus": "A/4"},
        {"nev": "Csévi Kevert", "alkohol": "20%", "db": 10000, "doboz_tipus": "A/2"},
        {"nev": "Csévi Cherry", "alkohol": "20%", "db": 20000, "doboz_tipus": "A/4"},
        {"nev": "Csévi Keserűlikőr", "alkohol": "24%", "db": 20000, "doboz_tipus": "A/4"},
        {"nev": "Szívós Démonn", "alkohol": "34%", "db": 50000, "doboz_tipus": "B/6"},
        {"nev": "Csévi DÉMON keserűlikőr", "alkohol": "33%", "db": 200000, "doboz_tipus": "B/24"},
        {"nev": "Sósborszesz", "alkohol": "40%", "db": 10000, "doboz_tipus": "A/2"},
        # Külön vodkás szerelék / egyéb PET palackok
        {"nev": "Csévi VODKOVA sz.", "alkohol": "33%", "db": 100000, "doboz_tipus": "W48-ra"},
        {"nev": "Csévi VODKOVA sz. PET", "alkohol": "33%", "db": 50000, "doboz_tipus": "0.05Pet"},
    ]

    motor = DobozKezelo()
    motor.cuccok_be pakolasa(raktar_tetalek)
    motor.jelentés_keszites()
