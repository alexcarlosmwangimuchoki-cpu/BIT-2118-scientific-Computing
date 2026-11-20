"""
BIT 2118 - Scientific Computing
Task 11: Newton-Raphson and Secant Methods (IRR & Loan Rate)
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
GRAPH_DIR = ROOT / "graphs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

from scipy.optimize import root_scalar

def calc_npv(r, cfs):
    return sum(cf / ((1.0 + r) ** t) for t, cf in enumerate(cfs))

def calc_dnpv(r, cfs):
    return sum(-t * cf / ((1.0 + r) ** (t + 1)) for t, cf in enumerate(cfs) if t > 0)

def main():
    cfs = [-10000.0, 3000.0, 3500.0, 4000.0, 2500.0]
    nr = root_scalar(lambda r: calc_npv(r, cfs), fprime=lambda r: calc_dnpv(r, cfs), x0=0.10, method="newton", xtol=1e-12)
    sec = root_scalar(lambda r: calc_npv(r, cfs), x0=0.05, x1=0.20, method="secant", xtol=1e-12)

    cfs_mod = [-11500.0, 3000.0, 3500.0, 4000.0, 2500.0]
    nr_mod = root_scalar(lambda r: calc_npv(r, cfs_mod), fprime=lambda r: calc_dnpv(r, cfs_mod), x0=0.10, method="newton", xtol=1e-12)

    # Real-world case: Loan effective interest rate
    loan_cfs = [24500.0, -6200.0, -6200.0, -6200.0, -6200.0, -6200.0]
    loan_nr = root_scalar(lambda r: calc_npv(r, loan_cfs), fprime=lambda r: calc_dnpv(r, loan_cfs), x0=0.08, method="newton", xtol=1e-12)
    loan_sec = root_scalar(lambda r: calc_npv(r, loan_cfs), x0=0.04, x1=0.15, method="secant", xtol=1e-12)

    lines = [
        "TASK 11: NEWTON-RAPHSON AND SECANT METHODS",
        f"IRR (Newton-Raphson): {nr.root:.6%} ({nr.iterations} iters) | NPV check: {calc_npv(nr.root, cfs):.8f}",
        f"IRR (Secant):         {sec.root:.6%} ({sec.iterations} iters)",
        f"Modified outlay (-$11,500) IRR: {nr_mod.root:.6%}",
        "",
        "REAL-WORLD CASE: LOAN EFFECTIVE INTEREST RATE",
        f"Effective Rate (Newton): {loan_nr.root:.6%} ({loan_nr.iterations} iters)",
        f"Effective Rate (Secant): {loan_sec.root:.6%} ({loan_sec.iterations} iters)",
    ]
    report = "\n".join(lines) + "\n"
    print(report)
    (OUT_DIR / "task_11_results.txt").write_text(report, encoding="utf-8")

    rates = np.linspace(0.0, 0.30, 200)
    npvs = [calc_npv(r, cfs) for r in rates]
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(rates * 100, npvs, label="NPV(r)")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.axvline(nr.root * 100, linestyle="--", label=f"IRR = {nr.root:.2%}")
    ax.set(title="Net Present Value vs Discount Rate", xlabel="Discount Rate r (%)", ylabel="NPV ($)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / "task_11_npv_irr_curve.png", dpi=180)
    plt.close(fig)

if __name__ == "__main__":
    main()
