import numpy as np

class MonteCarloEngine:
    """
    Modul specifikáció az automatizált README generátorhoz.
    """
    module_desc = """
    LEÍRÁS (HU): Monte Carlo szimulációs motor. A piaci káoszt modellezi több ezer lehetséges jövőbeli 
    forgatókönyv futtatásával. Nem jósolja meg az árat, hanem a "szélsőértékeket" (összeomlás/csúcs) 
    térképezi fel. A Borsodi operátor ezzel a modullal méri a kockázatot a vakszerencse helyett.

    DESCRIPTION (EN): Monte Carlo simulation engine. Models market chaos by running thousands 
    of potential future scenarios. Does not predict the price; instead, it maps out the extremes 
    (crash/peak). Used by the Borsodi operator to quantify risk instead of relying on blind luck.

    SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM
    """

    def __init__(self, alap_ar, volatilitas):
        self.alap_ar = alap_ar
        self.volatilitas = volatilitas 
    
    # Don Mérnök Extra: Súlyozott stabilitási faktor
    # Ha az érték túl magas (> 104), az integritásnak is nőnie kell
    szukseges_szint = self.min_stabilitasi_szint

    if adat['ertek'] > 104:
        szukseges_szint += 0.05  # Magasabb árfolyamnál szigorúbb ellenőrzés

    if adat['integritás'] >= szukseges_szint:
        return True, f"STABIL ({szukseges_szint:.2%}) - Mehet a Market Killing ✅"
    else:
        return False, f"INSTABIL - Küszöb: {szukseges_szint:.2%} ❌"
class MonteCarloEngine:
    def __init__(self, alap_ar, volatilitas):
        self.alap_ar = alap_ar
        self.volatilitas = volatilitas # A "Pista bá' féle rángatódzás" mértéke

    def szimulal(self, napok=30, szimulaciok=5000):
        # Don Mérnök: Nem a jövőt nézzük, hanem a kereteket.
        # Geometriai Brown-mozgás a káosz szimulálására.
        dt = 1/252 # Napi lépés
        mu = 0.0001 # Drift (kicsi, mert a piac nem jótékony)
        
        hozzamok = np.random.normal(mu * dt, self.volatilitas * np.sqrt(dt), (napok, szimulaciok))
        arak = self.alap_ar * np.exp(np.cumsum(hozzamok, axis=0))
        
        # Stabilitási küszöb: Hány százalékban esik be a tőke a 0.5x szint alá?
        osszeomlas_esely = np.sum(arak[-1] < (self.alap_ar * 0.5)) / szimulaciok
        
        print(f"\n[v161] MONTE CARLO - 5000 jövő futtatva.")
        print(f">>> Pista bá': 'Ha 5% felett van az esély a bedőlésre, húzd meg a gatyát!'")
        return osszeomlas_esely

# Don Mérnök teszt:
engine = MonteCarloEngine(alap_ar=62000, volatilitas=0.03)
print(f"Összeomlási valószínűség: {engine.szimulal():.2%}")
