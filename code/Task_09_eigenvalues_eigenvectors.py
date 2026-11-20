"""
BIT 2118 - Scientific Computing
Task 09: Eigenvalues and Eigenvectors (Network Centrality)
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

def compute_centrality(adj):
    vals, vecs = np.linalg.eig(adj)
    idx = int(np.argmax(np.real(vals)))
    lam = float(np.real(vals[idx]))
    v = np.abs(np.real(vecs[:, idx]))
    scores = v / np.sum(v)
    ver_err = float(np.linalg.norm(adj @ vecs[:, idx] - lam * vecs[:, idx]))
    return lam, scores, ver_err

def main():
    nodes = ["A", "B", "C", "D"]
    A = np.array([
        [0.0, 1.0, 1.0, 0.0],
        [1.0, 0.0, 1.0, 1.0],
        [1.0, 1.0, 0.0, 1.0],
        [0.0, 1.0, 1.0, 0.0],
    ], dtype=float)
    lam, scores, ver_err = compute_centrality(A)

    # Remove B-D edge (indices 1 and 3)
    A_mod = A.copy()
    A_mod[1, 3] = 0.0
    A_mod[3, 1] = 0.0
    lam_mod, scores_mod, _ = compute_centrality(A_mod)

    lines = [
        "TASK 09: EIGENVALUES AND EIGENVECTORS (CENTRALITY)",
        f"Dominant eigenvalue: {lam:.6f} | Verification error: {ver_err:.2e}",
        "Scores (Original): " + ", ".join(f"{n}={s:.4f}" for n, s in zip(nodes, scores)),
        "",
        "PARAMETER CHANGE: REMOVE B-D EDGE",
        f"Modified dominant eigenvalue: {lam_mod:.6f}",
        "Scores (Modified): " + ", ".join(f"{n}={s:.4f}" for n, s in zip(nodes, scores_mod)),
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_09_results.txt").write_text(report, encoding="utf-8")

    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    x = np.arange(len(nodes))
    w = 0.35
    ax.bar(x - w/2, scores, w, label="Original Network")
    ax.bar(x + w/2, scores_mod, w, label="B-D Edge Removed")
    ax.set_xticks(x)
    ax.set_xticklabels(nodes)
    ax.set(title="Eigenvector Centrality Scores by Node", xlabel="Node", ylabel="Normalized Importance")
    ax.grid(True, axis="y")
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_09_eigenvector_centrality.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
