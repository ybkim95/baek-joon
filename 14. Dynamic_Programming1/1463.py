import sys

N = int(sys.stdin.readline().rstrip())

dp = [0]*(N+1) # count list 역할을 함

for n in range(2,N+1):
    # 이건 모든 경우 다 해당되므로 조건문을 명시하지 않음
    dp[n] = dp[n-1]+1
    
    # n이 3으로 나뉘어 떨어지는 경우
    if n%3 == 0 and dp[n] > dp[n//3]+1: # <- 이미 위의 step을 적용한 dp[i]임에 주목!
        dp[n] = dp[n//3]+1

    # n이 2으로 나뉘어 떨어지는 경우
    if n%2 == 0 and dp[n] > dp[n//2]+1:
        dp[n] = dp[n//2]+1
    

# 여기까지 과연 min은 어디있는지 궁금할 것인데, 
# 만약 순서대로 나온 연산이 더 작은 값을 만들어낸 다면 다음 step으로 넘어가지 않을 것이기 때문에 유효함 (Ex. n-1 연산 -> n//3 연산)
print(dp[N])