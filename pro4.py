t,r=map(str,input().split())
y=0
if len(t)>len(r):
	t,r=r,t
p=0
while p<len(t):
	  y+=(ord(r[p])-ord(t[p]))
	  p+=1
for p in range(p,len(r)):
	  y+=ord(r[p])-ord('a')+1
print(y)
