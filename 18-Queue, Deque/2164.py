import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
arr = [i for i in range(1, N+1)]
queue = deque(arr)

while len(queue) != 1:
    # print(queue)4
    queue.popleft()
    a = queue.popleft()
    queue.append(a)

print(queue.pop())

    