import numpy as np

def tanh(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.array(x)

    tanh_x = (np.power(np.e, x) - np.power(np.e, -x)) / (np.power(np.e, x) + np.power(np.e, -x))

    return tanh_x