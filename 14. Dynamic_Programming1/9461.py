import sys

dic = {1:1, 2:1, 3:1}

def P(n):
    if n in dic:
        return dic[n]
    else:
        dic[n] = P(n-2) + P(n-3)
        return dic[n]

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N  = int(sys.stdin.readline().rstrip())
    print(P(N))