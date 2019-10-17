"""To see if a list is sorted or not"""
def isSorted(a):
	for i in range(0,len(a)-1):
		if a[i]>a[i+1]:
			return False
	return True

def main():
	l1=[1,2,3,4,5,6]
	l2=[1,3,2,4,6,5]
	print(isSorted(l1))
	print(isSorted(l2))

main()