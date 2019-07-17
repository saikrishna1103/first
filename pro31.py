s=int(input())
d=list(map(int,input().split()))
b=int(len(d)/2)
if sum(d[:b])//len(d[:b]) == sum(d[b:])//len(d[b:]):
    print("yes")
else:
        print("no")
