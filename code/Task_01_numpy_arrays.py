"""
BIT 2118 - Scientific Computing
Task 01: NumPy Arrays and Numerical Computation
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

def main():
    temperatures_c = np.array([
        18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8,
        25.6, 27.1, 28.3, 29.0, 29.4, 29.1, 28.5, 27.6,
        26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0
    ], dtype=float)

    mean_c = np.mean(temperatures_c)
    min_c = np.min(temperatures_c)
    max_c = np.max(temperatures_c)
    temperatures_f = 1.8 * temperatures_c + 32.0

    # Sensitivity test: peak reading at index 12 changed from 29.4 C to 35.0 C
    mod_temps_c = temperatures_c.copy()
    mod_temps_c[12] = 35.0
    mod_mean_c = np.mean(mod_temps_c)
    mod_max_c = np.max(mod_temps_c)

    # Real-world case: Smart Grid Energy & CO2 Emissions (0.45 kg CO2 / kWh)
    energy_kwh = np.array([
        1.2, 1.0, 0.9, 0.8, 0.9, 1.5,
        3.2, 4.5, 4.1, 3.8, 3.6, 3.5,
        3.7, 3.9, 4.0, 4.2, 4.8, 5.2,
        5.0, 4.3, 3.5, 2.8, 2.0, 1.5
    ], dtype=float)
    co2_kg = energy_kwh * 0.45

    lines = [
        "TASK 01: NUMPY ARRAYS AND NUMERICAL COMPUTATION",
        f"Mean Temperature (C): {mean_c:.2f} C ({1.8*mean_c+32:.2f} F)",
        f"Min Temperature (C):  {min_c:.2f} C ({1.8*min_c+32:.2f} F)",
        f"Max Temperature (C):  {max_c:.2f} C ({1.8*max_c+32:.2f} F)",
        f"First 6 Fahrenheit values: {np.round(temperatures_f[:6], 2)}",
        "",
        "SENSITIVITY ANALYSIS (Index 12: 29.4 C -> 35.0 C)",
        f"Modified Mean (C): {mod_mean_c:.2f} C | Modified Max (C): {mod_max_c:.2f} C ({1.8*mod_max_c+32:.2f} F)",
        "",
        "REAL-WORLD CASE: SMART GRID ENERGY & EMISSIONS",
        f"Mean Hourly Energy: {np.mean(energy_kwh):.2f} kWh | Min: {np.min(energy_kwh):.2f} kWh | Max: {np.max(energy_kwh):.2f} kWh",
        f"Total Daily Energy: {np.sum(energy_kwh):.2f} kWh | Total CO2: {np.sum(co2_kg):.2f} kg",
        f"First 6 CO2 readings (kg): {np.round(co2_kg[:6], 3)}",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_01_results.txt").write_text(report, encoding="utf-8")

    fig, axes = plt.subplots(2, 1, figsize=(9, 6.5))
    hours = np.arange(24)
    axes[0].plot(hours, temperatures_c, "o-", label="Original Temp (C)")
    axes[0].plot(hours, mod_temps_c, "s--", label="Modified Peak (35.0 C)")
    axes[0].set(title="24-Hour Temperature Profile", xlabel="Hour", ylabel="Temperature (C)")
    axes[0].grid(True)
    axes[0].legend()

    axes[1].bar(hours, co2_kg, label="CO2 Emissions (kg)")
    axes[1].set(title="Hourly Grid CO2 Emissions", xlabel="Hour", ylabel="CO2 (kg)")
    axes[1].grid(True)
    axes[1].legend()

    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_01_numpy_arrays.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
