#!/usr/bin/python
import json
import re
import sys

def main():
	sent_file = open(sys.argv[1])
	
	for line in sent_file: 
		res = re.search(r'^[A-Za-z0-9_@]*$', line)
		if res != None:
			print res.group()


if __name__ == '__main__':
	main()
