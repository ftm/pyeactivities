import os
import re

import setuptools

# Get version from __version__ variable in pyeactivities/__init__.py
# Code based on https://github.com/pypa/pip/blob/master/setup.py
here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string")


VERSION = find_version("pyeactivities", "__init__.py")


# Get long description from README file
with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pyeactivities-ftm",
    version=VERSION,
    author="Fraser May",
    author_email="frasertmay@gmail.com",
    description="Python API Wrapper for Imperial College Union eActivities",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ftm/pyeactivities",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    install_requires=["requests>=2.21.0"],
)
