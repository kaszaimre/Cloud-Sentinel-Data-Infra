import numpy as np


def calculate_position_size(
    account_balance, risk_percentage, entry_price, atr_value, atr_multiplier=2.0
):
    """Kiszámolja a tűpontos pozícióméretet és a Stop Loss szintet a volatilitás (ATR) alapján.

    Paraméterek:
    - account_balance: A teljes tőkeszámlád mérete (USD)
    - risk_percentage: Mekkora részét kockáztatod a tőkének egy ügyleten (pl.
    1.0 = 1%)
    - entry_price: A belépési ár (ahol megveszed az eszközt)
    - atr_value: Az eszköz aktuális ATR értéke (volatilitás)
    - atr_multiplier: Hányszorosa legyen az ATR a Stop Loss-nak (ajánlott: 1.5
    - 2.5)
    """
    # 1. Kiszámoljuk a maximális dolláros kockázatot ügyletenként
    maximum_risk_usd = account_balance * (risk_percentage / 100.0)

    # 2. Meghatározzuk a Stop Loss távolságát a volatilitás alapján
    stop_loss_distance = atr_value * atr_multiplier

    # 3. Kiszámoljuk a pontos Stop Loss árat (Long pozíció esetén)
    stop_loss_price = entry_price - stop_loss_distance

    # 4. Kiszámoljuk, hány darab egységet/részvényt szabad venni
    if stop_loss_distance > 0:
        position_size = maximum_risk_usd / stop_loss_distance
    else:
        position_size = 0

    # 5. Teljes pozíció értéke dollárban
    total_position_value = position_size * entry_price

    return {
        "Max Kockázat (USD)": round(maximum_risk_usd, 2),
        "Stop Loss Szint (Ár)": round(stop_loss_price, 4),
        "Megvásárolható Mennyiség (Darab/Coin)": round(position_size, 4),
        "Pozíció Teljes Értéke (USD)": round(total_position_value, 2),
    }


# --- ÉLES TESZT PÉLDA (Pl. Bitcoin vagy egy NASDAQ részvény) ---
szamla_toke = 100000  # $100,000 tőke
kockazat_szazalek = 1.0  # Szigorú 1% kockázat ($1,000)
belepesi_ar = 64150.0  # Aktuális BTC vagy részvény ár
aktualis_atr = 1250.0  # A piac jelenlegi volatilitása (ATR)

eredmeny = calculate_position_size(
    szamla_toke, kockazat_szazalek, belepesi_ar, aktualis_atr, atr_multiplier=2.0
)

# Eredmények kiíratása
print("=== T800 KOCKÁZATKEZELŐ MODUL ERŐSÍTÉS ===")
for kulcs, ertek in eredmeny.items():
    print(f"{kulcs}: {ertek}")
