from setuptools import setup, find_packages

setup(
    name="fraktaly",
    packages=find_packages(),
    description="Interactive fractal visualizer using Mandelbrot and Julia sets.",
    author="Sanzhar Toktarov",
    install_requires=[
        "numpy",
        "matplotlib",
        "numba"
    ],
)
