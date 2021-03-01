import sys

K = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(K):
    n = int(sys.stdin.readline().rstrip())
    if n != 0:
        stack.append(n)
    elif n == 0:
        stack.pop()

print(sum(stack))
    