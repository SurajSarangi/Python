"""To copy contents of one file to the other"""

s1=input("Enter name of first file with extension:\n")
s2=input("Enter name of second file with extension:\n")
f1=open(s1,'r')
f2=open(s2,'w')
for m in f1:
	f2.write(m)