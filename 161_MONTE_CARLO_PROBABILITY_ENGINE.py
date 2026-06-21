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
        # Don Mérnök extra: volatilitás + A "Pista bá' féle rángatódzás" mértéke
        self.volatilitas = volatilitas 

    def ellenoriz_stabilitas(self, adat):
        """Don Mérnök extra: súlyozott stabilitási faktor ellenőrzése"""
        szukseges_szint = 0.5  # Alapértelmezett minimum szint
        
        if adat.get('ertek', 0) > 104:
            # Ha az érték túl magas (> 104), az integritásnak is nőnie kell
            szukseges_szint += 0.05  # Magasabb árfolyamnál szigorúbb ellenőrzés

        if adat.get('integritás', 0) >= szukseges_szint:
            return True, f"STABIL ((szukseges_szint: {szukseges_szint:.2f})) - Mehet a market killing 🚀"
        else:
            return False, f"INSTABIL - Küszöb: ({szukseges_szint:.2f}) ❌"

    def szimulal(self, napok=30, szimulaciok=5000):
        """
        Don Mérnök: nem a jövőt nézzük, hanem a kereteket.
        Geometriai Brown-mozgás a káosz szimulálására.
        """
        dt = 1 / 252  # Napi lépésköz (kereskedési napok alapján)
        mu = 0.0001   # Drift (kicsi, mert a piac nem jótékony)
        
        # Véletlenszerű sokkok generálása az összes szimulációra és napra egyszerre
        sokkok = np.random.normal(0, np.sqrt(dt), (napok, szimulaciok))
        
        # Átpályázás kalkulációja
        hozamok = np.exp((mu - 0.5 * self.volatilitas**2) * dt + self.volatilitas * sokkok)
        
        # Az indító sor feltöltése az alapárral
        ar_matrix = np.zeros((napok + 1, szimulaciok))
        ar_matrix[0] = self.alap_ar
        
        for t in range(1, napok + 1):
            ar_matrix[t] = ar_matrix[t - 1] * hozamok[t - 1]
            
        return ar_matrix
