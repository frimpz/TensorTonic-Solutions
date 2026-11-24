import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    if len(x) == 0:
        return 0.0

    x = np.asarray(x, dtype=np.float32)
    p = np.asarray(p, dtype=np.float32)

    expected = np.sum(x*p)
    return expected