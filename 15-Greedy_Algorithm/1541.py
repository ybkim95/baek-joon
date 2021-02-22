import sys

equ = sys.stdin.readline().rstrip()

operator = ['+', '-'] 


equ = equ.split('+')
equ.sort()

plus = []
_minus = []
minus = []

for e in equ:
    if '-' not in e:
        plus.append(e)
    else:
        _minus.append(e)

for m in _minus:
    minus.append(m.split('-'))

minus = minus[0]

plus = [int(p) for p in plus]
m = int(minus[0])
minus = minus[1:]
for _m in minus:
    m -= int(_m)
print(sum(plus) + m)

# print(plus)
# print(minus)    






