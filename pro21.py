z=input()
for i in range(1,len(z)):
    if ord(z[i])>ord(z[0]):
        anse=z[i:]
        break
print(anse)
