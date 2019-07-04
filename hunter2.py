num = int(input())
lis = list(map(int,input().split()))
lis.sort(reverse = True)
t=0
for j in range(num):
  t=t*10+lis[j]
print(t) 
