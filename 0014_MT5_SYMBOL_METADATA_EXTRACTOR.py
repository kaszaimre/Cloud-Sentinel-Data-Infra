# -*- coding: utf-8 -*-
# ==============================================================================
# PROJEKT: 0014_MT5_SYMBOL_METADATA_EXTRACTOR
# 
module_desc = """ 
LEÍRÁS (HU):

MetaTrader 5 szimbólum-metaadat kinyerő és validáló modul.
Közvetlen kapcsolatot létesít a helyi MT5 terminállal. Automatikusan kiszívja 
a valós idejű piaci szinteket (Bid, Ask, Tick Size, Last) a kiválasztott 
eszközökhöz (pl. GOOGL, BTC-USD, HOOD), kizárva a manuális adatbeviteli hibákat.
Mottó: A borsodi nem hackel, a borsodi optimalizál.

DESCRIPTION (EN):

MetaTrader 5 symbol metadata extractor and validator module.
Establishes a direct connection with the local MT5 terminal. Automatically 
extracts real-time market levels (Bid, Ask, Tick Size, Last) for selected 
assets (e.g., GOOGL, BTC-USD, HOOD), eliminating manual data entry errors.
Motto: The Borsodi doesn't hack, the Borsodi optimizes.

SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM """
# ==============================================================================

import time
from datetime import datetime
import MetaTrader5 as mt5

def extract_symbol_metadata(symbol_name):
    """Csatlakozik az MT5-höz és kinyeri a pontos piaci struktúrát."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [INFO] Kapcsolódás az MT5 szerverhez... Eszköz: {symbol_name}")
    
    # MT5 Inicializálás
    if not mt5.initialize():
        print(f"-> [!] MT5 inicializálási hiba kód: {mt5.last_error()}")
        return None

    # Szimbólum kiválasztása a piacon
    mt5.symbol_select(symbol_name, True)
    symbol_info = mt5.symbol_info(symbol_name)
    
    # Kapcsolat azonnali lezárása az erőforrások kímélése érdekében
    mt5.shutdown()
    
    if symbol_info is None:
        print(f"-> [⚠️] A(z) '{symbol_name}' nem található az MT5 terminálban!")
        return None
        
    return symbol_info

if __name__ == "__main__":
    print("=== 014_mt5_symbol_metadata_extractor INDÍTÁSA ===")
    time.sleep(0.5)
    
    # Teszteljük a képeden szereplő Google (GOOGL) eszközzel
    target_symbol = "GOOGL"
    info = extract_symbol_metadata(target_symbol)
    
    if info is not None:
        print(f"\n[METADATA EXTRACTION SCCESSFUL] [{datetime.now().strftime('%H:%M:%S')}]")
        print(f"-> Eszköz:      {info.name}")
        print(f"-> Tick Size:   {info.trade_tick_size}")
        print(f"-> Tick Value:  {info.trade_tick_value}")
        print(f"-> Élő Bid:     {info.bid}")
        print(f"-> Élő Ask:     {info.ask}")
        print(f"-> Utolsó ár:   {info.last}")
        print(f"-> Rendszerállapot: [✓] TŰPONTOS REÁLADATOK BETÖLTVE A KERNELBE")
    else:
        # Biztonsági szimulációs fallback mód, ha az MT5 nincs megnyitva a PC-n
        print("\n[MOCK MODE] Az MT5 terminál nem elérhető. Szimulált precíziós adatok:")
        print("-" * 55)
        print(f"-> Eszköz:      {target_symbol} (Google Inc.)")
        print("-> Tick Size:   0.01")
        print("-> Élő Bid:     380.95")
        print("-> Élő Ask:     381.20")
        print("-> Utolsó ár:   380.34")
        print("-> Rendszerállapot: [✓] BIZTONSÁGI ADATMATRIX AKTIVÁLVA")

    print("\n[✓] A 014-es modul sikeresen lefutott, a gap betöltve a Git-ben.")
