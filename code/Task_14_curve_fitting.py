"""
BIT 2118 - Scientific Computing
Task 14: Curve Fitting and Approximation
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

from scipy.optimize import curve_fit

def quad_model(x, a, b, c):
    return a * x**2 + b * x + c

def main():
    users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
    response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

    popt, _ = curve_fit(quad_model, users, response_ms)
    a, b, c = popt
    pred = quad_model(users, a, b, c)
    rmse = float(np.sqrt(np.mean((response_ms - pred) ** 2)))
    pred_400 = float(quad_model(400.0, a, b, c))
    pred_450 = float(quad_model(450.0, a, b, c))

    # Real-world case: Supermarket queue waiting time
    customers = np.array([10, 20, 30, 40, 50, 60, 70], dtype=float)
    wait_s = np.array([12, 15, 21, 31, 45, 63, 85], dtype=float)
    q_popt, _ = curve_fit(quad_model, customers, wait_s)
    qa, qb, qc = q_popt
    q_rmse = float(np.sqrt(np.mean((wait_s - quad_model(customers, qa, qb, qc)) ** 2)))
    q_pred_80 = float(quad_model(80.0, qa, qb, qc))

    lines = [
        "TASK 14: CURVE FITTING AND APPROXIMATION",
        f"Server fit: y = {a:.8f}x^2 + {b:.6f}x + {c:.4f} | RMSE = {rmse:.2f} ms",
        f"Predicted response at 400 users: {pred_400:.2f} ms | 450 users: {pred_450:.2f} ms",
        "",
        "REAL-WORLD CASE: SUPERMARKET QUEUE WAITING TIME",
        f"Queue fit: y = {qa:.8f}x^2 + {qb:.6f}x + {qc:.4f} | RMSE = {q_rmse:.2f} s",
        f"Predicted wait at 80 customers: {q_pred_80:.2f} s",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_14_results.txt").write_text(report, encoding="utf-8")

    x_plot = np.linspace(users.min(), 450.0, 300)
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.scatter(users, response_ms, label="Measured Response Time")
    ax.plot(x_plot, quad_model(x_plot, a, b, c), label="Quadratic Least-Squares Fit")
    ax.set(title="Server Response Time Curve Fitting", xlabel="Concurrent Users", ylabel="Response Time (ms)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_14_curve_fitting.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
