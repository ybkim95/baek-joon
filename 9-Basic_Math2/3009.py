import sys

x_coord = []
y_coord = []

ans = [0]*2

for _ in range(3):
    x,y = list(map(int, sys.stdin.readline().rsplit()))
    x_coord.append(x)
    y_coord.append(y)

for i in range(3):
    if x_coord.count(x_coord[i]) == 1:
        ans[0] = x_coord[i]
    if y_coord.count(y_coord[i]) == 1:
        ans[1] = y_coord[i]

print(ans[0], ans[1])

