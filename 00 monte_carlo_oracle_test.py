import numpy as np
import matplotlib.pyplot as plt

def run_monte_carlo_oracle_test(
    initial_price=60000.0,
    mu=0.0002,          # Napi drift (várható hozam)
    sigma=0.02,         # Napi volatilitás
    n_days=100,         # Hány lépést szimuláljon
    n_sims=1000         # Pályák száma
):
    dt = 1
    # 1. Geometriai Brown-mozgás mátrix (n_days x n_sims)
    random_shocks = np.random.normal(0, np.sqrt(dt), size=(n_days, n_sims))
    price_paths = np.zeros((n_days, n_sims))
    price_paths[0] = initial_price

    for t in range(1, n_days):
        # GBM képlet: S(t) = S(t-1) * exp((mu - 0.5 * sigma^2)*dt + sigma * shock)
        price_paths[t] = price_paths[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * random_shocks[t])

    # 2. Szimulált Stratégia / Belépési logika (Példa: Momentum + Mean Reversion teszt)
    # Ha az árfolyam az elmúlt 5 nap mélypontjára esik -> VÉTEL
    total_returns = []
    
    for sim in range(n_sims):
        path = price_paths[:, sim]
        pnl = 0.0
        position = 0
        entry_price = 0.0

        for t in range(5, n_days):
            rolling_min = np.min(path[t-5:t])
            rolling_max = np.max(path[t-5:t])

            # Belépési logika tesztelése véletlen zajon
            if position == 0 and path[t] <= rolling_min:
                position = 1
                entry_price = path[t]
            elif position == 1 and path[t] >= rolling_max:
                pnl += (path[t] - entry_price) / entry_price
                position = 0

        total_returns.append(pnl * 100)

    # 3. Kiértékelés & Megjelenítés
    total_returns = np.array(total_returns)
    win_rate = np.mean(total_returns > 0) * 100
    avg_pnl = np.mean(total_returns)

    print("=== MONTE CARLO RANDOM WALK TESZT EREDMÉNYEK ===")
    print(f"Szimulált pályák: {n_sims}")
    print(f"Véletlen zajon elért nyerési arány: {win_rate:.2f}%")
    print(f"Átlagos PnL véletlen pályán: {avg_pnl:.2f}%")

    # Grafikon
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(price_paths[:, :20], alpha=0.6)  # Első 20 pálya
    plt.title("20 Random Walk Árpálya")
    plt.xlabel("Lépések (Napok)")
    plt.ylabel("Árfolyam")

    plt.subplot(1, 2, 2)
    plt.hist(total_returns, bins=30, color='skyblue', edgecolor='black')
    plt.axvline(0, color='red', linestyle='--')
    plt.title("Stratégia Hoza-eloszlása Zajon")
    plt.xlabel("PnL (%)")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_monte_carlo_oracle_test()
