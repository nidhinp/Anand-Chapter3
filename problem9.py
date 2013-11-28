""" Write a regular expression to validate a phone number.
"""

import re

def phone_number(sentance):
	ptn = r'\d+'
	match = re.search(ptn, sentance)
	if match:
		print match.group()
	

s = 'this is my phone number 9400893961'
phone_number(s)
