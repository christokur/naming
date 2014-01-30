# This file is part of naming
# Copyright (C) 2014  Cesar Saez

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation version 3.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
    "entry_points": {"gui_scripts": ["naming_editor = naming.layout.editor:main"]},
}

setup(**config)
