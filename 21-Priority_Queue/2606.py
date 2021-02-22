import sys

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            if n in graph:
                unvisited = list(set(graph[n])-set(visited))
                unvisited.sort(reverse=True)
                stack += unvisited
    
    return visited


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

network = {}

for _ in range(M):
    c1,c2 = list(map(int, sys.stdin.readline().rsplit()))

    if c1 not in network:
        network[c1] = [c2]
    elif c2 not in network[c1]:
        network[c1].append(c2)
    
    if c2 not in network:
        network[c2] = [c1]
    elif c1 not in network[c2]:
        network[c2].append(c1)

print(len(DFS(network,1))-1)