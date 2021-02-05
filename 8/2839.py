import sys

n = int(sys.stdin.readline().rstrip())

''' 방법 1 '''
# for i in range(n//3+1):
#     for j in range(n//5+1):
#         if n == 3*i+5*j:
#             print(i+j)
#             sys.exit()
# print(-1)

''' 방법 2 '''
box = 0
while True:
    if n % 5 == 0:
        box += n // 5
        print(box)
        break

    n -= 3
    box += 1

    if n < 0:
        print(-1)
        break
        