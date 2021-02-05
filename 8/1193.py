import sys

n = int(sys.stdin.readline().rstrip())

# a_n = n -> S_n = n(1+n) / 2 = 0.5(n^2 + n)

def f(n):
    return (n**2 + n) / 2

i = 0
while True:
    if n == f(i):
        if n % 2 == 0:
            print("{}/{}".format(1,i))
        else:
            print("{}/{}".format(i,1))
        break
    if f(i) < n < f(i+1):
        a = i+1
        b = int(n - f(i))
        # print("divmod:",a,b)
        sum = a + 1
        if a % 2 == 0:
            first = b
            second = sum - b 
            print("{}/{}".format(first, second))
        else:
            first = sum - b
            second = b
            print("{}/{}".format(first, second))
        break
    else:
        i += 1
