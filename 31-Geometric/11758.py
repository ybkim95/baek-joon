import sys

coord = []
for _ in range(3):
    a,b = map(int, sys.stdin.readline().split())
    coord.append((a,b))

vec = []
for i in range(2):
    vec.append((coord[i+1][0]-coord[i][0], coord[i+1][1]-coord[i][1]))

def outer(v1,v2):
    # v1: 1 2 3 | 1
    # v2: 4 5 6 | 4
    return v1[0]*v2[1] - v1[1]*v2[0]

if outer(vec[0], vec[1]) > 0:
    print(1)
elif outer(vec[0], vec[1]) < 0:
    print(-1)
else:
    print(0)