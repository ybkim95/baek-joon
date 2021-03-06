import sys

N = int(sys.stdin.readline().rstrip())

paper = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]

cnt1 = 0 # 1
cnt2 = 0 # 0

def check(unit_paper):
    # print(unit_paper)
    N = len(unit_paper)
    s = 0
    for i in range(N):
        s += sum(unit_paper[i])

    if N == 1:
        if unit_paper[0][0] == 1:
            return '11'
        else:
            return '10'
    
    if s == N*N:
        return '*1'
    elif s == 0:
        return '*0'
    else:
        return '~'

def divide(paper):
    global cnt1, cnt2
    a = check(paper)
    if a == '11' or a == '*1':
        cnt1 += 1
        # print("cnt1")
        return
    elif a == '10' or a == '*0':
        cnt2 += 1
        # print("cnt2")
        return
    else: # keep going
        N = len(paper)
        divide([row[:N//2] for row in paper[:N//2]])
        divide([row[:N//2] for row in paper[N//2:]])
        divide([row[N//2:] for row in paper[:N//2]])
        divide([row[N//2:] for row in paper[N//2:]])

divide(paper)

print(cnt2)
print(cnt1)
