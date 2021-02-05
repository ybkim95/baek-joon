import sys

def c2n(character):
    dictionary = {'ABC':2, 'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9}
    for i in dictionary.keys():
        for k in dictionary.keys():
            if character in list(k):
                return dictionary[k]

text = sys.stdin.readline().rstrip()

code = ''

for t in text:
    code += str(c2n(t))

sum = 0

for i in code:
    sum += int(i)

res = sum + len(code)

print(res)

    
