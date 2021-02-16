# greedy
# knapsack?

import sys

N, K = list(map(int, sys.stdin.readline().rsplit()))

coins = []

num_coins = 0

for _ in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))

coins.sort(reverse=True)

while True:

    if K <= 0:
        break

    for c in coins:
        n = K // c
        if n >= 1:
            num_coins += n
            K -= n * c

print(num_coins)
