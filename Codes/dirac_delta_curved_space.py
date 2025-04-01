import numpy as np

# Dirac Delta in Curved Space
x = np.linspace(-2, 2, 100000)
kappa = 1000 * np.exp(-100 * (x**2 - 1)**2)
integral = np.sum(kappa * np.sqrt(1 + x**2)) * 4 / 100000
print(f"Result: {integral:.3f} (Theoretical: √2 ≈ 1.414)")
