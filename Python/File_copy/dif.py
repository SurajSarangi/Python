"""To compare the lines of each file and see if they are same"""

s1=input("Enter name of first file with extension:\n")
s2=input("Enter name of second file with extension:\n")
f1=open(s1,'r')
f2=open(s2,'r')
l1=f1.readline()
l2=f2.readline()
while l1!='' and l2!='':
	if l1!=l2:
		print('No')
		break
	l1=f1.readline()
	l2=f2.readline()
if l1=='' and l2=='':
	print('Yes')