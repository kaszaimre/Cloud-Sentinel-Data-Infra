# ==============================================================================
# FÁJL NÉV: 028_memory_buffer_overflow_shield.py
# SORSZÁM: 028
#
# LEÍRÁS ÉS FELADAT:
# Memóriapuffer-túlcsordulás elleni védelmi modul (Buffer Overflow Shield). 
# Alacsony szintű beviteli adatfolyamokat ellenőriz a C-alapú memóriakezelő 
# rendszerek előtt. Ha a beérkező adatméret meghaladja a lefoglalt statikus 
# pufferméretet, a modul azonnal elvágja a bevitelt és izolálja a szálat, 
# megakadályozva a tetszőleges kódvégrehajtást (RCE).
# ==============================================================================

import sys

class BufferOverflowShield:
    def __init__(self, static_buffer_size=1024):
        """
        static_buffer_size: A lefoglalt biztonságos memóriaterület bájtban (alapértelmezett: 1KB)
        """
        self.max_allowed_size = static_buffer_size

    def validate_input_boundary(self, raw_input_bytes):
        """Megvizsgálja, hogy a beérkező adat biztonságosan elfér-e a pufferben."""
        input_length = len(raw_input_bytes)
        
        if input_length > self.max_allowed_size:
            print(f"  [🚨 OVERFLOW DETECTED] Input size boundaries breached!")
            print(f"    [-] Allocated Buffer Static Size : {self.max_allowed_size} bytes")
            print(f"    [-] Inbound Payload Actual Size  : {input_length} bytes")
            print(f"    [!] Overflow Delta Overhead      : {input_length - self.max_allowed_size} bytes")
            return False
        return True

    def process_secure_allocation(self, payload):
        """Biztonságos memóriakezelési szimuláció."""
        # Átalakítás bájtokká az alacsony szintű méréshez
        raw_bytes = str(payload).encode('utf-8')
        
        if not self.validate_input_boundary(raw_bytes):
            print("  [❌ MITIGATION] Input payload truncated. Memory pointer isolation engaged.")
            return raw_bytes[:self.max_allowed_size] # Kényszerített csonkolás a biztonságért
            
        print("  [🟢 COMPLIANT] Payload copied to allocated memory space safely.")
        return raw_bytes

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD KERNEL SEC -> BUFFER OVERFLOW SHIELD     ")
    print("=========================================================")
    
    # 512 bájtos szigorított puffer lefoglalása a teszthez
    shield = BufferOverflowShield(static_buffer_size=512)
    
    # 1. Teszt eset: Legitim, biztonságos méretű parancscsomag
    legit_packet = "ACTION=PROCESS_DATA;NODE_ID=84;TELEMETRY=ACTIVE"
    print(f"[*] Ingesting Legitimate Packet (Size: {len(legit_packet)} chars)...")
    shield.process_secure_allocation(legit_packet)
    
    print("-" * 57)
    
    # 2. Teszt eset: Rosszindulatú, túlméretezett exploit payload (A karakterekkel feltöltve)
    malicious_exploit = "A" * 600 + "\x90\x90\x90\xEB\x04"  # 600 bájt + szimulált shellcode nop sled
    print(f"[!] Ingesting Suspected Remote Code Execution (RCE) Exploitation Payload...")
    shield.process_secure_allocation(malicious_exploit)
    
    print("=========================================================")
