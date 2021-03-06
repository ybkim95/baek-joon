import sys

def fact(n):
    if n < 2:
        return 1
    else:
        return n*fact(n-1)

n = int(sys.stdin.readline().strip())
M = fact(n)
N = M
two = 0
five = 0

# print(N)

while True:
    if N % 2 == 0:
        two += 1
        N = N//2
    if N % 5 == 0:
        five += 1
        N = N//5
    
    if N % 2 != 0 and N % 5 != 0:
        break

print(min(two, five))
