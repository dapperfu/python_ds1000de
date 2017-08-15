# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='ds1000de',
      version='0.1',
      description='Python module for controlling Rigol DS1000D/E through PyVISA',
      url='https://github.com/jed-frey/python-ds1000de',
      author='Jed Frey',
      license='BSD',
      packages=['ds1000de'],
      setup_requires=[
              'pytest-runner',
              'pyvisa',
              ],
      tests_require=[
              'pytest',
              'pytest-html',
              'pytest-flake8',
              ],
      zip_safe=False,
      )
