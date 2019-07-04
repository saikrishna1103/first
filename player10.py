n,k=map(list,input().split())
cou=0
if(len(n)==len(k)):
    for i in range(0,len(n)):
        if(n[i]==k[i]):
            continue
        else:
            cou=cou+1
if(cou==1):
    print("yes")
else:
    print("no")
