from setuptools import setup

setup(
    name = "cffi_exa",
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["BO_example_build.py:ffi"],
    install_requires=["cffi>=1.0.0"],
)