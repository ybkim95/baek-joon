import sys

N = int(sys.stdin.readline().rstrip())

dp = [[0]*10 for _ in range(N+1)] # 각 자리수 숫자 별 0~9까지 사용된 빈도수를 체크하기 위함
for j in range(1,10):
    dp[1][j] = 1 

for i in range(2, N+1):
    for j in range(10): # 0-9까지의 수 
        if j == 0: # 끝자리가 0인 경우는 N-1번째 자리수에서 끝자리가 1로 사용된 경우와 같다. (trivial)
            dp[i][j] = dp[i-1][1]
        elif j == 9: # 끝자리가 9인 경우는 N-1번째 자리수에서 끝자리가 8로 사용된 경우와 같다. (trivial)
            dp[i][j] = dp[i-1][8]        
        else: # 그 외의 경우는 N-1번째 자리수에서 끝자리가 j-1 혹은 j+1로 사용된 경우와 같다. (trivial)
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)
