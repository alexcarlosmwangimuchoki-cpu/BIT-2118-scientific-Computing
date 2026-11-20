"""
BIT 2118 - Scientific Computing
Task 20: Monte Carlo Simulation (Project Budget Overrun Risk)
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
    rng = np.random.default_rng(42)
    total_budget = 180000.0
    N = 100_000

    p1 = rng.normal(50000.0, 5000.0, N)
    p2 = rng.normal(80000.0, 10000.0, N)
    p3 = rng.normal(40000.0, 8000.0, N)
    total_cost = p1 + p2 + p3

    over_budget = total_cost > total_budget
    overrun_prob = float(np.mean(over_budget))
    overrun_count = int(np.sum(over_budget))

    running_prob = np.cumsum(over_budget) / np.arange(1, N + 1)
    indices = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1

    lines = [
        "TASK 20: MONTE CARLO SIMULATION (BUDGET OVERRUN RISK)",
        f"Estimated probability of budget overrun: {overrun_prob:.4%}",
        f"Overrun cases: {overrun_count} out of {N}",
        f"Mean total cost: ${np.mean(total_cost):,.2f} | Std dev: ${np.std(total_cost):,.2f}",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_20_results.txt").write_text(report, encoding="utf-8")

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.semilogx(indices + 1, running_prob[indices], label="Running Overrun Probability")
    ax.axhline(overrun_prob, linestyle="--", label=f"Converged ({overrun_prob:.2%})")
    ax.set(title="Monte Carlo Convergence of Budget Overrun Risk", xlabel="Number of Simulations", ylabel="Estimated Overrun Probability")
    ax.grid(True, which="both")
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_20_monte_carlo_convergence.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
