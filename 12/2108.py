#첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
#둘째 줄에는 중앙값을 출력한다.
#셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
#넷째 줄에는 범위를 출력한다.

import sys

n = int(sys.stdin.readline().rstrip())

sta = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

print("=========================")

# (1) 산술평균
mean = round(sum(sta)/len(sta))
print(mean)


# (2) 중앙값
sta.sort()
mid = sta[len(sta)//2]
print(mid)


# (3) 최빈값
freq = {i:0 for i in set(sta)}
for s in sta:
    freq[s] += 1
_freq = sorted(freq.items(), reverse=True, key=lambda x: (x[1],-x[0]))

# print(_freq)

if len(_freq) > 1:
    if _freq[0][1] == _freq[1][1]:
        print(_freq[1][0])
    else:
        print(_freq[-1][0])
else:
    print(_freq[-1][0])


# (4) 범위
sta.sort()
var = sta[-1] - sta[0]
print(var)