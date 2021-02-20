import sys

N, M = list(map(int, sys.stdin.readline().rsplit()))

M1 = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]

M, K = list(map(int, sys.stdin.readline().rsplit()))

M2 = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]

res = [[0]*K]*N

for i in range(N):
    for j in range(K):
        res[i][j] = M1[i][j] * M2[j][]