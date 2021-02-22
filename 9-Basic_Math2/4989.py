import sys

while True:
    n = int(sys.stdin.readline().rstrip())
     
    if n == 0:
        break
    
    ans = []
    for _n in range(n+1, 2*n+1):    
        i = 2
        switch = False
        while True:
            if _n % i == 0:
                break
            elif i > _n**0.5:
                switch = True
                break
            else:
                i+=1
        if switch:
            ans.append(_n)
                
    print(len(ans))


