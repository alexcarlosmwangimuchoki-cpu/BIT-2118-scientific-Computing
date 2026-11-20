"""
BIT 2118 - Scientific Computing
Task 19: Optimization (Logistics Fleet Allocation)
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

from scipy.optimize import minimize

def main():
    cost = lambda z: 150.0 * z[0] + 250.0 * z[1]
    cons = {"type": "ineq", "fun": lambda z: 200.0 * z[0] + 400.0 * z[1] - 1500.0}
    bounds = [(0, None), (0, None)]

    sol = minimize(cost, x0=[5.0, 5.0], method="SLSQP", bounds=bounds, constraints=cons)
    x_opt, y_opt = sol.x

    best_int = None
    for a in range(0, 15):
        for b in range(0, 15):
            cap = 200 * a + 400 * b
            if cap >= 1500:
                tot_cost = 150 * a + 250 * b
                if best_int is None or tot_cost < best_int[0]:
                    best_int = (tot_cost, a, b, cap)

    lines = [
        "TASK 19: OPTIMIZATION (LOGISTICS FLEET ALLOCATION)",
        f"Continuous optimum -> Type A: {x_opt:.3f}, Type B: {y_opt:.3f}, Cost: ${sol.fun:.2f}",
        f"Integer optimum -> Type A: {best_int[1]}, Type B: {best_int[2]}, Capacity: {best_int[3]} boxes, Cost: ${best_int[0]}",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_19_results.txt").write_text(report, encoding="utf-8")

    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.bar(["Continuous (SLSQP)", "Integer Fleet"], [sol.fun, best_int[0]])
    ax.set(title="Fleet Dispatch Cost Comparison", ylabel="Cost ($)")
    ax.grid(True, axis="y")
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_19_optimization_cost.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
