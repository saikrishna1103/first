from itertools import permutations
n=input("")
s=permutations(n)
for i in list(s):
    print("".join(i))
