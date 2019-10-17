"""Displaying salary in tabular format depending on years of experience"""
s=eval(input("Enter starting salary:\n"))
p=eval(input("Enter percentage increase:\n"))
y=eval(input("Enter number of years:\n"))
print("{0:<8} | {1:<8}".format("Years:","Salary:"))
for i in range (1,y+1):
	s+=(p/100)*s
	print("{0:>8} | {1:^.2f}".format(i,s))