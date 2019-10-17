"""To print all the words and their frequecies of a text in alphabetical order"""
s1=input("Enter file name:\n")
f1=open(s1,'r')
(l,s)=([],'')
m=f1.read()
for i in m:
	if i==',':
		pass
	elif i==' ' or i=='.':
		l.append(s.lower())
		s=''
	else:
		s=s+i
l.sort()
k=set(l)
print("{0:20} | {1:12}".format("Word:","Frequency:"))
for i in k:
	c=0
	for j in l:
		if i==j:
			c+=1
	print("{0:20} | {1:4}".format(i,c))