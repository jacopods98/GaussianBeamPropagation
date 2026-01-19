from setuptools import setup, find_packages

setup(
    name="GaussianBeamPropagation",
    version="0.1.0",
    description="Gaussian beam propagation with ABCD matrices",
    packages=find_packages(),
    install_requires=["numpy", "sympy", "matplotlib"],
    python_requires=">=3.7",
)
