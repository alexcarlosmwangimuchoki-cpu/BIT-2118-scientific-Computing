# BIT2118-Scientific-Computing

Executable Python implementations, computed outputs, generated graphs, and documentation for **BIT 2118: Scientific Computing** (Bachelor of Science in Computer Science, Mount Kenya University).

> **Note on Task Count:** This repository contains **19 executable task scripts** (`Task_01` through `Task_20`, excluding `Task_05`, which is absent from the supplied group report).

## Group Members

| # | Name | Registration Number |
|---|---|---|
| 1 | Alex Carlos | BSCCS 52386/2025 |
| 2 | Collins Kisia | BSCCS/2025/50139 |
| 3 | Maxwel Njenga | BSCCS/2025/54271 |
| 4 | Felix Karathi | BSCCS/2025/52657 |
| 5 | Mbaka Kenyatta | BSCCS/2025/56784 |
| 6 | Haibe Hussein | BSCCS/2025/60612 |
| 7 | Noel Mumo | BSCCS/2025/55765 |
| 8 | Ahmed Mohamed | BSCCS/2025/50006 |

## Repository Structure

```text
BIT2118-Scientific-Computing/
├── README.md
├── requirements.txt
├── run_all.py
├── code/
│   ├── Task_01_numpy_arrays.py
│   ├── Task_02_vectorization.py
│   ├── Task_03_floating_point_errors.py
│   ├── Task_04_matrix_algebra.py
│   ├── Task_06_linear_systems.py
│   ├── Task_07_lu_decomposition.py
│   ├── Task_08_iterative_methods.py
│   ├── Task_09_eigenvalues_eigenvectors.py
│   ├── Task_10_bisection_fixed_point.py
│   ├── Task_11_newton_secant.py
│   ├── Task_12_nonlinear_systems.py
│   ├── Task_13_interpolation.py
│   ├── Task_14_curve_fitting.py
│   ├── Task_15_numerical_differentiation.py
│   ├── Task_16_numerical_integration.py
│   ├── Task_17_euler_method.py
│   ├── Task_18_scipy_ode.py
│   ├── Task_19_optimization.py
│   └── Task_20_monte_carlo.py
├── outputs/
├── graphs/
└── docs/
    └── tasks_overview.md
```

## Setup & Execution

1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Run all 19 tasks sequentially from the repository root:
   ```bash
   python run_all.py
   ```
3. Or run an individual task script:
   ```bash
   python code/Task_01_numpy_arrays.py
   ```
   Each script prints its results, writes a text summary to `outputs/`, and saves visual plots to `graphs/`.
