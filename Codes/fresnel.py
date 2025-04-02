import numpy as np
from scipy.integrate import quad

def calculate_fresnel():
    """Compute the Fresnel integral using curvometry principles."""
    result, error = quad(lambda x: np.sin(x**2), 0, np.inf)
    return result, error

if __name__ == "__main__":
    res, err = calculate_fresnel()
    print(f"Fresnel Integral: {res:.5f} (Error: {err:.5f})")
