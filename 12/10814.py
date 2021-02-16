import sys

N = int(sys.stdin.readline().rstrip())

info = []

for i in range(N):
    age, name = list(sys.stdin.readline().rsplit())
    info.append((int(age),name,i))

info.sort(key=lambda x: (x[0],x[2]))

for i in info:
    print(i[0],i[1])