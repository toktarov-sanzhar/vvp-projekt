import numpy as np
from numba import njit, prange

@njit
def julia_point(z: complex, c: complex, max_iter: int) -> int:
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

@njit
def compute_julia_set(c: complex, xmin: float, xmax: float, ymin: float, ymax: float,
                      width: int, height: int, max_iter: int) -> np.ndarray:
    result = np.zeros((height, width), dtype=np.int32)
    for i in prange(height):
        for j in prange(width):
            real = xmin + j * (xmax - xmin) / width
            imag = ymin + i * (ymax - ymin) / height
            z = complex(real, imag)
            result[i, j] = julia_point(z, c, max_iter)
    return result
