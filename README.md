# Airfoil Aerodynamic Analysis: NACA 2412 vs NACA 0012

*(Türkçe için bkz. [README.tr.md](README.tr.md))*

## Overview
This project analyzes and compares the aerodynamic performance of two well-known airfoil profiles — the **cambered NACA 2412** and the **symmetric NACA 0012** — across a range of angles of attack, using XFOIL for computation and Python/Matplotlib for visualization.

## Method
- **Tool:** XFOIL (Mark Drela, MIT) — a 2D airfoil analysis tool that computes lift and drag characteristics from airfoil geometry and flow conditions.
- **Conditions:** Reynolds number = 200,000 (representative of small UAV/model aircraft scale), Mach = 0, identical for both airfoils to allow direct comparison.
- **Angle of attack range:** NACA 2412: -5° to 15°. NACA 0012: -5° to 14°. (Small differences reflect the actual angles at which XFOIL converged to a solution for each airfoil.)

## Results — NACA 2412 (cambered)
- Lift coefficient (CL) increases steadily with angle of attack, flattening around 9-11°, indicating approach to stall.
- Drag coefficient (CD) stays low between -1° and 5°, then rises sharply beyond 7°.
- **Maximum efficiency (CL/CD ≈ 67) occurs around 6-7°.**

## Results — NACA 0012 (symmetric)
- As expected for a symmetric airfoil, CL = 0 exactly at 0° angle of attack (the 2412 airfoil, by contrast, still produces lift at 0° due to its camber).
- **Maximum efficiency (CL/CD ≈ 47) occurs around 5°** — notably lower than the 2412's peak efficiency.

## Comparison — Which Airfoil Is "Better"?
The cambered NACA 2412 achieves a **higher maximum efficiency** than the symmetric NACA 0012, meaning it generates more lift relative to drag at its optimal angle. This makes cambered airfoils the typical choice for main wings, where efficient lift generation is the priority.

However, symmetric airfoils like the NACA 0012 have their own advantage: they perform **identically in both directions** (positive and negative angle of attack), which is valuable for control surfaces like tail fins and stabilizers, or for aerobatic aircraft that need equal performance when flying inverted. Camber trades this symmetry for higher one-directional efficiency.

## Tools Used
- XFOIL (aerodynamic computation)
- Python 3 + Matplotlib (data visualization)

## Files
- `naca2412_naca0012_comparison_en.py` / `naca2412_naca0012_comparison_tr.py` — combined analysis and comparison scripts (English/Turkish comments)
- `data/naca2412_xfoil_output.txt`, `data/naca0012_xfoil_output.txt` — raw XFOIL output (polar data) for each airfoil
- Plot images — individual and comparison plots for lift, drag, and efficiency
