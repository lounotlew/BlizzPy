import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import setup


CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

if CURRENT_PYTHON < REQUIRED_PYTHON:
	sys.stderr.write("Your current version of Python is not supported. Please install or update to Python 3.6 or higher.")


setup(
	name='BlizzPy',
	version="1.0.0",
	python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
	url='https://github.com/lounotlew/BlizzPy',
	author='Lewis Kim',
	author_email='lewis.k@berkeley.edu',
	description="A comprehensive open-source API wrapper library for Blizzard's REST API. Currently supports WoW, SC2, and Diablo 3 game data.",
	license='Apache2',
	classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3'
	],
	packages=['blizzpy'],
	install_requires=[
	'pandas>=0.23.0'
	]
	)

