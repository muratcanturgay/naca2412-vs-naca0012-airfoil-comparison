"""
Airfoil Aerodynamic Comparison: NACA 2412 (cambered) vs NACA 0012 (symmetric)
Data source: XFOIL (Mark Drela, MIT) - Reynolds number = 200,000, Mach = 0
"""

import matplotlib.pyplot as plt

# --- NACA 2412 data (cambered airfoil) ---
alpha_2412 = [-5, -4, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15]
CL_2412 = [-0.4440, -0.2831, 0.1160, 0.2825, 0.4222, 0.5162, 0.6110,
           0.7057, 0.7997, 0.8917, 0.9769, 1.0467, 1.1050, 1.2029, 1.2830]
CD_2412 = [0.01696, 0.01488, 0.01010, 0.00998, 0.00981, 0.01010, 0.01068,
           0.01144, 0.01228, 0.01328, 0.01477, 0.01776, 0.02173, 0.03060, 0.06598]

# --- NACA 0012 data (symmetric airfoil) ---
alpha_0012 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14]
CL_0012 = [-0.6195, -0.5358, -0.4463, -0.3084, -0.1454, 0.0000, 0.1454, 0.3084,
           0.4462, 0.5357, 0.6194, 0.6975, 0.7732, 0.8494, 1.0708, 1.0993, 1.0776, 0.9864]
CD_0012 = [0.01307, 0.01176, 0.01105, 0.01066, 0.01034, 0.01020, 0.01034, 0.01066,
           0.01105, 0.01176, 0.01307, 0.01513, 0.01770, 0.02076, 0.03626, 0.04416, 0.05553, 0.07634]

# Efficiency (lift-to-drag ratio) for each airfoil
eff_2412 = [cl / cd for cl, cd in zip(CL_2412, CD_2412)]
eff_0012 = [cl / cd for cl, cd in zip(CL_0012, CD_0012)]

# --- Individual plots: NACA 2412 ---
plt.figure()
plt.plot(alpha_2412, CL_2412, marker='o')
plt.xlabel("Angle of Attack (deg)")
plt.ylabel("Lift Coefficient (CL)")
plt.title("NACA 2412 - Lift vs Angle of Attack")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(alpha_2412, CD_2412, marker='o', color='red')
plt.xlabel("Angle of Attack (deg)")
plt.ylabel("Drag Coefficient (CD)")
plt.title("NACA 2412 - Drag vs Angle of Attack")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(alpha_2412, eff_2412, marker='o', color='green')
plt.xlabel("Angle of Attack (deg)")
plt.ylabel("Efficiency (CL/CD)")
plt.title("NACA 2412 - Where Is the Most Efficient Angle?")
plt.grid(True)
plt.show()

# --- Individual plots: NACA 0012 ---
plt.figure()
plt.plot(alpha_0012, CL_0012, marker='o')
plt.xlabel("Angle of Attack (deg)")
plt.ylabel("Lift Coefficient (CL)")
plt.title("NACA 0012 - Lift vs Angle of Attack")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(alpha_0012, CD_0012, marker='o', color='red')
plt.xlabel("Angle of Attack (deg)")
plt.ylabel("Drag Coefficient (CD)")
plt.title("NACA 0012 - Drag vs Angle of Attack")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(alpha_0012, eff_0012, color='green')
plt.xlabel("Angle of Attack (deg)")
plt.ylabel("Efficiency (CL/CD)")
plt.title("NACA 0012 - Where Is the Most Efficient Angle?")
plt.grid(True)
plt.show()

# --- Comparison plots: both airfoils on the same graph ---
plt.figure()
plt.plot(alpha_2412, CL_2412, marker='o', label="NACA 2412 (cambered)")
plt.plot(alpha_0012, CL_0012, marker='s', label="NACA 0012 (symmetric)")
plt.xlabel("Angle of Attack (deg)")
plt.ylabel("Lift Coefficient (CL)")
plt.title("Lift Comparison: NACA 2412 vs NACA 0012")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(alpha_2412, CD_2412, marker='o', label="NACA 2412 (cambered)")
plt.plot(alpha_0012, CD_0012, marker='s', label="NACA 0012 (symmetric)")
plt.xlabel("Angle of Attack (deg)")
plt.ylabel("Drag Coefficient (CD)")
plt.title("Drag Comparison: NACA 2412 vs NACA 0012")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(alpha_2412, eff_2412, marker='o', label="NACA 2412 (cambered)")
plt.plot(alpha_0012, eff_0012, marker='s', label="NACA 0012 (symmetric)")
plt.xlabel("Angle of Attack (deg)")
plt.ylabel("Efficiency (CL/CD)")
plt.title("Efficiency Comparison: NACA 2412 vs NACA 0012")
plt.legend()
plt.grid(True)
plt.show()
