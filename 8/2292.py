import sys

def f(n):
    return 3*(n**2) + 3*n + 1

n = int(sys.stdin.readline().rstrip())

# 1
# 6
# 12
# 18
# 24
# 일반항은 6(n-1) + 1 -> S_n = n(6+6n) / 2 => S_n = 3n^2 + 3n + 1 (n >= 1)

if n == 1:
    print(1)
else:
    cnt = 0
    while True:
        if f(cnt) < n < f(cnt+1):
            print(cnt+2)
            break
        elif f(cnt) == n:
            print(cnt+1)
            break
        else:
            cnt += 1

