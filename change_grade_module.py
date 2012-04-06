#!/usr/bin/python

import re
import fileinput
from sys import stderr,stdout,argv,exit

arg1 = argv[1]
arg2 = argv[2]

def change_grade():
	if len(argv) != 3:
		    stderr.write("Usage: change_grade.py  STRING\n")
		    exit(1)
		    
		for line in fileinput.input('-'):
		 	m = re.search(argv[1], line)
		 	values = line.rstrip().rsplit(',') #note that split accepts an optional parameter to define what character the string is split on. If none is provided it defaults to any whitespace character  	
			if m:
		       		values[3] = argv[2]
				print ",".join(values)	
			else:
				print line	

## This should be a module later on
def main():
	change_grade()	


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

#change_grade should take three parameters for the search string grade and file. The arguments should be read in
#the __main__ block and then passed into change_grade.