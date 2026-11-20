"""
BIT 2118 - Scientific Computing
Task 12: Polynomial and Nonlinear Equation Solving
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

from scipy.optimize import root

def equations(z):
    x, y = z
    return [x**2 + y**2 - 4.0, y - (x**2 - 1.0)]

def vehicle_boundary(z):
    x, y = z
    return [x**2 + y**2 - 9.0, y - (x**2 - 1.0)]

def main():
    sol_pos = root(equations, [1.0, 1.0])
    sol_neg = root(equations, [-1.0, 1.0])

    v_pos = root(vehicle_boundary, [1.5, 1.5])
    v_neg = root(vehicle_boundary, [-1.5, 1.5])

    lines = [
        "TASK 12: POLYNOMIAL AND NONLINEAR EQUATION SOLVING",
        f"Guess [1, 1] -> Intersection: {np.round(sol_pos.x, 6)} | Success: {sol_pos.success}",
        f"Guess [-1, 1] -> Intersection: {np.round(sol_neg.x, 6)} | Success: {sol_neg.success}",
        "",
        "REAL-WORLD CASE: VEHICLE PATH & CIRCULAR BOUNDARY (r=3)",
        f"Guess [1.5, 1.5] -> Crossing: {np.round(v_pos.x, 6)} | Success: {v_pos.success}",
        f"Guess [-1.5, 1.5] -> Crossing: {np.round(v_neg.x, 6)} | Success: {v_neg.success}",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_12_results.txt").write_text(report, encoding="utf-8")

    theta = np.linspace(0, 2 * np.pi, 300)
    x_par = np.linspace(-2.2, 2.2, 300)
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.plot(2 * np.cos(theta), 2 * np.sin(theta), label="Circle: x^2 + y^2 = 4")
    ax.plot(x_par, x_par**2 - 1.0, label="Parabola: y = x^2 - 1")
    ax.scatter([sol_pos.x[0], sol_neg.x[0]], [sol_pos.x[1], sol_neg.x[1]], zorder=4, label="Intersections")
    ax.set_aspect("equal")
    ax.set(title="Nonlinear System Intersection", xlabel="x", ylabel="y")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_12_nonlinear_system.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
