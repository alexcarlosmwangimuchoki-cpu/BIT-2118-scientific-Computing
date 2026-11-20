"""
BIT 2118 - Scientific Computing
Task 08: Iterative Methods for Linear Systems (Jacobi & Gauss-Seidel)
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

def solve_jacobi_gs(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b, dtype=float)
    errors_j = []
    for _ in range(max_iter):
        xn = (b - R @ x) / D
        errors_j.append(float(np.max(np.abs(xn - x))))
        x = xn
        if errors_j[-1] < tol:
            break

    xg = np.zeros_like(b, dtype=float)
    errors_gs = []
    for _ in range(max_iter):
        old = xg.copy()
        for i in range(len(b)):
            xg[i] = (b[i] - A[i, :i] @ xg[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        errors_gs.append(float(np.max(np.abs(xg - old))))
        if errors_gs[-1] < tol:
            break

    return x, errors_j, xg, errors_gs

def main():
    A = np.array([
        [2.0, -1.0, 0.0, 0.0, 0.0],
        [-1.0, 2.0, -1.0, 0.0, 0.0],
        [0.0, -1.0, 2.0, -1.0, 0.0],
        [0.0, 0.0, -1.0, 2.0, -1.0],
        [0.0, 0.0, 0.0, -1.0, 2.0],
    ], dtype=float)
    b = np.array([100.0, 0.0, 0.0, 0.0, 20.0], dtype=float)
    xj, err_j, xgs, err_gs = solve_jacobi_gs(A, b, tol=1e-8)
    x_direct = np.linalg.solve(A, b)

    # Greenhouse wall case (35 C left, 5 C right, tol=1e-6)
    b_green = np.array([35.0, 0.0, 0.0, 0.0, 5.0], dtype=float)
    _, _, xg_green, err_gs_green = solve_jacobi_gs(A, b_green, tol=1e-6)

    lines = [
        "TASK 08: ITERATIVE METHODS (JACOBI & GAUSS-SEIDEL)",
        f"Jacobi temps ({len(err_j)} iters): {np.round(xj, 6)}",
        f"Gauss-Seidel temps ({len(err_gs)} iters): {np.round(xgs, 6)}",
        f"Direct solve check: {np.round(x_direct, 6)}",
        "",
        "REAL-WORLD CASE: GREENHOUSE WALL (35 C -> 5 C, tol=1e-6)",
        f"Gauss-Seidel temps ({len(err_gs_green)} iters): {np.round(xg_green, 4)}",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_08_results.txt").write_text(report, encoding="utf-8")

    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.semilogy(err_j, label=f"Jacobi ({len(err_j)} iters)")
    ax.semilogy(err_gs, label=f"Gauss-Seidel ({len(err_gs)} iters)")
    ax.set(title="Convergence of Iterative Temperature Solution", xlabel="Iteration", ylabel="Max Change (log scale)")
    ax.grid(True, which="both")
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_08_iterative_convergence.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
