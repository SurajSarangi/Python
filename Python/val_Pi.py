"""Calculatinng value of Pi using Gottfried Leibniz"""
t=eval(input("Enter number of terms\n"))
k=1
for i in range(1,t):
    if i%2==0:
        k=k+1/(2*i+1)
    else:
        k=k-1/(2*i+1)
print("Value of Pi: ",4*k)