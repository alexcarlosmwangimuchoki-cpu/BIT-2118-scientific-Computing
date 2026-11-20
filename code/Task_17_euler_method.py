"""
BIT 2118 - Scientific Computing
Task 17: Euler's Method for Newton's Law of Cooling
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

def euler_cooling(T0, T_env, k, dt, total_time):
    num_steps = int(total_time / dt) + 1
    t = np.linspace(0.0, total_time, num_steps)
    T = np.zeros(num_steps, dtype=float)
    T[0] = T0
    for i in range(num_steps - 1):
        dTdt = -k * (T[i] - T_env)
        T[i + 1] = T[i] + dTdt * dt
    return t, T

def main():
    T0, T_env, k = 90.0, 20.0, 0.05
    t_exact = np.linspace(0.0, 100.0, 500)
    T_exact = T_env + (T0 - T_env) * np.exp(-k * t_exact)

    lines = ["TASK 17: EULER'S METHOD FOR NEWTON'S LAW OF COOLING"]
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.plot(t_exact, T_exact, "k-", label="Exact Analytical Solution")

    for dt in [10.0, 2.0, 0.5]:
        t_e, T_e = euler_cooling(T0, T_env, k, dt, 100.0)
        exact_at_t = T_env + (T0 - T_env) * np.exp(-k * t_e)
        max_err = float(np.max(np.abs(T_e - exact_at_t)))
        lines.append(f"dt={dt:4.1f}s -> Final T(100s)={T_e[-1]:.4f} C | Max Abs Error={max_err:.4f} C")
        ax.plot(t_e, T_e, "o--", markersize=3, label=f"Euler (dt={dt}s)")

    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_17_results.txt").write_text(report, encoding="utf-8")

    ax.set(title="Task 17: Euler's Method vs Exact Cooling Curve", xlabel="Time (s)", ylabel="Temperature (C)")
    ax.grid(True, linestyle=":", alpha=0.7)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_17_euler_cooling.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
