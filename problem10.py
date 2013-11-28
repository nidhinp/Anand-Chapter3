""" Write a program to print the external IP address of the machine.
    Use the response from http://httpbin.org/get and read the IP
    address from there. The program should print only the IP address
    nothing else.
"""

import urllib
import re

def ip(url):
	response = urllib.urlopen(url)
	content = response.read()
	match = re.search(r'\d+.\d+.\d+.\d+', content)
	if match:
		print match.group()

ip('http://httpbin.org/get')
