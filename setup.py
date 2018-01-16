#!/usr/bin/env python

"""
Installer for pyvxl libraries and command-line tools.

Run "python setup.py install" to install script shortcuts in your path.

Requires setuptools (http://pypi.python.org/pypi/setuptools/).
"""

from setuptools import setup, find_packages

import os
import sys
import admin
if os.name == 'nt':
    from ctypes import WinDLL


LIB_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), 'lib'))

missing_dependencies = []

# Install the vector dll
try:
    if os.name == 'nt':
        try:
            vxDLL = WinDLL("c:\\Users\\Public\\Documents\\Vector XL Driver Library\\bin\\vxlapi.dll")
        except WindowsError:
            vxDLL = WinDLL("c:\\Documents and Settings\\All Users\\Documents\\Vector XL Driver Library\\bin\\vxlapi.dll")
except WindowsError:
    if not admin.isUserAdmin():
        path = os.path.join(LIB_PATH, 'xl_lib97.exe')
        admin.runAsAdmin(cmdLine=[path])
        raw_input('Press return to continue . . .')
    else:
        install_exe('xl_lib97.exe')


# Install pyvxl
console_scripts = []  # pylint: disable=C0103
warnings = []  # pylint: disable=C0103

from pyvxl import __program__
console_scripts.append(__program__ + " = pyvxl:main")
#
# Create scripts
setup(

    name='pyvxl',
    version='0.1.0',

    description=("A python interface to the vector vxlapi.dll for CAN communication."),
    author="Chris Cerovec",
    author_email="chris.cerovec@gmail.com",

    packages=find_packages(),
    package_data={'pyvxl': ['*.dbc']},

    entry_points={'console_scripts': console_scripts},

    install_requires=["colorama >= 0.2.7",
                      "ply >= 3.4"],
)

# Show warnings
if warnings:
    print '\n' + '\n'.join(warnings)