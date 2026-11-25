import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    row_len = len(A)
    col_len = len(A[0])

    new_array = [[0] * row_len for _ in range(col_len)]

    for row in range(row_len):
        for col in range(col_len):
            new_array[col][row] = A[row][col]

    return np.array(new_array)