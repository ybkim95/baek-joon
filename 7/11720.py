import sys
n = sys.stdin.readline().rstrip()
text = sys.stdin.readline().rstrip()

sum = 0

for i in text:
    sum += int(i)

print(sum)
