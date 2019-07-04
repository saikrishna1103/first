s1,s2=map(str,input().split())
if(len(s1)!=len(s2)):
    print("no")
x=[s1.count(j) for j in s1]
y=[s2.count(j) for j in s2]

if(x==y):
    print("yes")
else:
    print("no")
