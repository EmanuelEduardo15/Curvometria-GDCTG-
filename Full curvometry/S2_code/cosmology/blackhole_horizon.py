import numpy as np
import matplotlib.pyplot as plt

# Dynamic radius for black holes
def dynamic_radius(E, E_Planck=1.0):
    return 1 / (1 - E/E_Planck)

# Simulation
E = np.linspace(0, 0.99, 100)
R = dynamic_radius(E)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(E, R, 'b-', linewidth=2)
plt.xlabel('Energy (E/E_Planck)')
plt.ylabel('Radius (R)')
plt.title('Curvometry Avoids Singularities')
plt.savefig('fig3c_blackhole.pdf', dpi=600)
