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

    summation = 0
    for i in counts:
        p_i = i/total
        summation += p_i * np.log2(p_i)
        
    return -1 * summation
    