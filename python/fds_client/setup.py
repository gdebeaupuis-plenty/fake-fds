
from setuptools import find_packages, setup  # noqa: H301

NAME = "fdsclient"
VERSION = "0.0.3"

REQUIRES = []

setup(
    name=NAME,
    version=VERSION,
    description="Fake FDS",
    author_email="info@plenty.ag",
    url="",
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Fake
    """
)
