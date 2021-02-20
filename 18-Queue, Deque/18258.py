from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

deq = deque()
for _ in range(n):
    command = list(sys.stdin.readline().rsplit())

    if command[0] == 'push':
        deq.append(int(command[1]))
    
    elif command[0] == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()    
    
    elif command[0] == 'size':
        print(len(deq))

    elif command[0] == 'empty':
        print(1) if len(deq) == 0 else print(0)

    elif command[0] == 'front':
        print(deq[0]) if len(deq) != 0 else print(-1)

    elif command[0] == 'back':
        print(deq[-1]) if len(deq) != 0 else print(-1)