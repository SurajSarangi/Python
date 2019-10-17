"""To convert any representation to decimal"""
d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
n=input("Enter a number:\n")
b=int(input("Enter base:\n"))
(s,j)=(0,0)
for i in range (len(n)-1,-1,-1):
	s+=d[n[i]]*(b**j)
	j+=1
print("Decimal:\n",s)