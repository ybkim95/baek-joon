import sys

s1 = list(str(sys.stdin.readline().rstrip()))
s2 = list(str(sys.stdin.readline().rstrip()))

# print(s1,s2)

l1 = len(s1)
l2 = len(s2)

dp = [[0]*(l2+1) for _ in range(l1+1)]

for i in range(1,l1+1):
    for j in range(1,l2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max( dp[i-1][j], dp[i][j-1] )

print(dp[-1][-1])

