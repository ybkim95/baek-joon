import sys

def DFS(map,x,y):
    global num_danji
    visited[x][y] = True

    if map[x][y] == 1:
        num_danji += 1
    
    for i in range(4):
        x += dx[i]
        y += dy[i]
        if (0 <= x < n and 0 <= y < n) and (visited[x][y] and map[x][y] == 1):
            DFS(map,x,y)


N = int(sys.stdin.readline().rstrip())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

map = [list(map(int, sys.stdin.readline().rsplit()) for _ in range(N))
visited = [[False]*N for _ in range(N)]
num_danji = 0





