import sys

n = 123456
a = [True]*2*n
primes=[]

while True:

    N = int(sys.stdin.readline().rstrip())

    if N == 0:
        break
    
    M = int(N**0.5)
    for i in range(2,M+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, 2*N, i):
                a[j] = False

        _primes = [i for i in primes if i > N and i <= 2*N]
        
    print(len(_primes))


