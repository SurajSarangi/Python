"""To take infinite inputs till an enter key"""
print("Enter numbers followed by space")
a=[eval(n) for n in input().split(' ')]
s=sum(a)
av=sum(a)/len(a)
print("Sum: %3.3f\nAverage: %3.3f"%(s,av))