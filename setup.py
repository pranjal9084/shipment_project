from setuptools import find_packages, setup

setup(
    name="shipment",
    version='0.0.1',
    author='Pranjal Gupta',
    author_email='guptapranjal7890@gmail.com',
    packages=find_packages(),
    install_requires=[
        "httptools",
        "pyarrow"
    ]
)