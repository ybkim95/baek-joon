import sys

N = int(sys.stdin.readline().rstrip())
spare = N
res = []
i = 2
while N != 1:
    # print(N, i)
    if N % i == 0:
        res.append(i)
        N = int(N/i)
    else:
        i += 1

res.sort()

for r in res:
    print(r)

