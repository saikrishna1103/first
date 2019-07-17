import math
z = int(input())
res = int(math.pow( 2, round( math.log( z ) / math.log( 2 ) ) ))
if res == z:
    print(0)
else:
    print(z-res)
