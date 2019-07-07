sai = int(input())
lis = list(map(int,input().split()))
lis.sort()
a = []
for i in range(len(lis)-1):
    if lis[i]==lis[i+1]:
        a.append(lis[i])
        break
if a:
    for x in  set(a):
        print(x,end=" ")
else:
    print("unique")
