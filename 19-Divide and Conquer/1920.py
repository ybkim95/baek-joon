import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rsplit()))

M = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().rsplit()))

cache = { i:False for i in range(N) }


def BS(target, A, start, end):
    if start > end:
        return 0

    mid = int((start+end)/2)

    if A[mid] == target:
        return 1
    else:
        if target > A[mid]:
            return BS(target, A, mid+1, end)
        else:
            return BS(target, A, start, mid-1)

A.sort()
for target in B:
    start = 0
    end = N-1
    print(BS(target, A, start, end))