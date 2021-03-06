import sys

N = int(sys.stdin.readline().rstrip())

paper = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]

cnt1 = 0 # -1
cnt2 = 0 #  0
cnt3 = 0 #  1

def check(unit_paper):
    # print(unit_paper)
    N = len(unit_paper)
    s = 0

    for i in range(N):
        if len(set(unit_paper[i])) == 1:
            s += sum(unit_paper[i])
        else:
            return '~'

    if N == 1:
        if unit_paper[0][0] == -1:
            return '1-1'
        elif unit_paper[0][0] == 0:
            return '10'
        else:
            return '11'
    
    if s == -N**2:
        return '*-1'
    elif s == 0:
        return '*0'
    elif s == N**2:
        return '*1'

def divide(paper):
    global cnt1, cnt2, cnt3
    a = check(paper)
    if a == '1-1' or a == '*-1':
        cnt1 += 1
        return
    elif a == '10' or a == '*0':
        cnt2 += 1
        return
    if a == '11' or a == '*1':
        cnt3 += 1
        return
    else: # keep going
        N = len(paper)
        divide([row[:N//3] for row in paper[:N//3]])
        divide([row[N//3:N//3*2] for row in paper[:N//3]])
        divide([row[N//3*2:] for row in paper[:N//3]])

        divide([row[:N//3] for row in paper[N//3:N//3*2]])
        divide([row[N//3:N//3*2] for row in paper[N//3:N//3*2]])
        divide([row[N//3*2:] for row in paper[N//3:N//3*2]])
        
        divide([row[:N//3] for row in paper[N//3*2:]])
        divide([row[N//3:N//3*2] for row in paper[N//3*2:]])
        divide([row[N//3*2:] for row in paper[N//3*2:]])
        
divide(paper)

print(cnt1)
print(cnt2)
print(cnt3)
