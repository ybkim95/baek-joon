import sys

n = int(sys.stdin.readline().rstrip())

init = 666

while n:
    if '666' in str(init):
        n -= 1
    init += 1

print(init-1)
