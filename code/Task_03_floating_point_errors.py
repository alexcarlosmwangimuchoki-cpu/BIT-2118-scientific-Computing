"""
BIT 2118 - Scientific Computing
Task 03: Floating-Point Arithmetic and Numerical Errors
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

from decimal import Decimal

def main():
    calculated = 0.1 + 0.2
    expected = 0.3
    exact_eq = (calculated == expected)
    close_eq = bool(np.isclose(calculated, expected))

    true_val = float(np.sqrt(2.0))
    approx_1 = 1.414
    abs_err_1 = abs(true_val - approx_1)
    rel_err_1 = abs_err_1 / abs(true_val)

    approx_2 = 1.4142
    abs_err_2 = abs(true_val - approx_2)
    rel_err_2 = abs_err_2 / abs(true_val)

    # Real-world case: Shop receipt using Decimal
    price = Decimal("125.50")
    qty_orig = 3
    discount = Decimal("25.00")
    sub_orig = price * qty_orig
    due_orig = sub_orig - discount

    qty_mod = 4
    sub_mod = price * qty_mod
    due_mod = sub_mod - discount

    lines = [
        "TASK 03: FLOATING-POINT ARITHMETIC AND NUMERICAL ERRORS",
        f"0.1 + 0.2 = {calculated:.17f}",
        f"Exact equality (0.1 + 0.2 == 0.3): {exact_eq}",
        f"np.isclose(0.1 + 0.2, 0.3): {close_eq}",
        f"sqrt(2) = {true_val:.10f}",
        f"Approx 1.414 -> Abs Error: {abs_err_1:.8f}, Rel Error: {rel_err_1:.8f} ({rel_err_1*100:.4f}%)",
        f"Approx 1.4142 -> Abs Error: {abs_err_2:.8f}, Rel Error: {rel_err_2:.8f} ({rel_err_2*100:.4f}%)",
        "",
        "REAL-WORLD CASE: SHOP RECEIPT (DECIMAL)",
        f"Qty=3 -> Subtotal: KSh {sub_orig}, Amount Due: KSh {due_orig}",
        f"Qty=4 -> Subtotal: KSh {sub_mod}, Amount Due: KSh {due_mod}",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_03_results.txt").write_text(report, encoding="utf-8")

    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    labels = ["Approx 1.414", "Approx 1.4142"]
    abs_errs = [abs_err_1, abs_err_2]
    ax.bar(labels, abs_errs)
    ax.set(title="Absolute Approximation Error for sqrt(2)", ylabel="Absolute Error")
    ax.grid(True, axis="y")
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_03_floating_point_errors.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
