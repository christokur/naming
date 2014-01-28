from setuptools import setup, find_packages

config = {
    "name": "naming",
    "description": "Pure python naming convention.",
    "author": "Cesar Saez",
    "author_email": "cesarte@gmail.com",
    "url": "http://www.github.com/csaez/naming",
    "version": "0.1.0",
    "install_requires": ["nose"],
    "setup_requires": ["nose>=1.0"],
    "packages": find_packages(exclude=['ez_setup', 'examples', 'tests']),
    "scripts": [],
    "entry_points": {"gui_scripts": ["naming_editor = naming.editor:main"]},
}

setup(**config)
