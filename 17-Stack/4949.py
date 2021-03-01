import sys

while True:
    print("h")
    _a = sys.stdin.readline()
    if '.' in str(_a) and len(str(_a)) == 1:
        break
    elif '.' == str(_a).strip() and len(str(_a)) > 1:
        print("yes")
        continue
    else:
        a = str(_a).rstrip()
        arr = list(a)[:-1]
        stack = [arr.pop()]
    
    while True:
        # print(arr)
        # print(stack)

        if len(arr) == 0 and len(stack) != 0:
            print("no")
            break
        elif len(arr) == 0 and len(stack) == 0:
            print("yes")
            break

        if len(stack) == 0:
            a = arr.pop()
            if a in '()[]':
                stack.append(a)

        elif (arr[-1] == '(' and stack[-1] == ')') or (arr[-1] == '[' and stack[-1] == ']'):
            stack.pop()
            arr.pop()

        else:
            a = arr.pop()
            if a in '()[]':
                stack.append(a)



    