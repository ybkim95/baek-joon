import sys

N = int(sys.stdin.readline().rstrip())

def draw(i,j):
    while(i != 0):
        # 중복될 것처럼 보이지만 return으로 인해 신기하게도 중복 X
        if (i % 3 == 1 and j % 3 == 1): # 빈칸이 있어야 하는 자리들의 공통적인 특성
            sys.stdout.write(" ") # 기존 print 대신 이걸 쓰면 즉각적으로 출력이 되어 굉장히 편리
            return
        i //= 3
        j //= 3
    
    sys.stdout.write("*")

for i in range(N):
    for j in range(N):
        draw(i,j)
    sys.stdout.write("\n") # print와 다르게 수동으로 "\n"을 통해 개행해줘야 한다.