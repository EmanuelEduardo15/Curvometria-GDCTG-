from scripts.dirac_delta import curved_dirac_delta
import numpy as np

def test_dirac():
    result = curved_dirac_delta()
    expected = np.sqrt(2)
    assert np.isclose(result, expected, rtol=0.01), "Dirac delta test failed!"
