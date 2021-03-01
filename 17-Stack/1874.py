import sys

N = int(sys.stdin.readline().rstrip())
original = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
seq = original 
seq.sort(reverse=True)
stack = []

while True:
    stack.append(seq.pop())


    

