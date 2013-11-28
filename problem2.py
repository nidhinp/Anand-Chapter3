""" Write a program to count number of files for each extension in the given directory.
    The program should take a directory name as argument and print count and extension
    for each available file extension.
"""

import sys
from os import listdir
from os.path import isfile, join

def extcount(mypath):
	a = {}
	for x in [f.split('.')[1] for f in listdir(mypath) if isfile(join(mypath, f))]:
		a[x] = a.get(x, 0) + 1
	for key, value in a.items():
		print key, value

if len(sys.argv) < 2:
	print 'usage: extcount_3_2.py path'
else:
	extcount(sys.argv[1])
