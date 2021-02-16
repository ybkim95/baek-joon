# counting sort
import sys

# length
T = int(sys.stdin.readline().rstrip())

# input
A = [int(sys.stdin.readline().rstrip()) for _ in range(T)]

count = [0]*(10000001)
countSum = [0]*(10000001)

# count
for i in range(T):
	count[A[i]] += 1

# accumulation
for i in range(1, 10000001):
	countSum[i] = countSum[i-1] + count[i]

# ans
B = [0]*(T)

for i in range(T-1, -1, -1):
	B[countSum[A[i]]] = A[i]

# print ans
for i in range(1, T):
	print(B[i])