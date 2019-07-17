z = int(input())
q = [ int(x) for x in input().split()]
z = len(q)
u1 = 0
for i in range(0,z-2):
    for j in range(i+1, z-1):
        for k in range(j+1, z):
            if q[i] > q[j] > q[k] :
                u1 =u1+ 1
print(u1)
