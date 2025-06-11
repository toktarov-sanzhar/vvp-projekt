import numpy as np
<<<<<<< HEAD
from numba import njit

@njit()
def mandelbrot(c: complex, max_iter: int) -> int:
    """Compute the number of iterations for the Mandelbrot formula
    until divergence or reaching the max_iter.

    Parameters:
    - c (complex): The complex point to test.
    - max_iter (int): Maximum number of iterations.

    Returns:
    - int: Number of iterations before divergence (or max_iter).
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def compute_mandelbrot_set(xmin: float, xmax: float, ymin: float, ymax: float,
                           width: int, height: int, max_iter: int) -> np.ndarray:
    """Compute a 2D array of Mandelbrot values for a region of the complex plane.

    Parameters:
    - xmin, xmax, ymin, ymax (float): Bounds of the complex plane region.
    - width, height (int): Resolution of the output image.
    - max_iter (int): Max iterations per point.

    Returns:
    - np.ndarray: 2D array representing the Mandelbrot set.
    """
    result = np.zeros((height, width), dtype=np.int32)
    for i in range(height):
        for j in range(width):
            re = xmin + (xmax - xmin) * j / width
            im = ymin + (ymax - ymin) * i / height
            c = complex(re, im)
=======
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
>>>>>>> 5b19da3a35a2ebaee1badc58f5c0986c681f2009
            result[i, j] = mandelbrot(c, max_iter)
    return result
