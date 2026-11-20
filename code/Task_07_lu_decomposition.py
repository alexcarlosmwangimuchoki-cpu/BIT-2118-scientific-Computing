"""
BIT 2118 - Scientific Computing
Task 07: Gaussian Elimination and LU Decomposition
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

from scipy.linalg import lu_factor, lu_solve

def main():
    A = np.array([
        [4.0, 1.0, 0.0],
        [-1.0, 4.0, -1.0],
        [0.0, -1.0, 3.0],
    ], dtype=float)
    b_list = [
        np.array([15.0, 10.0, 10.0]),
        np.array([16.0, 11.0, 9.0]),
        np.array([14.0, 12.0, 11.0]),
    ]

    lu, piv = lu_factor(A)
    sols = [lu_solve((lu, piv), bi) for bi in b_list]

    # Parameter experiment: A[0, 1] = 1.0 -> 3.0
    A_mod = A.copy()
    A_mod[0, 1] = 3.0
    lu_m, piv_m = lu_factor(A_mod)
    sol_m1 = lu_solve((lu_m, piv_m), b_list[0])

    # Real-world case: Structural Truss Displacements across 3 load steps
    K_stiff = np.array([
        [50.0, -20.0, 0.0],
        [-20.0, 40.0, -10.0],
        [0.0, -10.0, 30.0],
    ], dtype=float)
    forces = [
        np.array([100.0, 150.0, 50.0]),
        np.array([120.0, 180.0, 70.0]),
        np.array([80.0, 200.0, 90.0]),
    ]
    lu_k, piv_k = lu_factor(K_stiff)
    displacements = [lu_solve((lu_k, piv_k), f) for f in forces]

    lines = [
        "TASK 07: LU DECOMPOSITION (PA = LU)",
        f"Set 1 solution: {np.round(sols[0], 4)}",
        f"Set 2 solution: {np.round(sols[1], 4)}",
        f"Set 3 solution: {np.round(sols[2], 4)}",
        f"Modified A[0,1]=3.0 (Set 1): {np.round(sol_m1, 4)}",
        "",
        "REAL-WORLD CASE: STRUCTURAL TRUSS DISPLACEMENTS (mm)",
    ]
    for idx, disp in enumerate(displacements, start=1):
        lines.append(f"Hour {idx} displacements: {np.round(disp, 4)}")

    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_07_results.txt").write_text(report, encoding="utf-8")

    fig, ax = plt.subplots(figsize=(8, 4.8))
    disp_arr = np.array(displacements)
    for node in range(3):
        ax.plot([1, 2, 3], disp_arr[:, node], "o-", label=f"Node {node+1}")
    ax.set(title="Structural Truss Node Displacements Over 3 Timesteps", xlabel="Timestep (Hour)", ylabel="Displacement (mm)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_07_lu_truss_displacements.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
