import sys

N = int(sys.stdin.readline().rstrip())

# Example
"""
N = 1 -> 1
N = 2 -> 11 00
N = 3 -> 111 001 100
N = 4 -> 1111 0000 0011 1100 1001
N = 5 -> 11111 00001 10000 00100 10011 00111 11100 11001
"""

dp = [0]*1000001

if N == 1:
    print(1)
    exit()

else:
    dp[1] = 1
    dp[2] = 2

    for n in range(3,N+1):
        dp[n] = (dp[n-2] + dp[n-1]) % 15746

    print(dp[N])
