import sys

N = int(sys.stdin.readline().strip())

road_len = list(map(int, sys.stdin.readline().split()))
unit_cost = list(map(int, sys.stdin.readline().split()))

ans = road_len[0]*unit_cost[0]
length = 0
target = unit_cost[0]

# Ex
#  2 3 1
# 5 2 4 1

for i in range(1, N-1):
    if unit_cost[i] < target:
        ans += target*length
        target = unit_cost[i]
        length = road_len[i] # length를 정해주는게 제일 중요
    else:
        length += road_len[i]
    
    if i == N-2:
        ans += target * length 

print(ans)
