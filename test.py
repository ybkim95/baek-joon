import sys

def solution(n):
    string = str(n)
    ans = []
    for s in string:
        ans.append(int(s))
    ans.sort(reverse=True)
    
    for a in ans:
        print(a, end="")

n = sys.stdin.readline().rstrip()
solution(n)
