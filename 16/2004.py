import sys

n,m = map(int, sys.stdin.readline().split())

def cnt(n,k):
    ans = 0
    while n != 0:
        n = n // k
        ans += n
    return ans

if m == 0:
    print(0)
    exit()
else:
    print(min(cnt(n,2) - cnt(m,2) - cnt(n-m,2), cnt(n,5) - cnt(m,5) - cnt(n-m,5)))
