import sys

M,N = list(map(int,sys.stdin.readline().rsplit()))

a = [False,False] + [True]*(N-1)
primes=[]

for i in range(2,N+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, N+1, i):
        a[j] = False

primes = [i for i in primes if i >= M]
for p in primes:
    print(p)


