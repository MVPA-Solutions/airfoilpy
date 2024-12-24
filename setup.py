from setuptools import setup, find_packages

setup(
    name="airfoilpy",
    version="1.0.1",
    description="A basic package for generating and working with airfoil shapes.",
    author="Josh",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)