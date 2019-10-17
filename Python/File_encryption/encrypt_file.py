"""Encrypting an entire file"""

f1=open("input.txt",'r')
f2=open("output.txt",'w')

for m in f1:
	for i in m:
		if i==' ':
			f2.write(' ')
		elif i=='.':
			f2.write('.')
		elif i=='\n':
			f2.write('\n')
		elif ord(i)>=65 and ord(i)<=90:
			j=ord(i)+5
			if j>ord('Z'):
				k=j-ord('Z')
				j=ord('A')+k-1
			f2.write(chr(j))
		else:
			j=ord(i)+5
			if(j>ord('z')):
				k=j-ord('z')
				j=ord('a')+k-1
			f2.write(chr(j))
f1.close()
f2.close()