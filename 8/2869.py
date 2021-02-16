import sys

A, B, V = list(map(int, sys.stdin.readline().rsplit()))

# 2 1 5                -> 4 (2 + 1 * 3)
# 5 1 6                -> 2 (5 + 4 * 1)
# 100 99 1000000000    -> 999999901 (100 + 1 * 999999900)

if (A >= V):
    cnt = 0
else:
    cnt = 1

res = V-A

if (A-B) >= res:
    cnt += 1
else:
    if res % (A-B) == 0:
        cnt += res // (A-B)
    else:
        cnt += (res // (A-B)) +1

print(cnt)