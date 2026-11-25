import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x)
    x_bar = np.mean(x)
    n = np.shape(x)[0]

    variance = (1/(n-1))* np.sum(np.power((x-x_bar), 2))
    sqrt = np.sqrt(variance)

    return {"variance": float(variance), "standard_deviation": float(sqrt)}