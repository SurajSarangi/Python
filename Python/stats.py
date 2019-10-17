"""To define a module having statistical functions like mean, median, mode of  list"""
def median(l):
	l.sort()
	n=len(l)
	if(n==0):
		return 0
	if n%2!=0:
		return l[(n//2)]
	else:
		k=(l[n//2-1]+l[n//2])/2
		return k

def mode(l):
	if len(l)==0:
		return 0
	d={}
	for i in l:
		n=d.get(i,None)
		if n==None:
			d[i]=1
		else:
			d[i]=n+1
	maxi=max(d.values())
	for j in d:
		if d[j]==maxi:
			return j
			break

def mean(l):
	if len(l)==0:
		return 0
	me=sum(l)/len(l)
	return me


l=[1,6,4,9,3,6,7,2,5,5,7,6]
print("List: ",l)
print("Mean: ",mean(l))
print("Median: ",median(l))
print("Mode: ",mode(l))