x,y=map(str,input().split())
t=abs(len(x)-len(y))
for j in range(len(x)):
    if(len(y)==1 and y[j] in x):
        break
    if(x[j]!=y[j]):
        t=t+1
print(t)
