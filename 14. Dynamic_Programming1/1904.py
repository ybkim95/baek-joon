import sys
from itertools import product

N = int(sys.stdin.readline().rstrip())

# "00" 혹은 "1"을 조합해서 만들 수 있다

# arr = {1: 2, 2: 2, 3: 2, 4: 5}

# if N in arr:
#     ans = arr[N]
# else:



# print(ans % 15746)

a = ["1", "0"]
res = []
for i in product(a, repeat=N):
    res.append("".join(list(i)))

for r in res:
    if '010' not in r and '101' not in r:
        print(r)

         