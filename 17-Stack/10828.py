import sys

n = int(sys.stdin.readline().rstrip())

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if len(self.stack) < 1:
            print(-1)
        else:
            print(self.stack.pop())

    def size(self):
        print(len(self.stack))

    def empty(self):
        if len(self.stack) == 0:
            print(1)
        else:
            print(0)

    def top(self):
        if len(self.stack) < 1:
            print(-1)
        else:
            print(self.stack[-1])


stack = Stack()

for _ in range(n):
    command = list(sys.stdin.readline().rsplit())

    # print(command)

    if len(command) > 1 and command[0] == 'push':
        x = int(command[1])
        stack.push(x)

    else:
        if command[0] == 'pop':
            stack.pop()
        elif command[0] == 'size':
            stack.size()
        elif command[0] == 'empty':
            stack.empty()
        elif command[0] == 'top':
            stack.top()



