from scripts.fresnel import calculate_fresnel
import numpy as np

def test_fresnel():
    result, error = calculate_fresnel()
    expected = np.sqrt(np.pi / 8)
    assert np.isclose(result, expected, atol=error), "Fresnel integral failed!"
