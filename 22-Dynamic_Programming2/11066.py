import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    K = int(sys.stdin.readline().rstrip())
    f_size = list(map(int, sys.stdin.readline().rsplit()))
    f_size.sort()

    # print(f_size)

    ans = 0
    ans += f_size[0]*(K-1)
    # print(ans)
    ans += f_size[1]*(K-1)
    # print(ans)
    
    for i in range(2, K):
        ans += f_size[i]*(K-i)
        # print(ans)    
    
    if K % 2 == 0:
        print(min(ans,2*sum(f_size)))
    else:
        # 홀수인 경우
        max1 = 
        max2 = 
        print(min(ans,))
        


