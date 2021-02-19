import sys

n = int(sys.stdin.readline().rstrip())

persons = []

for _ in range(n):
    w,h = list(map(int, sys.stdin.readline().rsplit()))
    persons.append((w,h))

# print(persons)

rank = [0]*n

for i,p in enumerate(persons):

    # print("p: {}".format(p))

    r = 0

    for _p in persons:
        # print(_p)
        if _p[0] > p[0] and _p[1] > p[1]:
            r += 1

    rank[i] = r+1

for _r in rank:
    print(_r)