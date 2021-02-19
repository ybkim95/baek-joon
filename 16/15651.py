import sys
from itertools import product

N,M = list(map(int, sys.stdin.readline().rsplit()))

item = [i for i in range(1, N+1)]

res = product(item, repeat=M)

for i in res:
    print(' '.join([str(j) for j in i]))
