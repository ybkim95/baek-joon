import sys

N = int(sys.stdin.readline().strip())
weight = list(map(int, sys.stdin.readline().split())) # 구술의 무게를 추정하기 위해 필요한 추들의 무게 list

M = int(sys.stdin.readline().strip())
check_list = list(map(int, sys.stdin.readline().split())) # 무게를 확인하고 싶은 구술들의 무게 list

dp = [0] * (N+1)

def knapsack(target, weight):
    for w in weight:
        if w < target:
            


    


for i in range(M):
    knapsack(check_list[i], weight)

