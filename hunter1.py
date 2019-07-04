num = int(input())
lis = list(map(int,input().split()))
lis.sort()
z = []
for i in range(len(lis)-1):
    if lis[i]==lis[i+1]:
        z.append(lis[i])
if z:
    for x in  set(z):
        print(x,end=" ")
else:
    print("unique")
