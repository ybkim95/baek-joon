import sys

# 0-1 knapsack problem

N,K = map(int, sys.stdin.readline().rsplit()) # Number of items, Weight Limit

W=[0]
V=[0]

for _ in range(N):
    w,v = map(int, sys.stdin.readline().rsplit()) # (weight,value) pair
    W.append(w)
    V.append(v)

def Knapsack1(num_item,capacity): # 시간 초과
    if capacity == 0 or num_item == 0:
        return 0
    elif W[num_item] > capacity:
        return Knapsack1(num_item-1, capacity)
    else:
        return max( V[num_item-1] + Knapsack1(num_item-1, capacity-W[num_item]), Knapsack1(num_item-1, capacity) ) 

def Knapsack2(n,c):
    dp = [[0]*(c+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(c,0,-1):
            if w >= W[i]:
                dp[i][w] = max( V[i] + dp[i-1][w-W[i]], dp[i-1][w] )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][c]

print(Knapsack2(N,K))