"""
BIT 2118 - Scientific Computing
Task 10: Bisection and Fixed-Point Methods
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

from scipy.optimize import root_scalar

def main():
    f = lambda T: T - 25.0 - 10.0 * np.exp(-T / 20.0)
    g = lambda T: 25.0 + 10.0 * np.exp(-T / 20.0)

    bisect_res = root_scalar(f, bracket=[20.0, 40.0], method="bisect", xtol=1e-10)
    t_fp = 30.0
    fp_iters = 0
    for _ in range(100):
        t_next = g(t_fp)
        fp_iters += 1
        if abs(t_next - t_fp) < 1e-10:
            t_fp = t_next
            break
        t_fp = t_next

    # Parameter sensitivity: heat gain amplitude 10 -> 20
    f_mod = lambda T: T - 25.0 - 20.0 * np.exp(-T / 20.0)
    g_mod = lambda T: 25.0 + 20.0 * np.exp(-T / 20.0)
    bisect_mod = root_scalar(f_mod, bracket=[20.0, 40.0], method="bisect", xtol=1e-10)
    t_fp_mod = 30.0
    fp_iters_mod = 0
    for _ in range(100):
        t_next = g_mod(t_fp_mod)
        fp_iters_mod += 1
        if abs(t_next - t_fp_mod) < 1e-10:
            t_fp_mod = t_next
            break
        t_fp_mod = t_next

    # Real-world case: CSTR steady-state concentration
    f_cstr = lambda C: C - 50.0 + 18.0 * (1.0 - np.exp(-0.05 * C))
    g_cstr = lambda C: 50.0 - 18.0 * (1.0 - np.exp(-0.05 * C))
    cstr_bisect = root_scalar(f_cstr, bracket=[25.0, 50.0], method="bisect", xtol=1e-10)
    c_val = 40.0
    for _ in range(100):
        c_next = g_cstr(c_val)
        if abs(c_next - c_val) < 1e-10:
            c_val = c_next
            break
        c_val = c_next

    lines = [
        "TASK 10: BISECTION AND FIXED-POINT METHODS",
        f"Bisection T*: {bisect_res.root:.6f} C ({bisect_res.iterations} iters)",
        f"Fixed-Point T*: {t_fp:.6f} C ({fp_iters} iters)",
        f"Modified (amp=20) Bisection T*: {bisect_mod.root:.6f} C | Fixed-Point T*: {t_fp_mod:.6f} C ({fp_iters_mod} iters)",
        "",
        "REAL-WORLD CASE: CSTR STEADY-STATE CONCENTRATION",
        f"Steady-state concentration C*: {cstr_bisect.root:.6f} mol/m^3",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_10_results.txt").write_text(report, encoding="utf-8")

    t_grid = np.linspace(20.0, 40.0, 300)
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(t_grid, f(t_grid), label="f(T) [amp=10]")
    ax.plot(t_grid, f_mod(t_grid), "--", label="f_mod(T) [amp=20]")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.axvline(bisect_res.root, linestyle=":", label=f"Root T*={bisect_res.root:.2f} C")
    ax.set(title="Thermal Equilibrium Root Finding", xlabel="Temperature T (C)", ylabel="f(T)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_10_bisection_fixed_point.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
