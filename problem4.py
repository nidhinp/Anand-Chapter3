import sys
from os import listdir
from os.path import isfile, join


def dirtree(path):
	for content in listdir(path):
		if isfile(join(path, content)):
			print '|--', content
		else:
			dirtree(join(path, content))

if len(sys.argv) < 2:
	print 'usage: python problem4.py path'
else:
	dirtree(sys.argv[1])

