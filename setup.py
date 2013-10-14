#!/usr/bin/env python
"""
=====
cmmap
=====

Simple CFFI wrapper around mmap.
"""
from setuptools import setup, find_packages

setup(
  name="cmmap",
  version="0.0.1",
  py_modules = ['cmmap'],
  tests_require=['nose'],
  test_suite='nose.collector',

  author='Michel Pelletier',
  author_email='pelletier.michel@yahoo.com',
  description='mmap cffi wrapper',
  long_description=__doc__,
  license='BSD',
  url='https://github.com/michelp/pyczmq',
      install_requires=[
        'cffi',
        ],
)
