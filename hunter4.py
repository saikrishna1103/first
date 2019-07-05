num = int(input())
li = list(map(int,input().split()))[:num]
for i in range(num):
  if li.count(li[i])==1:
   print(li[i])
