import numpy as np

def adam_step(
    param: list,
    grad: list,
    m: list,
    v: list,
    t: int,
    lr: float = 1e-3,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns (param_new, m_new, v_new) as NumPy arrays.
    """
    # Write code here
    m = np.array(m)
    v = np.array(v)
    grad = np.array(grad)
    param = np.array(param)

    m_t = beta1*m + (1-beta1)*grad
    v_t = beta2*v + (1-beta2)*(np.power(grad, 2))

    m_new = m_t/(1-np.power(beta1, t))
    v_new = v_t/(1-np.power(beta2, t))

    param_new = param - (lr*(m_new/(np.sqrt(v_new) + eps)))

    return (param_new, m_t, v_t)

