import sys

A, B, V = list(map(int, sys.stdin.readline().rsplit()))

# 2 1 5                -> 4 (2 + 1 * 3)
# 5 1 6                -> 2 (5 + 4 * 1)
# 100 99 1000000000    -> 999999901 (100 + 1 * 999999900)

n = V // (A-B)

V -= n * (A-B)



