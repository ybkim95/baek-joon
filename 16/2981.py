import sys

# 약수
def div(n):
    div_list = [n]
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            div_list.append(i)
            if n//i != i: # 이 부분 중요
                div_list.append(n//i)
    div_list.sort()
    return div_list

# print(div(12))

# 최대공약수
def gcd(a,b):
    while b != 0:
        d = a%b
        a = b
        b = d
    return a

N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

arr.sort(reverse=True)
gcds = []
# ans = 0
for i in range(len(arr)-1):
    gcds.append(arr[i]-arr[i+1])

if len(gcds) == 1:
    ans = gcds[0]
elif len(gcds) == 2:
    ans = gcd(gcds[0], gcds[1])
else:
    ans = gcds[0]
    for i in range(1,len(gcds)):
        ans = gcd(ans, gcds[i])

for i in div(ans):
    print(i, end=' ')



# #최대공약수를 빠르게 구해주는 유클리드 호제법
# def gcd(x,y):
#     mod = x % y
#     while mod >0:
#         x = y
#         y = mod
#         mod = x % y
#     return y

# #약수 리스트를 구해주는 함수
# def div(x):
#     div_list = [x]
#     for i in range(2, int(x**(1/2) + 1)):
#         if x % i == 0:
#             div_list.append(i)
#             if x//i != i:
#                 div_list.append(x//i) 
#     div_list.sort()
#     return div_list 
    
    
# #입력함수
# N = int(input())
# freight = []
# for _ in range(N):
#     freight.append(int(input()))
# freight.sort(reverse = True)


# #화물들의 차이 입력
# freight_diff = []
# for i in range(len(freight)-1):
#     freight_diff.append(freight[i] - freight[i+1])

# #화물들의 차이를 최대공약수 함수를 이용해 구해주기
# if len(freight_diff) == 1:
#     answer = freight_diff[0]
# elif len(freight_diff) == 2:
#     answer = gcd(freight_diff[0], freight_diff[1])
# else:
#     answer = freight_diff[0]
#     for i in range(1, len(freight_diff)):
#         answer = gcd(answer, freight_diff[i]) 

# #구한 최대공약수의 모든 약수 출력
# for i in div(answer):
#     print(i, end = ' ')