"""Conerting decimal to octal"""
i=int(input("Enter a decimal:\n"))
o=''
while(i>0):
	o=str(i%8)+o
	i=i//8
print("Octal: ",o)