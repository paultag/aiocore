#!/usr/bin/env python

from setuptools import setup
from aiocore import __version__

long_description = ""

setup(
    name="aiocore",
    version=__version__,
    packages=['aiocore',],
    author="Paul Tagliamonte",
    author_email="paultag@debian.org",
    long_description=long_description,
    description='does some stuff with things & stuff',
    license="Expat",
    url="",
    platforms=['any']
)
