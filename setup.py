#!/usr/bin/env python

from distutils.core import setup

setup(
	name='Package Tree',
	version='0.1',
	description='Utility to convert a YAML-formatted package dependency tree into .deb metapackages using FPM',
	author='Theo Julienne',
	author_email='theo.julienne@gmail.com',
	url='https://github.com/theojulienne/packagetree',
	packages=['packagetree'],
	install_requires=['docopt', 'pyyaml'],
	entry_points = {
		'console_scripts': ['packagetree=packagetree.cli:main'],
	}
)
