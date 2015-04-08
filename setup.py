from setuptools import setup, find_packages

config = {
    "name": "naming",
    "description": "Pure python naming convention library.",
    "author": "Cesar Saez",
    "author_email": "cesarte@gmail.com",
    "url": "http://www.github.com/csaez/naming",
    "version": "0.2.0",
    "install_requires": [],
    "setup_requires": [],
    "packages": find_packages(exclude=['ez_setup', 'examples', 'tests']),
    "scripts": [],
}

setup(**config)
