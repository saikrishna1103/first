num1,num2=map(int,input().split())
a=[]
for j in range(num1+1,num2+1):
  if j>1:
    for v in range(2,j):
      if(j%v==0):
        break
    else:
      a.append(v)
print(len(a)+1)
