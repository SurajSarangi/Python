"""To make a table for payment plan of a loan"""
p=eval(input("Enter purchase price:\n"))
print("Down payment: %5.2f"%(0.1*p))
p=p-0.1*p
pa=0.05*p
print("{0:^8} | {1:^10} | {2:^8} | {3:^8} | {4:^15} | {5:^10}".format("Month","Balance Owed","Interest","Principal","Monthly Payment","New Balance"))
t=1
while(p>0):
	i=p*0.01
	pr=pa-i
	bal=p-pa
	if(bal<=0):
		bal=0.00
	print("{0:^8} | {1:^12.2f} | {2:^8.2f} | {3:^9.2f} | {4:^15.2f} | {5:^10.2f}".format(t,p,i,pr,pa,bal))
	t=t+1
	p=bal