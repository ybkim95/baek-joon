import sys

text = sys.stdin.readline().rstrip()
text = text.lower()

a = {}

for t in text:
    a[t] = a.get(t,0) + 1

b = [0]

for i in a.keys():
    if a[i] > b[0]:
        b[0] = a[i]
    elif a[i] == b[0]:
        b.append(a[i])

b = [_b for _b in b if _b >= max(b)]

if len(b) > 1:
    print('?')
else:

    max_char = max(a.keys(), key= lambda k: a[k]) 

    print(max_char.upper())