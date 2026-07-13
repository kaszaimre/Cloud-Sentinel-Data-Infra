import time
import random

class MasterPhoenixCore:
    """
    =====================================================================
    00A1 MÁSTER PHOENIX - KIBER-FÚZIÓS PARANCSNOKI MAG v7.0
    =====================================================================
    Don Tábornok saját fejlesztésű kereskedelmi és diktálási rendszere.
    """
    def __init__(self):
        self.system_status = "CONNECTED"
        self.test_balance_usdt = 551194.53
        self.current_btc_price = 62834.69
        self.trigger_threshold = 19  # A képernyőn látható 19%-os határ
        
    def process_voice_dictation(self, audio_text: str):
        """A jobb oldali Voice Rec modulból érkező szövegek feldolgozása"""
        print(f"🎙️ [Master Phoenix Voice] Beérkező hangparancs: '{audio_text}'")
        if "long" in audio_text.lower() or "belépés" in audio_text.lower():
            return "TRIGGER_LONG"
        elif "stop" in audio_text.lower() or "zárás" in audio_text.lower():
            return "TRIGGER_CLOSE_ALL"
        return "WAITING_FOR_COMMAND"

    def check_fusion_triggers(self, current_long_pct, current_short_pct):
        """
        Kiber-fúziós trigger információk kiértékelése.
        Ha a trend és a százalékos értékek elérik a kritikus szintet, aktivál.
        """
        print(f"⚡ [Trigger Check] Aktuális szintek -> LONG: {current_long_pct}%, SHORT: {current_short_pct}%")
        
        # A képernyőképed alapján: LONG 19% (NEM AKTÍV), SHORT 19% (AKTÍV)
        if current_short_pct >= self.trigger_threshold and current_long_pct <= 20:
            return "SHORT_JEL_AKTIV"
        elif current_long_pct > 50:
            return "LONG_JEL_AKTIV"
        
        return "MÁTRIX_STABIL_HOLD"

    def execute_terminal_trade(self, asset: str, direction: str, size_usd: float = 5000):
        """Alul futó bot és demo pozíciók indítása (pl. EOG, BAC, XVG)"""
        if self.system_status != "CONNECTED":
            return "❌ Binance API Leválasztva!"
            
        position_id = f"PHX-{random.randint(1000, 9999)}"
        print(f"📥 [Binance API Terminal] Pozíció megnyitva! ID: {position_id}")
        print(f"   - Eszköz: {asset} | Irány: {direction} | Méret: ${size_usd} | Ár: {self.current_btc_price:,} USD")
        return position_id

# --- KIBER-RENDSZER INDÍTÁSA ---
if __name__ == "__main__":
    phoenix = MasterPhoenixCore()
    print(f"🦾 [Master Phoenix] Rendszer felállt. Státusz: {phoenix.system_status} | Keret: ${phoenix.test_balance_usdt:,}")
    
    # 1. Hangalapú parancs szimulálása
    action = phoenix.process_voice_dictation("Azonnali Long belépés a bázison!")
    
    # 2. Trigger ellenőrzés a képed adatai alapján (Trend: -58)
    status = phoenix.check_fusion_triggers(current_long_pct=19, current_short_pct=19)
    print(f"📊 Fúziós Állapot: {status}")
    
    # 3. Új pozíció rögzítése a futó bot listába
    phoenix.execute_terminal_trade("BTCUSD/USDT", "LONG", size_usd=5000)
    print("\nA Master Phoenix mag stabilan ketyeg, fasa és kész! 🚀")
