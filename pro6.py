t = int(input())
l = list(map(int,input().split()))
count = 0
for i in range(t):
    for j in range(i,t):  
        for k in range(j,t):
            if l[i]<l[j]<l[k]:
                count+=1
print(count)
