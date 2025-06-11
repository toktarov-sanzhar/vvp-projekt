import numpy as np
from numba import njit

@njit()
def julia(z: complex, c: complex, max_iter: int) -> int:
    """Compute the number of iterations for Julia formula until divergence or max_iter.

    Parameters:
    - z (complex): Initial complex point.
    - c (complex): Constant parameter for Julia set.
    - max_iter (int): Maximum iterations.

    Returns:
    - int: Number of iterations before divergence (or max_iter).
    """
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def compute_julia_set(c: complex, xmin: float, xmax: float,
                      ymin: float, ymax: float, width: int,
                      height: int, max_iter: int) -> np.ndarray:
    """Compute a 2D array of Julia values for a region in the complex plane.

    Parameters:
    - c (complex): Julia set constant.
    - xmin, xmax, ymin, ymax (float): Bounds of the complex plane.
    - width, height (int): Resolution of the output image.
    - max_iter (int): Max iterations per point.

    Returns:
    - np.ndarray: 2D array representing the Julia set.
    """
    result = np.zeros((height, width), dtype=np.int32)
    for i in range(height):
        for j in range(width):
            re = xmin + (xmax - xmin) * j / width
            im = ymin + (ymax - ymin) * i / height
            z = complex(re, im)
            result[i, j] = julia(z, c, max_iter)

    return result