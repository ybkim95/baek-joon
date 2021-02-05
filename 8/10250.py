import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    H,W,N = list(map(int, sys.stdin.readline().rsplit()))
    a,b = divmod(N,H)

    floor = b
    door = a

    if floor == 0:
        floor = str(H)
    else:
        floor = str(floor)

    if b == 0:
        door = str(door)
    else:
        door = str(door+1)

    if int(door) < 10:
        door = '0' + door

    print(floor+door)
