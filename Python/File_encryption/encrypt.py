"""Encrypting a line of text using Caesar cipher and distance value"""
s=input("Enter a line of text:\n")
s=s.lower()
d=int(input("Enter distance value:\n"))
s2=""
for i in s:
	j=ord(i)+d
	if(j>ord('z')):
		k=j-ord('z')
		j=ord('a')+k-1
	s2=s2+chr(j)
print("Encrypted: ",s2)