import numpy as np

# Simplified Path Integral Simulation
N = 1000 # Number of curvetons
dt = 0.001
paths = np.random.normal(size=(100, N)) # 100 random paths

# Calculate the action S[x]
S = np.sum((np.diff(paths, axis=1)**2) / (2 * dt), axis=1)
integral = np.mean(np.exp(1j * S)) # Average over paths
print(f"Result: {integral:.5f}")
