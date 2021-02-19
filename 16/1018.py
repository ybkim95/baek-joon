import sys

m,n = list(map(int, sys.stdin.readline().rsplit()))

candidate = [sys.stdin.readline().rstrip() for _ in range(m)]

# print(candidate)
# print(candidate[0:8][0:8])
# print(candidate[1:9][1:9])

# print("===================")

label = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
label1 = list(reversed(label))
res = []

def diff(_candidate):
    ans = 0
    # print(_candidate)
    for i in range(8):
        for j in range(8):
            # print(i,j)
            if _candidate[i][j] != label[i][j]:
                ans += 1
    return ans

def diff1(_candidate):
    ans = 0
    for i in range(8):
        for j in range(8):
            if _candidate[i][j] != label1[i][j]:
                ans += 1
    return ans

for s_row in range(0, m-7):
    for s_col in range(0, n-7):
        # print("s_row:{}, s_col:{}".format(s_row, s_col))
        res.append(diff([row[s_col:s_col+8] for row in candidate[s_row:s_row+8]]))
        res.append(diff1([row[s_col:s_col+8] for row in candidate[s_row:s_row+8]]))

print(min(res))

