import numpy as np
import matplotlib.pyplot as plt

def curvometry_force(kappa, R):
    """Calculate curvature force term for Navier-Stokes."""
    return -np.gradient(kappa * R)

# Simulate turbulence
kappa = np.linspace(0, 10, 100)
R = 1.0 / kappa
F_curv = curvometry_force(kappa, R)

# Plot results
plt.plot(kappa, F_curv)
plt.xlabel('Curvature (κ)')
plt.ylabel('Curvature Force (F_curv)')
plt.savefig('fig3.png')
