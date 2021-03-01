import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N,M = map(int, sys.stdin.readline().rsplit())
    graph = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(M)]
    print(N-1)


