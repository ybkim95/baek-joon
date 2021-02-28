import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rsplit()))
dp = [arr[0]] + [0]*(N-1)
# print("arr:",arr)

for i in range(1,N):
    dp[i] = max(arr[i]+dp[i-1], arr[i]) # 부모가 부자면 양도를 받고, 빚이 있으면 과감히 버리고 새출발하는 느낌
# print("dp: ",dp)

print(max(dp))


        
