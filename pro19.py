k=int(input())
m=[]
while(k):
    m+=list(map(int,input().split()))
    k-=1 
m=sorted(m)
print(*m)
