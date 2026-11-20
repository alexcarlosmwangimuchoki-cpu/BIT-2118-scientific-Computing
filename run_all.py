"""
BIT 2118 - Scientific Computing
Master Runner: Executes all 19 task scripts sequentially and reports execution status.
"""

from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
CODE_DIR = ROOT / "code"

def main():
    scripts = sorted(CODE_DIR.glob("Task_*.py"))
    print(f"Found {len(scripts)} task scripts in {CODE_DIR}\n" + "=" * 60)
    passed = 0
    failed = []
    start_all = time.perf_counter()

    for idx, script in enumerate(scripts, start=1):
        t0 = time.perf_counter()
        res = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
        elapsed = time.perf_counter() - t0
        if res.returncode == 0:
            passed += 1
            print(f"[{idx:02d}/{len(scripts):02d}] PASS ({elapsed:5.2f}s) -> {script.name}")
        else:
            failed.append((script.name, res.stderr))
            print(f"[{idx:02d}/{len(scripts):02d}] FAIL ({elapsed:5.2f}s) -> {script.name}")

    total_elapsed = time.perf_counter() - start_all
    print("=" * 60)
    print(f"Completed {passed}/{len(scripts)} tasks successfully in {total_elapsed:.2f}s.")
    if failed:
        for name, err in failed:
            print(f"--- Error in {name} ---\n{err}")
        sys.exit(1)

if __name__ == "__main__":
    main()
