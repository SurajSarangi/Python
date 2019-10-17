# cook your dish here

def getParity( n ):
    return (bin(n).count("1"))%2

t=int(input())
while(t>0):
    A=set()
    (ce,co)=(0,0)
    q=int(input())
    for i in range(0,q):
        p=int(input())
        if(i==0):
            A.add(p)
            x=getParity(p)
            if(x==0):
                ce=ce+1
            else:
                co=co+1
        else:
            l0=len(A)
            A.add(p)
            l1=len(A)
            if((l1-l0)>0):
                x=getParity(p)
                if(x==0):
                    ce=ce+1
                else:
                    co=co+1
                for j in A.copy():
                    r=j^p
                    if(r!=0):
                        A.add(r)
                        l2=len(A)
                        if((l2-l1)>0):
                            x=getParity(r)
                            if(x==0):
                                ce=ce+1
                            else:
                                co=co+1 
        print(ce," ",co)
    t=t-1
