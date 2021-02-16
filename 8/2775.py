import sys

apart = [[j if i==0 else 0 for j in range(14)] for i in range(14)]

def num_people(floor, door):

    if floor == 1:
        apart[floor][door] = int(door*(door+1)/2)
        return apart[floor][door]
    
    if door == 1:
        apart[floor][door] = 1
        return apart[floor][door]

    else:
        apart[floor][door] = sum([apart[floor-1][d] for d in range(1, door+1)])
        return apart[floor][door]

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    for i in range(k+1):
        for j in range(n+1):
            print("{}층의 {}호의 사람은 {}명입니다".format(i, j, apart[i][j]))

    print("================================================")

    num_people(k, n)

    #print(apart[k][n])

    for i in range(k+1):
        for j in range(1,n+1):
            print("{}층의 {}호의 사람은 {}명입니다".format(i, j, apart[i][j]))
