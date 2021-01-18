import setuptools
from distutils.core import setup, Extension

# See https://stackoverflow.com/a/51272967/5188860
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SS_HardwareController", # Replace with your own username
    version="0.0.1",
    author="Ricardo H. Ramirez-Gonzalez",
    author_email="ricardo@grow.cab",
    description="A to control hardware from the Raspberry Pi in an uniform way",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GrowCab/SS_HardwareController",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
