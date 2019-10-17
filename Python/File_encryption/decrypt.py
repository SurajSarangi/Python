"""Decrypting a line of text using Caesar cipher and distance value"""
s=input("Enter a line of text:\n")
s=s.lower()
d=int(input("Enter distance value:\n"))
s2=""
for i in s:
	j=ord(i)-d
	if j<ord('a'):
		k=ord('a')-j
		j=ord('z')-k+1
	s2=s2+chr(j)
print('Decrypted: ',s2)