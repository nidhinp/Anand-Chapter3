import sys
import re
import urllib

def antihtml(url):
	response = urllib.urlopen(url)
	content = response.read()
	

if len(sys.argv) < 2:
	print 'usage python problem6.py url'
else:
	antihtml(sys.argv[1])
