import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

res = []
for n in range(M, N+1):
    i = 2
    while True:
        if n % i == 0:
            res.append(n)
            break
        elif i == N:
            break
        else:
            i +=1


print(sum(res))
print(min(res))
