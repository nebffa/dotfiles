#!/usr/bin/python3

"""Installs Ben Lucato's dotfiles."
"""


import os
import sys
import glob
import shutil


def get_dotfiles(dirname):
	ignore = ['.gitignore', '.git']
	return [filename for filename in glob.glob('{0}/.[A-Za-z]*'.format(dirname) if filename not in ignore)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise RuntimeError('USAGE: python install.py TARGET_OS_NAME')

	target_os = sys.argv[1]

	os_agnostic_dotfiles = get_dotfiles('.')
	os_specific_dotfiles = get_dotfiles(target_os)

	for dotfile in os_agnostic_dotfiles:
		shutil.copy(dotfile, os.path.expanduser('~'))
