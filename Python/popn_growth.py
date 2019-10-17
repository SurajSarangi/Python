"""To calculate the growth of microorganisms taking the initial number,
growth rate and growth period and number of hours"""
i=eval(input("Enter initial number of microorganisms:\n"))
g=eval(input("Enter growth rate:\n"))
t=eval(input("Enter growth period:\n"))
h=eval(input("Enter number of hours:\n"))
for j in range(0,h,t):
	i*=g
print("Population after {} hours:{}".format(h,i))