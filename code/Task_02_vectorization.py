"""
BIT 2118 - Scientific Computing
Task 02: Mathematical Functions and Vectorization
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

import timeit

def main():
    rng = np.random.default_rng(42)
    returns_pct = rng.normal(0.05, 1.2, 1_000_000)

    def loop_version():
        adjusted = []
        for val in returns_pct:
            dec = val / 100.0
            adjusted.append(dec ** 2)
        return adjusted

    def vectorized_version():
        dec = returns_pct / 100.0
        return dec ** 2

    loop_time = timeit.timeit(loop_version, number=1)
    vector_time = timeit.timeit(vectorized_version, number=5) / 5.0
    vec_result = vectorized_version()
    speedup = loop_time / vector_time if vector_time > 0 else float("inf")

    # Latency benchmark (1,000,000 samples from U(5, 250) ms -> seconds squared)
    latency_ms = rng.uniform(5.0, 250.0, 1_000_000)
    latency_sq_s = (latency_ms / 1000.0) ** 2

    lines = [
        "TASK 02: MATHEMATICAL FUNCTIONS AND VECTORIZATION",
        f"First 5 squared decimal returns: {np.round(vec_result[:5], 8)}",
        f"Python loop time (N=1,000,000): {loop_time:.6f} s",
        f"NumPy vectorized time (N=1,000,000): {vector_time:.6f} s",
        f"Approximate speed-up: {speedup:.1f}x",
        f"Mean squared latency (s^2): {np.mean(latency_sq_s):.6e}",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_02_results.txt").write_text(report, encoding="utf-8")

    fig, ax = plt.subplots(figsize=(8, 4.5))
    sizes = [10_000, 100_000, 1_000_000]
    loop_times = []
    vec_times = []
    for n in sizes:
        arr = rng.normal(0.05, 1.2, n)
        t_l = timeit.timeit(lambda: [(x / 100.0) ** 2 for x in arr], number=1)
        t_v = timeit.timeit(lambda: (arr / 100.0) ** 2, number=5) / 5.0
        loop_times.append(t_l)
        vec_times.append(t_v)

    x = np.arange(len(sizes))
    width = 0.35
    ax.bar(x - width/2, loop_times, width, label="Python Loop (s)")
    ax.bar(x + width/2, vec_times, width, label="NumPy Vectorized (s)")
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels([f"N={s:,}" for s in sizes])
    ax.set(title="Loop vs Vectorized Execution Time (Log Scale)", ylabel="Time (seconds)")
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_02_vectorization_benchmark.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
