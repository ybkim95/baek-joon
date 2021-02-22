import sys

def BFS(grpah, root):
    visited = []
    queue = [root]

    while queue: # queue가 빌 때까지 반복
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n in graph:
                unvisited = list(set(graph[n])-set(visited)) # 중복되는거 제거
                unvisited.sort()
                queue += unvisited

    return " ".join([str(i) for i in visited])


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack: # stack이 빌 때까지 반복
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                unvisited = list(set(graph[n])-set(visited)) # 중복되는거 제거
                unvisited.sort(reverse=True) # reversed 해주는 것에 유의
                stack += unvisited
    return " ".join([str(i) for i in visited])


N,M,V = list(map(int, sys.stdin.readline().rsplit()))

graph = {}

for _ in range(M):
    v1,v2 = list(map(int, sys.stdin.readline().rsplit()))
    if v1 not in graph:
        graph[v1] = [v2]
    elif v2 not in graph[v1]:
        graph[v1].append(v2)
    if v2 not in graph:
        graph[v2] = [v1]
    elif v1 not in graph[v2]:
        graph[v2].append(v1)

print(DFS(graph, V))
print(BFS(graph, V))




