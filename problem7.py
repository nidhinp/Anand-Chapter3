""" Write a function make_slug that takes a name converts it into a slug.
    A slug is a string where spaces and special charactes are replaces by 
    a hyphen, typically used to create blog post URL from post title. It 
    should also make sure there are no more than one hyphen in any place
    and there are no hyphen at the beginning and end of the slug.
"""

import re

def make_slug(word):
	slug = re.sub(r'[\s!]', '-', word)
	modified_slug = re.sub(r'-+', '-', slug)
        space = re.sub(r'-', ' ',modified_slug)
        print re.sub(r'\s', '-',space.strip())	

make_slug("hello world")
make_slug("hello world!")
make_slug("  --hello-  world--")

