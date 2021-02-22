import sys
import heapq

def dijkstra(graph, start):
    INF = float('INF')
    
    d = {node:INF for node in graph}
    d[start] = 0 # start as 0









# number of vertex, edge: V,E 
V,E = map(int, sys.stdin.readline().rsplit())

# start node K
K = int(sys.stdin.readline().rstrip())

INF = float('INF') # or V*10+1 s.t w <= 10 
graph = {i:{} for i in range(1,V+1)}

for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().rsplit())
    graph[u-1][v-1] = w

# print(graph)


