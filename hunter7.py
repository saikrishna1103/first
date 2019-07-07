nani=int(input(""))
l=list(map(int,input("").split()))
m=[]
for i in range(len(l)):
    if(i%2==0 and l[i]%2!=0 or i%2!=0 and l[i]%2==0 ):
    	m.append(l[i])
       
for i in m:
    print(i,end=" ")
