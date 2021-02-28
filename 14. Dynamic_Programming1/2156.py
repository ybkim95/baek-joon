import sys

# 계단 문제와 유사

N = int(sys.stdin.readline().rstrip())
wine = [0] + [int(sys.stdin.readline().rstrip()) for _ in range(N)]
dp = [0]*(N+1)

for i in range(1,N+1):
    if i == 1:
        dp[i] = wine[i]
    elif i == 2:
        dp[i] = wine[i] + wine[i-1]
    else:
        # Case 1. OXOO | <- i번쨰 
        # Case 2.  OXO | <- i번쨰
        # Case 3.    X | <- i번쨰
        dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i], dp[i-1])

print(dp[N])
