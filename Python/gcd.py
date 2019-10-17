"""Calculating GCD of 2 numbers using Euclid's Algorithm"""
def gcd(a,b):
	if b==0:
		return a
	elif a==0:
		return b
	elif a>b:
		print("GCD of {} and {}".format(b,a%b))
		return gcd(b,a%b)
	else:
		print("GCD of {} and {}".format(b%a,a))
		return gcd(b%a,a)

a=eval(input("Enter 1st number:\n"))
b=eval(input("Enter 2nd number:\n"))
if a==0 or b==0:
	print('Zero is invalid')
else:
	k=gcd(a,b)
	print("GCD of {} and {} : {}".format(a,b,k))