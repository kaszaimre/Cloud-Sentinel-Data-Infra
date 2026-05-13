# ==============================================================================
# FÁJL NÉV: 046_secure_memory_wipe.py
# SORSZÁM: 046
#
# LEÍRÁS ÉS FELADAT:
# Biztonságos Memóriatisztító és Token-Megsemmisítő (Secure Memory Wipe) modul.
# Gondoskodik arról, hogy a kritikus kriptográfiai kulcsok, jelszavak és 
# API tokenek a használat után ne maradjanak benne a RAM memóriában. A modul 
# alacsony szintű memóriafelülírást szimulál (Garbage Collection kényszerítéssel 
# és nullázó bájtok beírásával), megakadályozva a Core Dump és Memory Dump alapú 
# adathalászatot.
# ==============================================================================

import sys
import gc
import ctypes

class SecureMemoryWiper:
    def __init__(self):
        self.log_file = "./sentinel_events.log"

    def wipe_string_buffer(self, target_string):
        print("=========================================================")
        print("   CYBER-BORSOD KERNEL -> SECURE RAM BUFFER WIPE CORE    ")
        print("=========================================================")
        print("[*] Locating internal variable memory pointers...")
        
        # Megkeressük a szöveg memóriacímét a RAM-ban
        memoria_cim = id(target_string)
        hossz = len(target_string)
        
        print(f"  [-] Target Object RAM Address: {hex(memoria_cim)}")
        print(f"  [-] Alloc Size: {hossz} characters. Initiating destruction pipeline...")
        
        try:
            # Alacsony szintű C-típusú karaktertömb elérése a memóriacím alapján
            # Közvetlenül felülírjuk a memóriaterületet nullákkal ('\x00')
            offset = sys.getsizeof(target_string) - hossz - 1
            ctypes.memset(memoria_cim + offset, 0, hossz)
            
            # Kényszerítjük a Python memóriatisztító motorját (Garbage Collector)
            gc.collect()
            
            print("[🟢 SUCCESS] Cryptographic memory block zeroed out successfully.")
            return True
        except Exception as e:
            print(f"[❌ ERROR] Memory pointer isolation failed: {e}")
            return False

if __name__ == "__main__":
    wiper = SecureMemoryWiper()
    
    # Érzékeny adat, amit azonnal meg kell semmisíteni a RAM-ból a lefutás után
    ideiglenes_titok = "MASTER_SESSION_KEY_ABC987654321"
    wiper.wipe_string_buffer(ideiglenes_titok)
    
    print("=========================================================")
