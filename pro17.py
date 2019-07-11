z,q=map(int,input().split())
l=list(map(int,input().split()))
f=0
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if(l[i]+l[j]==q):
            f=1 
            break
    if(f==1):
        break
if(f==0):
    print("no")
else:
    print("yes")
