import sys 
import heapq 

INF = sys.maxsize 

V, E = map(int, sys.stdin.readline().rsplit()) 
K = int(sys.stdin.readline().rstrip()) 

dis = [INF]*(V+1) 
heap = [] 
graph = [[] for _ in range(V + 1)] # V+1에 주목, 0은 무의미

def Dijkstra(start): 
    dis[start] = 0 
    heapq.heappush(heap,(0, start)) 
    
    while heap: 
        cur_w, cur_n = heapq.heappop(heap) 
        
        if dis[cur_n] < cur_w: 
            continue 
        
        for w, next_n in graph[cur_n]: 
            if dis[next_n] > w + cur_w :
                dis[next_n] = w + cur_w 
                heapq.heappush(heap,(w + cur_w , next_n)) 
                
for _ in range(E): 
    u, v, w = map(int, sys.stdin.readline().rsplit()) 
    graph[u].append((w, v)) 
    
Dijkstra(K) 
for i in range(1,V+1): # 0번째는 무시
    print("INF" if dis[i] == INF else dis[i])
