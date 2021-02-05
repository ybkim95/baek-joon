import sys

a,b = list(sys.stdin.readline().rsplit())

def change(number):
    a = list(number)
    b = list()
    for i in range(len(number)):
        b.append(a[len(number)-1-i])

    b = ''.join(b)

    return int(b)

a = change(a)
b = change(b)

print(max(a,b))
