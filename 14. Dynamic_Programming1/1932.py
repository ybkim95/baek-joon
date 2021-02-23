import sys

n = int(sys.stdin.readline().rstrip())

tri = []

for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().rsplit())))

# 예시
# 0층  7
# 1층 |3| \8\
# 2층 |8| 1 \0\
# 3층 |2| 7 4 \4\ 
# 4층 |4| 5 2 6 \5\

for stair in range(1, n):
    for idx in range(stair+1): # 0층에는 1개, 1층에는 2개, 2층에는 3개 ...
        # 수직선 부분에 해당되는 element들
        if idx == 0:
            tri[stair][idx] += tri[stair-1][idx]

        # 경사진 부분의 element들
        elif idx == stair:
            tri[stair][idx] += tri[stair-1][idx-1]
        
        # 그 어느곳에도 해당되는 않는 element들
        else:
            tri[stair][idx] += max( tri[stair-1][idx-1], tri[stair-1][idx] )

print(max(tri[n-1]))