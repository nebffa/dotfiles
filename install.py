#!/usr/bin/python3

"""Installs Ben Lucato's dotfiles."
"""


import os
import sys
import glob
import shutil


def get_dotfiles(dirname):
	return glob.glob('{0}/.[A-Za-z]*'.format(dirname))


if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise RuntimeError('USAGE: python install.py')

	target_os = sys.argv[1]
	home_dir = os.path.expanduser('~')

	script_location = os.path.dirname(os.path.realpath(__file__))
	os_agnostic_dotfiles = get_dotfiles(script_location)
	os_specific_dotfiles = get_dotfiles(os.path.join(script_location, target_os))

	for dotfile in os_specific_dotfiles:
		shutil.copy(dotfile, home_dir)		
