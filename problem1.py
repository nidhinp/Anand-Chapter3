""" Write a program to list all files in the given directory.
"""

from os import listdir
from os.path import isfile, join
import sys

def list_files(mypath):
	for x in [f for f in listdir(mypath) if isfile(join(mypath, f))]:
		print x

if len(sys.argv) < 2:
	print 'usage: problem1.py path'
else:
	list_files(sys.argv[1]) 
