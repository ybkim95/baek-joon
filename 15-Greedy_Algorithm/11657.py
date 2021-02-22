import sys

INF = sys.maxsize # 무한대

N,M = map(int, sys.stdin.readline().rsplit())

graph = {i:{} for i in range(1,N+1)}

for _ in range(M):
    A,B,C = map(int, sys.stdin.readline().rsplit())
    if B not in graph[A]:
        graph[A][B] = C
    elif B in graph[A]:
        graph[A][B] = min(C, graph[A][B])

# print(graph)

def BellmanFord(graph):
    INF = sys.maxsize
    dis = {i:INF for i in graph} # distance | 0번째는 무의미한 idx 
    # pred = []*N
    dis[1] = 0 # start는 1로 주어짐

    # iterate V-1 times
    for i in range(1,N):
        for node in graph:
            for adj in graph[node]:
                if dis[node] != INF and dis[adj] > dis[node] + graph[node][adj]: # INF 부분 추가 중요
                    dis[adj] = dis[node] + graph[node][adj]
                    # pred[adj] = node

    # negative cycle check
    for node in graph:
        for adj in graph[node]:
            if dis[node] != INF and dis[adj] > dis[node] + graph[node][adj]: # INF 부분 추가 중요
                print(-1)
                return


    for i in dis:
        if i != 1:
            if dis[i] != INF:
                print(dis[i])
            else:
                print(-1)
    return

BellmanFord(graph)