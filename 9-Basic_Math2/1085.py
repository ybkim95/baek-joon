import sys

x,y,w,h = list(map(int, sys.stdin.readline().rsplit()))

print(min(abs(w-x), abs(h-y), abs(x), abs(y)))