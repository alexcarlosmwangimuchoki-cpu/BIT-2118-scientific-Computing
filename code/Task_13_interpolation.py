"""
BIT 2118 - Scientific Computing
Task 13: Numerical Interpolation
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

from scipy.interpolate import interp1d, CubicSpline

def main():
    hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
    temp = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.5], dtype=float)

    linear = interp1d(hours, temp, kind="linear")
    cubic = CubicSpline(hours, temp)

    t1, t2 = 10.5, 10.25
    l1, c1 = float(linear(t1)), float(cubic(t1))
    l2, c2 = float(linear(t2)), float(cubic(t2))

    gh_temp = np.array([21.0, 21.8, 23.1, 24.6, 26.2, 27.0, 27.4], dtype=float)
    gh_linear = interp1d(hours, gh_temp, kind="linear")
    gh_cubic = CubicSpline(hours, gh_temp)
    gh_l, gh_c = float(gh_linear(t1)), float(gh_cubic(t1))

    lines = [
        "TASK 13: NUMERICAL INTERPOLATION",
        f"At 10:30 (10.5): Linear = {l1:.3f} C | Cubic = {c1:.3f} C",
        f"At 10:15 (10.25): Linear = {l2:.3f} C | Cubic = {c2:.3f} C",
        f"Change (10:30 -> 10:15): Linear {l2-l1:+.3f} C | Cubic {c2-c1:+.3f} C",
        "",
        "REAL-WORLD CASE: GREENHOUSE SENSOR (10:30)",
        f"Linear = {gh_l:.3f} C | Cubic = {gh_c:.3f} C",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_13_results.txt").write_text(report, encoding="utf-8")

    x_grid = np.linspace(8, 14, 300)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.scatter(hours, temp, label="Measurements", zorder=3)
    ax.plot(x_grid, linear(x_grid), "--", label="Linear Interpolation")
    ax.plot(x_grid, cubic(x_grid), label="Cubic Spline")
    ax.scatter([t1], [l1], marker="o", label=f"Linear 10:30 ({l1:.2f} C)")
    ax.scatter([t1], [c1], marker="x", label=f"Cubic 10:30 ({c1:.2f} C)")
    ax.set(title="Weather Station Temperature Interpolation", xlabel="Hour", ylabel="Temperature (C)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_13_interpolation.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
