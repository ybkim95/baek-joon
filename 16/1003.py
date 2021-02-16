import sys

T = int(sys.stdin.readline().rstrip())

count = []

for i in range(41):
    if i == 0:
        count.append(0)
    elif i < 3:
        count.append(1)
    else:
        count.append(count[i-1] + count[i-2])

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        print("1 0")
    else:
        print(count[n-1], count[n])