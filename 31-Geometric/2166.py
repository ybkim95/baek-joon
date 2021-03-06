import sys

N = int(sys.stdin.readline().strip())

coord = []

def dis(c1,c2):
    return ( (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 )**0.5


for _ in range(N):
    x,y = map(int, sys.stdin.readline().split())
    coord.append((x,y))

# print(coord)

# ans = 0

# Method 1. 헤론의 법칙 시도 -> 실패?
# while len(coord) != 2:
#     a = dis(coord[0], coord[1])
#     b = dis(coord[0], coord[2])
#     c = dis(coord[1], coord[2])
#     s = (a+b+c)/2
#     S = (s*(s-a)*(s-b)*(s-c))**0.5
#     ans += S

#     coord.pop(1)

# print(round(ans,1))

# Method 2. 신발끈의 법칙
temp1 = 0
temp2 = 0
for i in range(N-1):
    temp1 += coord[i][0]*coord[i+1][1] # 0 1 2 
    temp2 += coord[i+1][0]*coord[i][1]
temp1 += coord[N-1][0]*coord[0][1]
temp2 += coord[0][0]*coord[N-1][1]
ans = abs(temp1-temp2)*0.5

print(ans)