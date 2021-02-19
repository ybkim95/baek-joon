import sys
from itertools import combinations

N,M = list(map(int, sys.stdin.readline().rsplit()))

item = [i for i in range(1, N+1)]

res = list(combinations(item, M))

for i in range(len(res)):
    print(' '.join([str(j) for j in res[i]]))