"""
BIT 2118 - Scientific Computing
Task 04: Matrix Algebra and Matrix Operations
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
    points = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
    ], dtype=float)

    angle_45 = np.deg2rad(45.0)
    rot_45 = np.array([
        [np.cos(angle_45), -np.sin(angle_45)],
        [np.sin(angle_45), np.cos(angle_45)]
    ], dtype=float)
    scale_mat = np.array([
        [2.0, 0.0],
        [0.0, 1.5]
    ], dtype=float)

    tf_45 = rot_45 @ scale_mat
    pts_45 = points @ tf_45.T
    det_45 = float(np.linalg.det(tf_45))

    angle_90 = np.deg2rad(90.0)
    rot_90 = np.array([
        [np.cos(angle_90), -np.sin(angle_90)],
        [np.sin(angle_90), np.cos(angle_90)]
    ], dtype=float)
    tf_90 = rot_90 @ scale_mat
    pts_90 = points @ tf_90.T
    det_90 = float(np.linalg.det(tf_90))

    # Real-world case: Robot floor map coordinates (30 deg rotation, 1.2 scale)
    robot_pts = np.array([[2.0, 1.0], [4.0, 1.0], [2.0, 3.0]], dtype=float)
    angle_30 = np.deg2rad(30.0)
    rot_30 = np.array([
        [np.cos(angle_30), -np.sin(angle_30)],
        [np.sin(angle_30), np.cos(angle_30)]
    ], dtype=float)
    robot_tf = rot_30 @ (1.2 * np.eye(2))
    robot_new = robot_pts @ robot_tf.T

    lines = [
        "TASK 04: MATRIX ALGEBRA AND MATRIX OPERATIONS",
        f"45-deg + Scale Determinant: {det_45:.4f}",
        f"Transformed points (45 deg):\n{np.round(pts_45, 4)}",
        f"90-deg + Scale Determinant: {det_90:.4f}",
        f"Transformed points (90 deg):\n{np.round(pts_90, 4)}",
        "",
        "REAL-WORLD CASE: ROBOT MAP TRANSFORMATION (30 deg, scale 1.2)",
        f"New map coordinates:\n{np.round(robot_new, 4)}",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_04_results.txt").write_text(report, encoding="utf-8")

    fig, ax = plt.subplots(figsize=(7, 7))
    sq_closed = np.vstack([points, points[0]])
    p45_closed = np.vstack([pts_45, pts_45[0]])
    p90_closed = np.vstack([pts_90, pts_90[0]])
    ax.plot(sq_closed[:, 0], sq_closed[:, 1], "o-", label="Original Unit Square")
    ax.plot(p45_closed[:, 0], p45_closed[:, 1], "s--", label="45-deg + Scale")
    ax.plot(p90_closed[:, 0], p90_closed[:, 1], "^:", label="90-deg + Scale")
    ax.set_aspect("equal")
    ax.set(title="2D Affine Matrix Transformations", xlabel="X", ylabel="Y")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_04_matrix_transformations.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
