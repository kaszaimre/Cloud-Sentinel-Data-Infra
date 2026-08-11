import numpy as np


def check_execution_safety(
    ask_price, bid_price, target_size_usd, orderbook_depth_asks, config
):
    """Ellenőrzi, hogy a piaci spread és az orderbook mélysége biztonságos-e a
    belépéshez.

    Paraméterek:
    - ask_price: Az aktuális eladási ár (Long belépési szint)
    - bid_price: Az aktuális vételi ár
    - target_size_usd: A pozíció tervezett mérete dollárban (pl. 5000)
    - orderbook_depth_asks: Lista a legközelebbi ask szintekről és likviditásról
    [(ár, volumen), ...]
    - config: Beállítások (max_spread_pct, max_estimated_slippage_pct)
    """
    # 1. Spread százalékos kiszámítása és ellenőrzése
    current_spread = ask_price - bid_price
    spread_percentage = (current_spread / ask_price) * 100.0

    if spread_percentage > config["max_spread_pct"]:
        return {
            "status": "REJECTED",
            "reason": f"Túl tág spread: {round(spread_percentage, 3)}% (Limit: {config['max_spread_pct']}%).",
        }

    # 2. Árcsúszás (Slippage) becslése az orderbook likviditás alapján
    required_units = target_size_usd / ask_price
    accumulated_units = 0
    total_cost = 0

    for price, volume in orderbook_depth_asks:
        units_from_level = min(volume, required_units - accumulated_units)
        total_cost += units_from_level * price
        accumulated_units += units_from_level
        if accumulated_units >= required_units:
            break

    if accumulated_units < required_units:
        return {
            "status": "REJECTED",
            "reason": "Elégtelen likviditás az orderbookban a kért mérethez.",
        }

    average_execution_price = total_cost / required_units
    estimated_slippage_pct = (
        (average_execution_price - ask_price) / ask_price
    ) * 100.0

    if estimated_slippage_pct > config["max_estimated_slippage_pct"]:
        return {
            "status": "REJECTED",
            "reason": f"Magas becsült árcsúszás: {round(estimated_slippage_pct, 3)}% (Limit: {config['max_estimated_slippage_pct']}%).",
        }

    return {
        "status": "APPROVED",
        "spread_pct": round(spread_percentage, 3),
        "estimated_slippage_pct": round(estimated_slippage_pct, 3),
        "avg_execution_price": round(average_execution_price, 4),
    }


# --- INFRA KONFIGURÁCIÓ ---
guard_config = {
    "max_spread_pct": 0.15,  # Maximum 0.15%-os spread engedélyezett
    "max_estimated_slippage_pct": 0.08,  # Maximum 0.08%-os árcsúszás
}

# Példa: $5000-os pakkot akarunk dobni, de az orderbook vékony
kamu_orderbook_asks = [
    (64151.0, 0.02),
    (64153.0, 0.03),
    (64158.0, 0.05),  # Az ár csúszik felfelé, ahogy faljuk a likviditást
]

visszajelzes = check_execution_safety(
    ask_price=64150.0,
    bid_price=64130.0,
    target_size_usd=5000.0,
    orderbook_depth_asks=kamu_orderbook_asks,
    config=guard_config,
)

print("=== T800 EXECUTION GUARD MODULE ===")
for k, v in visszajelzes.items():
    print(f"{k}: {v}")
