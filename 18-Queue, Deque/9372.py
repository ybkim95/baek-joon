import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N,M = map(int, sys.stdin.readline().rsplit())
    graph = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(M)]
    print(N-1) # 연결 그래프의 정의를 참고하면 바로 답이 나오는 문제.


