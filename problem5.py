import sys
import urllib

def get_basename(url):
	if url[-1] == '/':
		return 'index.html'
	else:
		return url.split('/')[-1]

def wget(url):
	basename = get_basename(url)
	response = urllib.urlopen(url)
	print 'saving %s as %s' %(url, basename)
	content = response.read()
	f = open(basename, 'w')
	f.write(content)
	f.close()
	

if len(sys.argv) < 2:
	print 'usage: wget_5.py url'
else:
	wget(sys.argv[1])
