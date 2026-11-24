def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    top_k = set(recommended[:k])
    relevant = set(relevant)

    retr = len(top_k.intersection(relevant))
    precision_k = retr/k
    recall_k = retr/len(relevant)

    return [precision_k, recall_k]