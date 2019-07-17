z=int(input())
q=list(map(int,input().split()))
s=0
t=0
for i in range(z):
	if i%2==0:
		s=s+q[i]
	else:
		t+=q[i]
print(max(s,t))
