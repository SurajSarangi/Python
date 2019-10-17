"""To print all the words of a text in alphabetical order"""
s1=input("Enter file name:\n")
f=open(s1,'r')
(k,s)=([],'')
m=f.read()
for i in m:
	if i==',':
		pass
	elif i==' ' or i=='.':
		k.append(s.lower())
		s=''
	else:
		s=s+i
k.sort()
l=set(k)
for i in l:
	print(i)