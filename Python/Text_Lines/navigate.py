"""Navigating through the lines of a text using a list"""
s=input("Enter file name with extension:\n")
f=open(s,'r')
(l,c)=([],0)
line=f.readline()
while line!='':
	c+=1
	l.append(line[:-1])           #to avoid the new line
	line=f.readline()
print("No. of lines: ",c)
if len(l)==0:
	print("File empty")
else:
	while True:
		n=int(input("Enter the line number:\n"))
		if n==0:
			break
		print('\n',l[n-1],'\n')