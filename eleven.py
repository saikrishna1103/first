s,a = map(int,input().split())
power = 1
i = 1

while(i <= a):
    power = power * s
    i = i + 1
print(power)
