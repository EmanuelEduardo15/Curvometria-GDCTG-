import numpy as np

def curvature_energy(kappa, beta=1.0):
    """Folding energy from curvature"""
    return beta * np.sum(kappa**2)

# Example: target curvature (simulated)
kappa_target = np.array([0.2, 0.4, 0.1, 0.3])
energy = curvature_energy(kappa_target)
print(f"Folding energy: {energy:.2f} kT")
