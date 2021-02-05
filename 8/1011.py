import sys

n = int(sys.stdin.readline().rstrip())

def num_op(s, e):
    start = s+1
    end = e-1

    count = 0
    choice = [2, 1, 0]

    while True:
        if start >= end:
            break
        
        for c in choice:
            if (start + c) <= end:
                start += c
                choice[0] = c+1
                choice[1] = c
                choice[2] = c-1
                count += 1
                break
            
    print(count + 2)


for i in range(n):
    start, end = list(map(int, sys.stdin.readline().rsplit()))

    num_op(start, end)