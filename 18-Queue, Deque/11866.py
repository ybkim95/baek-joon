import sys

N,K = map(int, sys.stdin.readline().rsplit())
arr = [i for i in range(1, N+1)]
ans = []

# 1 2 3 4 5 6 7        
# 1 2 X 4 5 6 7       2
# 1 2 X 4 5 X 7       4
# 1 X X 4 5 X 7       1
# 1 X X 4 5 X X
# 1 X X 4 X X X
# X X X 4 X X X

pop_idx = 0
while arr:
    pop_idx = (pop_idx + (K-1)) % len(arr) # 현재 상태에서 pop 해야할 element의 index
    pop_elem = arr.pop(pop_idx)
    ans.append(pop_elem)

print("<", end="")
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end="")
    else:
        print(ans[i], end=", ")
print(">")
