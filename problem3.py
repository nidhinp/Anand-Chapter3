""" Write a program to list all files in the given directory along with their
    length and last modification time. The output should contain one line for
    each file containing filename, length, and modification date separated by 
    tabs.
"""

import sys
import datetime
from os import listdir
from os.path import isfile, join, getmtime, getsize

def file_details(path):
	for x in [f for f in listdir(path) if isfile(join(path, f))]:
		print x, '\t',getsize(x), '\t', datetime.datetime.fromtimestamp(getmtime(x)).strftime('%Y-%m-%d %H:%M:%S')

if len(sys.argv) < 2:
	print 'usage: python problem3 path'
else:
	file_details(sys.argv[1])
