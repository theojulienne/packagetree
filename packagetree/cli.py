"""
Package Tree

Usage:
  packagetree [--dryrun] [--dest-dir=<path>] [--iteration=<iteration>] <file>

Options:
  --dryrun                Don't actually generate the packages, just output some details about what would be run.
  --dest-dir=<path>       Destination directory for created packages. If not specified, defaults to '.'.
  --iteration=<iteration> Specify a default iteration, otherwise none specified.
"""

from docopt import docopt

import yaml
import tempfile
import sys
import os
import subprocess

def create_package(package, spec, cli):
	print package
	print '  Version:', spec['version']

	cmd = [
		'fpm',
		'-s', 'empty',
		'-t', 'deb',
		'-n', package,
		'-v', spec['version'],
	]

	if cli['--iteration'] is not None:
		cmd.append('--iteration')
		cmd.append(cli['--iteration'])

	print '  Dependencies:'
	for dep in spec['dependencies']:
		print '   ', dep

		cmd.append('-d')
		cmd.append('%s' % dep)

	if cli['--dryrun']:
		print '  Command:', ' '.join(cmd)
	else:
		subprocess.call(cmd)
	
	print

def main():
	arguments = docopt(__doc__, version='Package Tree v0.1')
	
	f = open(arguments['<file>'], 'rb')
	tree = yaml.load(f.read())
	f.close()

	if not arguments['--dryrun']:
		if os.system('which fpm >/dev/null') != 0:
			sys.stderr.write('FPM could not be found, is it installed? If not, try \'gem install fpm\'\n')
			sys.exit(1)

		if arguments['--dest-dir'] is not None:
			dest = arguments['--dest-dir']
			if not os.path.exists(dest):
				os.makedirs(dest)
			os.chdir(dest)

	for package,spec in tree.iteritems():
		create_package(package, spec, arguments)