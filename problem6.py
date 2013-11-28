""" Write a program that takes a URL as argument, downloads the html from web
    and print it after striping html tags.
"""

import sys
import re
import urllib

def antihtml(url):
	response = urllib.urlopen(url)
	content = response.read()
	tags = re.compile(r'<[^>]+>')
	cleantext = re.sub(tags, '', content)
	print cleantext		

if len(sys.argv) < 2:
	print 'usage python problem6.py url'
else:
	antihtml(sys.argv[1])
