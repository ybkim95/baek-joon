import sys

M,N = map(int, sys.stdin.readline().rsplit())
map = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(M)]
trace = [[-1]*N for _ in range(M)]

dx = [0, 0, -1, 1] # 상 하 좌 우
dy = [-1, 1, 0, 0]

def dfs(x,y):
    # 마지막 
    if x == M-1 and y == N-1:
        return 1
    # 이미 방문한 적이 있는 곳
    if trace[x][y] != -1:
        return trace[x][y]
    # 방문한 적이 없는 곳
    trace[x][y] = 0
    for i in range(len(dx)):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if 0 <= x < M and 0 <= y < N:
            if map[n_x][n_y] < map[x][y]:
                trace[x][y] += dfs(n_x,n_y)
    return trace[x][y]

print(dfs(0,0))