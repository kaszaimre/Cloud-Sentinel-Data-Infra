def biztonsagi_szuro(self, adat):
    """
    Modul specifikáció az automatizált README generátorhoz.
    """
    module_desc = """
    LEÍRÁS (HU): Súlyozott stabilitási faktorral dolgozó biztonsági szűrő. Ellenőrzi az adat integritását 
    és a piaci stabilitást. 104-es érték felett szigorított módban fut, megakadályozva a 
    'vaktában lövést'. A 'Borsodi' rendszer elsődleges védelmi vonala a Market Killing előtt.

    DESCRIPTION (EN): Weighted stability factor security filter. Validates data integrity and 
    market stability. Runs in strict mode above a value of 104 to prevent reckless operations. 
    The primary defense line of the 'Borsodi' system before executing Market Killing commands.

    SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM 
    """
    
    # Don Mérnök Extra: Súlyozott stabilitási faktor
    # Ha az érték túl magas (> 104), az integritásnak is nőnie kell
    szukseges_szint = self.min_stabilitasi_szint

    if adat['ertek'] > 104:
        szukseges_szint += 0.05  # Magasabb árfolyamnál szigorúbb ellenőrzés

    if adat['integritás'] >= szukseges_szint:
        return True, f"STABIL ({szukseges_szint:.2%}) - Mehet a Market Killing ✅"
    else:
        return False, f"INSTABIL - Küszöb: {szukseges_szint:.2%} ❌"
class BorsodiUnitTest:
    def __init__(self, modul_nev):
        self.modul_nev = modul_nev
        self.teszt_siker = 0
        self.teszt_bukas = 0

    def assert_integritas(self, feltetel, uzenet):
        if feltetel:
            self.teszt_siker += 1
            print(f"  [OK] {uzenet}")
        else:
            self.teszt_bukas += 1
            print(f"  [!!] HIBA: {uzenet}")

    def report(self):
        print(f"\n--- {self.modul_nev} VALIDÁCIÓ ---")
        print(f"Siker: {self.teszt_siker} | Bukás: {self.teszt_bukas}")
        if self.teszt_bukas > 0:
            print(">>> Pista bá': 'Fiam, ez a kód még nyers, ne pörkölj vele!'")
        else:
            print(">>> Pista bá': 'Ez a vas tiszta, mehet a Market Killing!'")

# Használat egy modul tesztelésére:
teszt = BorsodiUnitTest("Pork_Protocol_v3")
teszt.assert_integritas(5 > 2, "Adatfolyam inicializálva")
teszt.assert_integritas(True, "Integritás-szint > 0.85")
teszt.report()
