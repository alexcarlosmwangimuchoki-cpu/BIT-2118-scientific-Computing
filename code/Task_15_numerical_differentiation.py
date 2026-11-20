"""
BIT 2118 - Scientific Computing
Task 15: Numerical Differentiation
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

def estimate_speed(time_s, position_m):
    speed = np.zeros(len(position_m), dtype=float)
    speed[0] = (position_m[1] - position_m[0]) / (time_s[1] - time_s[0])
    for i in range(1, len(time_s) - 1):
        speed[i] = (position_m[i + 1] - position_m[i - 1]) / (time_s[i + 1] - time_s[i - 1])
    speed[-1] = (position_m[-1] - position_m[-2]) / (time_s[-1] - time_s[-2])
    return speed

def main():
    time_s = np.arange(0, 7, dtype=float)
    position_m = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])
    speed = estimate_speed(time_s, position_m)

    changed_pos = position_m.copy()
    changed_pos[3] = 17.1
    changed_speed = estimate_speed(time_s, changed_pos)

    water_t = np.array([0, 1, 2, 3, 4, 5], dtype=float)
    vol_l = np.array([0, 12, 25, 39, 54, 70], dtype=float)
    flow_l_min = estimate_speed(water_t, vol_l)

    lines = [
        "TASK 15: NUMERICAL DIFFERENTIATION",
        f"Speeds (m/s): {np.round(speed, 3)}",
        f"Speed at t=3s before: {speed[3]:.3f} m/s | after pos[3]=17.1m: {changed_speed[3]:.3f} m/s",
        f"Water flow rate (L/min): {np.round(flow_l_min, 3)}",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_15_results.txt").write_text(report, encoding="utf-8")

    fig, axes = plt.subplots(2, 1, figsize=(8.5, 6.5))
    axes[0].plot(time_s, position_m, "o-", label="Original GPS Position")
    axes[0].plot(time_s, changed_pos, "s--", label="Modified t=3s Position (17.1m)")
    axes[0].set(title="GPS Position vs Time", xlabel="Time (s)", ylabel="Position (m)")
    axes[0].grid(True)
    axes[0].legend()

    axes[1].plot(time_s, speed, "o-", label="Original Speed")
    axes[1].plot(time_s, changed_speed, "s--", label="Modified Speed")
    axes[1].set(title="Estimated Speed vs Time", xlabel="Time (s)", ylabel="Speed (m/s)")
    axes[1].grid(True)
    axes[1].legend()

    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_15_numerical_differentiation.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
