import sys

sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().strip())
tree = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

parent_info = {i:0 for i in range(1,N+1)}

def dfs(root,tree,parent):
    for i in tree[root]:
        if parent_info[i] == 0:
            parent_info[i] = root
            dfs(i,tree,parent_info)

dfs(1,tree,parent_info)

for i in parent_info:
    if i > 1:
        print(parent_info[i])



# 7 (1~7번 노드까지)
# 1 6 
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7
