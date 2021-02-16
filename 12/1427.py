import sys

num = sys.stdin.readline().rstrip()

arr = [int(n) for n in num]

arr.sort(reverse=True)

ans = ""
for a in arr:
    ans += str(a)

print(ans)

