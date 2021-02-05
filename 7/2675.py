import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    n, text = sys.stdin.readline().rsplit()
    n = int(n)

    for i in text:
        print(i*n, end='')
    print()
