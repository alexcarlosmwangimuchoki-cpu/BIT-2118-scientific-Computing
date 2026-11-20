"""
BIT 2118 - Scientific Computing
Task 06: Solution of Systems of Linear Equations (Ax = b)
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
    A = np.array([[4.0, 2.0], [8.0, 12.0]], dtype=float)
    b = np.array([20.0, 72.0], dtype=float)
    x = np.linalg.solve(A, b)
    res_norm = float(np.linalg.norm(b - A @ x))

    b_mod = np.array([20.0, 96.0], dtype=float)
    x_mod = np.linalg.solve(A, b_mod)
    res_mod_norm = float(np.linalg.norm(b_mod - A @ x_mod))

    # Real-world case: 3-Plant Grid Allocation
    A_grid = np.array([
        [0.5, 0.2, 0.1],
        [0.1, 0.6, 0.3],
        [0.2, 0.1, 0.8],
    ], dtype=float)
    b_demand = np.array([140.0, 210.0, 310.0], dtype=float)
    dispatch = np.linalg.solve(A_grid, b_demand)
    grid_res = float(np.linalg.norm(b_demand - A_grid @ dispatch))

    lines = [
        "TASK 06: LINEAR SYSTEMS (Ax = b)",
        f"Original solution (Type A, Type B): {np.round(x, 4)} | Residual norm: {res_norm:.2e}",
        f"Modified b=[20, 96] solution: {np.round(x_mod, 4)} | Residual norm: {res_mod_norm:.2e}",
        "",
        "REAL-WORLD CASE: 3-PLANT GRID DISPATCH",
        f"Plant A: {dispatch[0]:.2f}, Plant B: {dispatch[1]:.2f}, Plant C: {dispatch[2]:.2f}",
        f"Verification residual norm: {grid_res:.2e}",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_06_results.txt").write_text(report, encoding="utf-8")

    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    labels = ["Original (b=[20,72])", "Modified (b=[20,96])"]
    type_a = [x[0], x_mod[0]]
    type_b = [x[1], x_mod[1]]
    idx = np.arange(len(labels))
    w = 0.35
    ax.bar(idx - w/2, type_a, w, label="Server Type A")
    ax.bar(idx + w/2, type_b, w, label="Server Type B")
    ax.set_xticks(idx)
    ax.set_xticklabels(labels)
    ax.set(title="Server Allocation Sensitivity to Memory Load", ylabel="Server Units")
    ax.grid(True, axis="y")
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_06_linear_systems.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
