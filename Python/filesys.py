"""To navigate through files of a directory and access the contents"""

import os, os.path
q='7'
c=('1','2','3','4','5','6','7')
m="""1. List current directory
2. Move up
3. Move down
4. Number of files in the directory
5. Size of directory in bytes
6. Search for filename and display contents
7. Quit"""
def main():
 	while True:
 		print(os.getcwd())
 		print(m)
 		command=acceptCommand()
 		runCommand(command)
 		if command==q:
 			print("Bye Bye")
	 			break

def acceptCommand():
	print("Enter a number:\n")
	while True:
		co=input()
		if co not in c:
			print("Command not recognised!\nEnter again:\n")
		else:
			return co

def runCommand(command):
	if command=='1':
		listDir(os.getcwd())
	elif command=='2':
		moveUp()
	elif command=='3':
		moveDown(os.getcwd())
	elif command=='4':
		print("No. of files:",countFiles(os.getcwd()))
	elif command=='5':
		print("Size of directory:",sizeDir(os.getcwd()))
	elif command=='6':
		findfile(os.getcwd())

def listDir(dir):
	l=os.listdir(dir)
	for i in l:
		print(i)

def moveUp():
	os.chdir('..')

def moveDown(dir):
	while True:
		t=input("Enter name of directory:\n")
		if os.path.exists(dir + os.sep + t) and os.path.isdir(t):
			os.chdir(t)
			break
		else:
			k=input("Invalid Name\nWould you like to try again?(y/n)\n")
			if k=='n':
				break

def countFiles(dir):
	c=0
	l=os.listdir(dir)
	for i in l:
		if os.path.isfile(i):
			c+=1
		else:
			os.chdir(i)
			c+=countFiles(os.getcwd())
			os.chdir('..')
	return c

def sizeDir(dir):
	c=0
	l=os.listdir(dir)
	for i in l:
		if os.path.isfile(i):
			c+=os.path.getsize(i)
		else:
			os.chdir(i)
			c+=countFiles(os.getcwd())
			os.chdir('..')
	return c	

def findfile(dir):
	try:
		t=input("Enter string to search with extension:\n")
		f=open(t,'r')
		m=f.read()
		print(m)
	except:
		k=input("File not found!\nWould you like to try again?(y/n)\n")
		if(k=='y'):
			findfile(os.getcwd())
		else:
			return
main()