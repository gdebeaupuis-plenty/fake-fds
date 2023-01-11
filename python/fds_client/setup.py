
from setuptools import find_packages, setup  # noqa: H301

NAME = "fds-client"
VERSION = "1.0.0"

REQUIRES = []

setup(
    name=NAME,
    version=VERSION,
    description="Fake Farm Definition Service API",
    author_email="info@plenty.ag",
    url="",
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Fake
    """
)
