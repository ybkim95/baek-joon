import sys

N, K = list(map(int, sys.stdin.readline().rsplit()))

knapsack = [ list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]
knapsack.sort()

value = 0
i = 0
while K > 0:
    value += knapsack[i][1]
    K -= knapsack[i][0]
    i += 1

print(value)

