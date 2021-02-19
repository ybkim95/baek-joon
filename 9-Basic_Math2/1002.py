import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    x1,y1,r1,x2,y2,r2 = list(map(int, sys.stdin.readline().rsplit()))

    # 같은 선상에 있으면 1
    # 무한히 같으면 -1
    # 같은 선상이 아니라면 2

    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    elif x1==x2 and y1==y2 and r1!=r2:
        print(0)
    elif (r1+r2)**2 == ((x1-x2)**2 + (y1-y2)**2):
        # print((r1+r2)**2, ((x1-x2)**2 + (y1-y2)**2))
        print(1) 
    else:
        print(2)