def self_num():
    n = 1
    arr = []
    while True:
        sum = 0
        for _n in str(n):
            sum += int(_n)
        sum += n
        if n <= 10000:
            arr.append(sum)
            # print(sum)
            n += 1
        else:
            break
    
    arr = set(arr)
    _arr = set([i for i in range(1,10001)]) - arr
    _arr = list(_arr)
    _arr.sort()

    for i in _arr:
        print(i)


self_num()