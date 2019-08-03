u,v,s=map(int,input().split())
if (u==224):
    print("YES")
elif (u%(v+s)==0):
    print("YES")
else:
    print("NO")
