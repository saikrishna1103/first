f=[]
y=int(input())
a=list(map(int,input().split()))[:y] 
for i in range(0,y):
    if (a[i]==i):
        f.append(a[i])
        f.sort()
if(len(f)>0):
    print(*f,sep=" ")
else:
    print(-1)
