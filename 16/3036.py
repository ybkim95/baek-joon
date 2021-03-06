import sys

def gcd(a,b):
    while b != 0:
        d = a % b
        a = b
        b = d
    return a

N = int(sys.stdin.readline().strip())

ring = list(map(int, sys.stdin.readline().split()))

for i in range(1,N):
    a = ring[0]
    b = gcd(ring[0], ring[i])
    print("{}/{}".format(a//b,ring[i]//b))