"""Converting octal to decimal"""
o=int(input("Enter an octal:\n"))
(k,i)=(0,0)
while(o>0):
	d=o%10
	i+=d*(8**k)
	k+=1
	o//=10
print("Integer: ",i)