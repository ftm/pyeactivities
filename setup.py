import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pyeactivities-ftm",
    version="0.1.0",
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
    install_requires=[
        "requests>=2.21.0"
    ]
)
