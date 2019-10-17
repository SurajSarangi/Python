t=int(input())
while(t>0):
    k=0
    n=int(input())
    d=[0 for i in range(0 , n)]
    a=[]
    c=[int (n) for n in input().split(' ')]
    h=[int (n) for n in input().split(' ')]
    for i in range(0,n):
        l=i-c[i]
        r=i+c[i]
        if(l<0):
            l=0
        d[l]=d[l]+1
        if(r<n-1):
            d[r+1]=d[r+1]-1
    for i in range(0,n):
        if(i==0):
            a.append(d[i])
        else:
            a.append(d[i]+a[i-1])
    a.sort()
    h.sort()
    for i in range(0,n):
        if(a[i]!=h[i]):
            k=1
            break
    if(k==0):
        print("YES")
    else:
        print("NO")
    

    t=t-1