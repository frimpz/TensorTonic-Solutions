def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    x_new = x0
    for i in range(steps):
        grad = 2*a*x_new + b
        x_new = x_new - lr *grad

    return x_new