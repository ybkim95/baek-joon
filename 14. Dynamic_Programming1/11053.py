import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rsplit()))

# dp[i]는 i번째 항목 이전에 최대 길이의 부분 수열값 + 1을 의미 
dp = [0]*N # 초기화

for i in range(N):
    target = A[i] # 이 값을 중심으로 하여 대조군 A[j]와 비교할 예정
    for j in range(i):
        if A[j] < target and dp[i] < dp[j]: # 현재 위치에서 볼때, 이전의 어떤 위치 j에 대해 현재의 값 A[i]가 A[j]보다 크면 일단 기본 조건을 충족 시킨 것이므로 dp[i] < dp[j]라면 흡수하는 느낌
            dp[i] = dp[j]
    dp[i] += 1 # 본인이 더해질 것이므로

print(max(dp))


