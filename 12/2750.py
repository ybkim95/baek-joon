import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

for end in range(1, N):
    for i in range(end, 0, -1):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1],arr[i]

for i in range(len(arr)):
    print(arr[i])