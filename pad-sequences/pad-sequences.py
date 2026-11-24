import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    N = len(seqs)

    if N == 0:
        return np.empty((0, 0), dtype=int)

    if max_len is None:
        max_len = max(len(seq) for seq in seqs)

    if max_len < 0:
        raise ValueError("max_len must be non-negative")

    result = np.full((N, max_len), pad_value, dtype=int)

    for i, seq in enumerate(seqs):
        length = min(len(seq), max_len)
        result[i, :length] = seq[:length]

    return result