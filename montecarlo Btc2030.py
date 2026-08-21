import matplotlib.pyplot as plt
import numpy as np

# --- Szimulációs Paraméterek ---
S0 = 60000.0  # Kezdő BTC árfolyam ($)
mu = 0.25  # Várható éves növekedési ütem (25% drift)
sigma = 0.55  # Évesített volatilitás (55%)

years = 4.5  # Időtáv 2030 végéig
n_steps = int(years * 365)  # Napi lépések száma (~1642 nap)
dt = years / n_steps
n_simulations = 500  # Szimulált pályák száma

# --- Geometriai Brown-mozgás (GBM) Számítás ---
np.random.seed(42)  # Reprodukálhatóság
shock = np.random.normal(0, np.sqrt(dt), size=(n_steps, n_simulations))
drift_term = (mu - 0.5 * sigma**2) * dt
log_returns = drift_term + sigma * shock

# Kumulatív szorzat az árfolyampályákhoz
price_paths = np.zeros((n_steps + 1, n_simulations))
price_paths[0] = S0
price_paths[1:] = S0 * np.exp(np.cumsum(log_returns, axis=0))

# --- Statisztikai sávok kinyerése ---
time_axis = np.linspace(2026.5, 2030.0, n_steps + 1)
median_path = np.median(price_paths, axis=1)
p10_path = np.percentile(price_paths, 10, axis=1)  # Medve forgatókönyv
p90_path = np.percentile(price_paths, 90, axis=1)  # Bika forgatókönyv

# --- Matplotlib Vizualizáció ---
plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(12, 6), dpi=100)

# Egyedi szimulációs pályák halvány kirajzolása
ax.plot(time_axis, price_paths, color="#00ffcc", alpha=0.03, linewidth=1)

# Statisztikai vonalak és sávok
ax.plot(
    time_axis,
    median_path,
    color="#ffcc00",
    linewidth=2.5,
    label=f"Medián Várakozás (2030: ${median_path[-1]:,.0f})",
)
ax.plot(
    time_axis,
    p90_path,
    color="#00ff88",
    linestyle="--",
    linewidth=1.8,
    label=f"90. Percentilis / Bika (2030: ${p90_path[-1]:,.0f})",
)
ax.plot(
    time_axis,
    p10_path,
    color="#ff3366",
    linestyle="--",
    linewidth=1.8,
    label=f"10. Percentilis / Medve (2030: ${p10_path[-1]:,.0f})",
)

# Konfidencia sáv kitöltése
ax.fill_between(
    time_axis,
    p10_path,
    p90_path,
    color="#00ffcc",
    alpha=0.08,
    label="80% Valószínűségi Sáv",
)

# Formázás és skálázás
ax.set_yscale("log")
ax.set_title(
    "BTC/USD Monte Carlo Szimuláció (2026 – 2030)",
    fontsize=14,
    fontweight="bold",
    color="#ffffff",
)
ax.set_xlabel("Év", fontsize=11, color="#aaaaaa")
ax.set_ylabel("Árfolyam USD (Logaritmikus skála)", fontsize=11, color="#aaaaaa")
ax.grid(True, which="both", linestyle=":", alpha=0.3, color="#555555")
ax.legend(loc="upper left", framealpha=0.8, facecolor="#1e1e1e")

plt.tight_layout()
plt.show()
