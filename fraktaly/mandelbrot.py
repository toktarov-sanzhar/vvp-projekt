import numpy as np
from numba import njit, prange

@njit
def mandelbrot(c: complex, max_iter: int) -> int:
    z = 0 + 0j
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

@njit
def compute_mandelbrot_set(xmin: float, xmax: float, ymin: float, ymax: float,
                           width: int, height: int, max_iter: int) -> np.ndarray:
    result = np.zeros((height, width), dtype=np.int32)
    for i in prange(height):
        for j in prange(width):
            real = xmin + j * (xmax - xmin) / width
            imag = ymin + i * (ymax - ymin) / height
            c = complex(real, imag)
            result[i, j] = mandelbrot(c, max_iter)
    return result
