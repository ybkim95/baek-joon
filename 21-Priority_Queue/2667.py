import sys

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    
    return visited

N = int(sys.stdin.readline().rstrip())

danji = {}
temp = [list(sys.stdin.readline().rsplit()) for _ in range(N)]

for i in range(N-1):
    for j in range(N-1):
        if temp[i][j+1] == '1':
            if (i,j) not in danji:
                danji[(i,j)] = (i,j+1)
            elif (i,j+1) not in danji[(i,j)]:
                danji[(i,j)].append((i,j+1))

            if (i,j+1) not in danji:
                danji[(i,j+1)] = (i,j)
            elif (i,j) not in danji[(i,j+1)]:
                danji[(i,j+1)].append((i,j))

        elif temp[i+1][j] == '1':
            if (i,j) not in danji:
                danji[(i,j)] = (i+1,j)
            elif (i+1,j) not in danji[(i,j)]:
                danji[(i,j)].append((i+1,j))

            if (i+1,j) not in danji:
                danji[(i+1,j)] = (i,j)
            elif (i,j) not in danji[(i+1,j)]:
                danji[(i+1,j)].append((i,j))

for i in range(N):
    for j in range(N):
        







                