sai=int(input(""))
n1=list(map(int,input().split()))
o=len(n1)
large=max(n1)
y,z=0,0
for i in range(0,o-1):
 for j in range(i+1,o):
  if abs(n1[i]+n1[j])< large:
   y,z=n1[i],n1[j]
   large=abs(y+z)
print(y, z)
