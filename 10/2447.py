import sys

n = int(sys.stdin.readline().rstrip())

def circle(n):
    if n == 3:
        first = "***"
        second = "* *"
        third = "***"

    m = n // 3
    for i in range(3):

print(circle(n))

