import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    if len(y) == 0:
        return 0.0

    total = len(y)
    values, counts = np.unique(y, return_counts=True)
    if len(values) == 1:
        return 0.0

    prob = counts/total

    h_s = -1*np.sum(prob*np.log2(prob))
    return h_s
    