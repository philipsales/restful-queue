# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "flask_api_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Swagger ReST Article",
    author_email="",
    url="",
    keywords=["Swagger", "Swagger ReST Article"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['flask_api_server/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['flask_api_server=flask_api_server.__main__:main']},
    long_description="""\
    This is the swagger file that goes with our server code
    """
)

