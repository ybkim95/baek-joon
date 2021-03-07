import sys

coord1 = list(map(int, sys.stdin.readline().split())) # a b
a = (coord1[0], coord1[1])
b = (coord1[2], coord1[3])

coord2 = list(map(int, sys.stdin.readline().split())) # c d
c = (coord2[0], coord2[1])
d = (coord2[2], coord2[3])

ab = (b[0]-a[0], b[1]-a[1])
bc = (c[0]-b[0], c[1]-b[1])
bd = (d[0]-b[0], d[1]-b[1])

cd = (d[0]-c[0], d[1]-c[1]) 
da = (d[0]-a[0], d[1]-a[1])
db = (d[0]-b[0], d[1]-b[1])


def ccw(v1,v2):
    return v1[0]*v2[1] - v1[1]*v2[0]


if ccw(ab, bc) * ccw(ab, bd) == 0 and ccw(cd, da) * ccw(cd, db) == 0:
    if a > b:
        a,b = b,a
    if c > d:
        c,d = d,c
    
    if not (c > b or a > d):
        print(1)
        exit()
    else:
        print(0)
        exit()

if ccw(ab, bc) * ccw(ab, bd) <= 0 and ccw(cd, da) * ccw(cd, db) <= 0:
    print(1)
else:
    print(0)
