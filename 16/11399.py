import sys

N = int(sys.stdin.readline().rstrip())

order = list(map(int, sys.stdin.readline().rsplit()))

order.sort()

# print(order)a

wait = 0
ans  = 0

for i in range(N):
    wait += order[i]
    ans += wait

print(ans)

    
    
