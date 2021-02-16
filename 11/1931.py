import sys

T = int(sys.stdin.readline().rstrip())

schedule = [] 

for _ in range(T):
    start,end = map(int, sys.stdin.readline().rsplit())
    schedule.append((end,start))

schedule.sort()

cnt = 1
start = schedule[0][0]

for i in range(1, T):
    if schedule[i][1] >= start:
        start = schedule[i][0]
        cnt += 1

print(cnt)
