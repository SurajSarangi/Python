"""To write a recursive function that takes path as input and displays name if it is a file 
or the name of the files if it is a directory"""

import os, os.path

def patho(dir):
	l=os.listdir(dir)
	for i in l:
		if os.path.isfile(i):
			print(i)
		else:
			patho(i)
patho(os.getcwd())