import sys

n = int(sys.stdin.readline().rstrip())

def draw(n):
    if n == 3:
        first = "***"
        second = "* *"
        third = "***"

    return draw(n//3)

print(circle(n))

