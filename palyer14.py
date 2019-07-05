s=int(input())
v=input()[::-1]
vow=('a','e','i','o','u','A','E','I','O','U')
for i in v:
  if i in vow:
    v=v.replace(i,"")
print(v,end="")
