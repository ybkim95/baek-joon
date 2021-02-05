import sys

def check(n):
    arr = [int(i) for i in str(n)]

    if len(arr) <= 2:
        return 1
    else:
        a = set()
        for i in range(len(arr)-1):
            a.add(arr[i] - arr[i+1])

        if len(a) == 1:
            return 1
        else:
            return 0

def hansu(n):
    cnt = 0
    for i in range(1, n+1):
        cnt += check(i)
    
    print(cnt)

n = sys.stdin.readline().rstrip()
hansu(int(n))