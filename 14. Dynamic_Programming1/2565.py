# 전깃줄 문제 - LIS 응용2

import sys

N = int(sys.stdin.readline().rstrip())
util_pole = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]

# dp[i]는 i번째 항목 이전에 최대 길이의 부분 수열값 + 1을 의미 
dp1 = [0]*N
dp2 = [0]*N 
dp  = [0]*N

for i in range(N):
    target = util_pole[i][1] # 이 값을 중심으로 하여 대조군 A[j]와 비교할 예정
    for j in range(i+1, N):
        if util_pole[j][1] < target and dp1[i] < dp1[j]: 
            dp1[i] = dp1[j]
    dp1[i] += 1 # 본인이 더해질 것이므로

for i in range(N-1, -1, -1):
    target = util_pole[i][1] # 이 값을 중심으로 하여 대조군 A[j]와 비교할 예정
    for j in range(i, -1, -1):
        if util_pole[j][1] < target and dp2[i] < dp2[j]: # 현재 위치에서 볼때, 이전의 어떤 위치 j에 대해 현재의 값 A[i]가 A[j]보다 작으면 일단 기본 조건을 충족 시킨 것이므로 dp[i] < dp[j]라면 흡수하는 느낌
            dp2[i] = dp2[j]
    dp2[i] += 1 # 본인이 더해질 것이므로

print(dp1, dp2)