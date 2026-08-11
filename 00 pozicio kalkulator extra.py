import numpy as np


def manage_active_position(
    current_price,
    highest_price_since_entry,
    entry_candle_index,
    current_candle_index,
    atr_value,
    config,
):
    """Menedzseli a futó pozíciót: kezeli a követő stopot és az időalapú kényszerített zárást.

    Paraméterek:
    - current_price: Az eszköz aktuális élő ára
    - highest_price_since_entry: A legmagasabb elért ár a belépés óta (Long
    esetén)
    - entry_candle_index: A gyertya indexe, ahol a bot belépett
    - current_candle_index: Az aktuális gyertya indexe
    - atr_value: Az aktuális ATR érték a csúszó stophoz
    - config: Beállítási szótár (trailing_multiplier, max_candle_hold)
    """
    # 1. Időalapú zárás ellenőrzése (Time-Based Exit)
    candles_held = current_candle_index - entry_candle_index
    if candles_held >= config["max_candle_hold"]:
        return {
            "action": "CLOSE",
            "reason": f"Időalapú zárás: A pozíció elérte a {config['max_candle_hold']} gyertyás limitet.",
        }

    # 2. Dinamikus Követő Stop (Trailing Stop) kiszámítása a legmagasabb pontból
    # Ahogy az ár megy fel, a stop szint is emelkedik, de soha nem csökkenhet!
    trailing_stop_distance = atr_value * config["trailing_multiplier"]
    dynamic_trailing_stop = highest_price_since_entry - trailing_stop_distance

    # 3. Kiszámoljuk, hogy az aktuális ár áttörte-e a követő stopot
    if current_price <= dynamic_trailing_stop:
        return {
            "action": "CLOSE",
            "reason": f"Követő Stop kiütve: Az ár ({current_price}) elérte a dinamikus védelmi szintet ({round(dynamic_trailing_stop, 4)}).",
        }

    return {
        "action": "HOLD",
        "current_trailing_stop": round(dynamic_trailing_stop, 4),
        "candles_remaining": config["max_candle_hold"] - candles_held,
    }


# --- ÉLES INFRA TESZT ---
rendszer_config = {
    "trailing_multiplier": 1.5,  # Az ATR hányszorosa kövesse az árat
    "max_candle_hold": 12,  # Maximum 12 gyertyáig maradhat bent a pozíció
}

# Példa: Beléptünk 64,150-en, az ár felment 66,000-ig, de most visszanyalt 64,200-ra
allapot = manage_active_position(
    current_price=64200.0,
    highest_price_since_entry=66000.0,
    entry_candle_index=100,
    current_candle_index=105,  # 5 gyertya telt el
    atr_value=1100.0,
    config=rendszer_config,
)

print("=== T800 POZÍCIÓ MENEDZSER MODUL ===")
for k, v in allapot.items():
    print(f"{k}: {v}")
