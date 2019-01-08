from distutils.core import setup

setup(
    name="pyeactivities",
    packages=["pyeactivities"],
    version="0.1.0",
    description="Python API Wrapper for Imperial College Union eActivities",
    author="Fraser May",
    author_email="frasertmay@gmail.com",
    url="https://github.com/ftm/pyeactivities",
    install_requires=[
        "requests>=2.21.0"
    ]
)
