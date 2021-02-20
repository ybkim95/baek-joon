import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

def prime_list(m, n):
    arr = [True]*(n+1)

    _n = int((n+1)**0.5)
    for i in range(2, _n+1):
        if arr[i] == True:
            for j in range(2*i, n+1, i):
                arr[j] = False

    return [i for i in range(max(2,m),n+1) if arr[i] == True]

res = prime_list(M,N)

if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(min(res))
    # print(res)
