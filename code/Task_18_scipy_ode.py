"""
BIT 2118 - Scientific Computing
Task 18: SciPy ODE Integration for RC Circuit Dynamics
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

from scipy.integrate import solve_ivp

def rc_circuit(t, Vc, R, C, Vin):
    return [(Vin - Vc[0]) / (R * C)]

def main():
    R = 1000.0
    C_values = [1e-6, 2.2e-6, 4.7e-6]
    Vin = 5.0
    t_span = (0.0, 0.02)
    t_eval = np.linspace(0.0, 0.02, 1000)

    lines = ["TASK 18: SCIPY ODE INTEGRATION (RC CIRCUIT CHARGING)"]
    fig, ax = plt.subplots(figsize=(8.5, 4.8))

    for C in C_values:
        sol = solve_ivp(rc_circuit, t_span, [0.0], args=(R, C, Vin), t_eval=t_eval, method="RK45")
        tau_ms = R * C * 1e3
        v_end = float(sol.y[0, -1])
        lines.append(f"C={C*1e6:3.1f} uF (tau={tau_ms:3.1f} ms) -> V_C(20ms)={v_end:.4f} V")
        ax.plot(sol.t * 1000.0, sol.y[0], label=f"C={C*1e6:.1f} uF (tau={tau_ms:.1f} ms)")

    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_18_results.txt").write_text(report, encoding="utf-8")

    ax.set(title="Task 18: RC Circuit Charging Dynamics (RK45)", xlabel="Time (ms)", ylabel="Capacitor Voltage V_C (V)")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_18_scipy_capacitor.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
