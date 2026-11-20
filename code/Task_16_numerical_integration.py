"""
BIT 2118 - Scientific Computing
Task 16: Numerical Integration
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

from scipy.integrate import simpson

def main():
    time_h = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
    power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9], dtype=float)

    trap_orig = float(np.trapz(power_kw, x=time_h))
    simp_orig = float(simpson(power_kw, x=time_h))

    changed_power = power_kw.copy()
    changed_power[3] = 2.2
    trap_mod = float(np.trapz(changed_power, x=time_h))
    simp_mod = float(simpson(changed_power, x=time_h))

    flow_t_h = np.array([0, 4, 8, 12, 16, 20, 24], dtype=float)
    flow_l_min = np.array([2.0, 2.4, 2.8, 3.1, 2.7, 2.2, 1.8], dtype=float)
    flow_l_h = flow_l_min * 60.0
    vol_trap = float(np.trapz(flow_l_h, x=flow_t_h))
    vol_simp = float(simpson(flow_l_h, x=flow_t_h))

    lines = [
        "TASK 16: NUMERICAL INTEGRATION",
        f"Original Energy -> Trapezoidal: {trap_orig:.3f} kWh | Simpson: {simp_orig:.3f} kWh",
        f"Modified (6h -> 2.2 kW) -> Trapezoidal: {trap_mod:.3f} kWh | Simpson: {simp_mod:.3f} kWh",
        f"Daily Water Volume -> Trapezoidal: {vol_trap:.1f} L | Simpson: {vol_simp:.1f} L",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_16_results.txt").write_text(report, encoding="utf-8")

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.plot(time_h, power_kw, "o-", label="Original Power (kW)")
    ax.plot(time_h, changed_power, "s--", label="Modified 6h Power (2.2 kW)")
    ax.fill_between(time_h, power_kw, alpha=0.2, label="Energy Area")
    ax.set(title="Smart-Meter Power Curve & Energy Integration", xlabel="Time (hours)", ylabel="Power (kW)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_16_numerical_integration.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
