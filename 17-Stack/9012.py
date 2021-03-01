import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    arr = list(str(sys.stdin.readline().rstrip()))
    stack = [arr.pop()]
    while True:
        # print(arr)
        # print(stack)
        if len(arr) == 0 and len(stack) != 0:
            print("NO")
            break
        elif len(arr) == 0 and len(stack) == 0:
            print("YES")
            break

        if len(stack) == 0:
            stack.append(arr.pop())

        elif arr[-1] == '(' and stack[-1] == ')':
            stack.pop()
            arr.pop()

        else:
            stack.append(arr.pop())


# # Ex. ())(()

# # STEP 1.
# ['(', ')', ')', '(', '(']   [')']

# # STEP 2.
# ['(', ')', ')', '(']   []

# # STEP 3.
# ['(', ')', ')']   ['(']

# # STEP 4.
# ['(', ')']   ['(', ')']



    