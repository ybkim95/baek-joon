import sys

N = int(sys.stdin.readline().rstrip())

cnt = 0

def num(N):
    if N == 1:
        return 1
    else:
        return num(N-1)*2+1

def hanoi(source, destination, temp, n):
    global cnt
    if n < 1:
        return 
    hanoi(source, temp, destination, n-1)
    
    print("{} {}".format(source, destination))

    hanoi(temp, destination, source, n-1)
    
print(num(N))
hanoi(1,3,2,N)
