import sys

n = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rsplit()))

cnt = 0

for n in numbers:
    if n > 1:
        switch = True
        for i in range(2, n):
            if n % i == 0:
                switch = False
            
        if switch:
            cnt += 1
        

print(cnt)

