import sys
V = int(sys.stdin.readline().strip())
tree = {i:{} for i in range(1, V+1)}
parent_info = {i:0 for i in range(1, V+1)}

for _ in range(V):
    temp = list(map(int, sys.stdin.readline().split()))
    N = temp[0]
    temp = temp[1:-1]
    while temp:
        n = temp[0]
        d = temp[1]
        tree[N][n] = d
        temp = temp[2:]

# print(tree)

def dfs(start,tree):
    d = 0
    # print(start,tree)
    for i in tree[start]:
        if start in tree[i]:
            del tree[i][start]
        d += tree[start]
        dfs(i,tree)

dst = []
dfs(1,tree)
        

    
