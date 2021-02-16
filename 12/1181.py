import sys

N = int(sys.stdin.readline().rstrip())

dic = set()

for _ in range(N):
    dic.add(sys.stdin.readline().rstrip())

# print(dic)

ans = sorted(dic, key = lambda x : (len(x), x))

for a in ans:
    print(a)