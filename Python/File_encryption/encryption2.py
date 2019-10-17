"""Encrypting a file in a different way using bit string and shift"""

f1=open("input.txt",'r')
f2=open("output2.txt",'w')
for m in f1:
	s=''
	for i in m:
		if i==' ':
			s=s[-1]+s[:-1]+' '
			f2.write(s)
		elif i=='.':
			f2.write('.')
		elif i=='\n':
			f2.write('\n')
		elif ord(i)>=65 and ord(i)<=90:
			j=ord(i)+1
			if j>ord('Z'):
				j=ord('A')
			e=bin(j)
			s=s+e[2:]
		else:
			j=ord(i)+1
			if(j>ord('z')):
				j=ord('a')
			e=bin(j)
			s=s+e[2:]
f1.close()
f2.close()