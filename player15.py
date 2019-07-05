n=str(input())
s={}

for i in n:
    if i not in s.keys():
        s[i]=n.count(i)
print(max(s, key=s.get))
