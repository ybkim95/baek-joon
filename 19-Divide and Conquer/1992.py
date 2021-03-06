import sys

N = int(sys.stdin.readline().rstrip())

paper = [ list(str(sys.stdin.readline().strip())) for _ in range(N) ]

ans = ""

def check(unit_paper):
    # print(unit_paper)
    N = len(unit_paper)
    s = 0
    for i in range(N):
        s += sum(map(int,unit_paper[i]))

    if N == 1:
        if unit_paper[0][0] == '1':
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
    #print(paper)
    global ans
    a = check(paper)
    if a == '11' or a == '*1':
        ans += '1'
        # print("cnt1")
        return
    elif a == '10' or a == '*0':
        ans += '0'
        # print("cnt2")
        return
    else: # keep going
        N = len(paper)
        ans += '('

        divide([row[:N//2] for row in paper[:N//2]])
        divide([row[N//2:] for row in paper[:N//2]])
        divide([row[:N//2] for row in paper[N//2:]])
        divide([row[N//2:] for row in paper[N//2:]])

        ans += ')'

divide(paper)

print(ans)
