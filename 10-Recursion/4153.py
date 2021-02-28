import sys

while True:
    a,b,c = list(map(int, sys.stdin.readline().rsplit()))

    if a == 0 and b == 0 and c == 0:
        break

    arr = sorted(list((a,b,c)))

    if arr[2]**2 == arr[0]**2 + arr[1]**2:
        print("right")
    else:
        print("wrong")
