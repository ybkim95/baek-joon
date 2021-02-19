import sys

n = int(sys.stdin.readline().rstrip())

team = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(n)]

# print(team)

from itertools import combinations

item = [i for i in range(n)]

res = []

for i,j in list(combinations(item, int(n/2))):
    res.append( abs( (team[i][j] + team[j][i]) ) )

print(min(res))
