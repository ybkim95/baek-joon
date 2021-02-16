import sys

N = int(sys.stdin.readline().rstrip())

coord = []

for _ in range(N):
    x,y = list(map(int, sys.stdin.readline().rsplit()))
    coord.append((x,y))

# print(coord)

coord.sort()

# print(coord)

for c in coord:
    print(c[0], c[1])
