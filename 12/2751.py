import sys

T = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(T)]

arr.sort()

for i in range(len(arr)):
    print(arr[i])