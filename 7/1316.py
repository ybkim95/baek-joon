import sys

def group(text):
    text = [t for t in text]
    _text = set(text)

    res = {t:0 for t in _text}

    for i in range(len(text)):
    
        if res[text[i]] > 0:
            if i == 0:
                pass
            else:
                if text[i] == text[i-1]:
                    pass
                else:
                    return 0

        res[text[i]] += 1

    return 1


cnt = 0

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    text = sys.stdin.readline().rstrip()

    cnt += group(text)

print(cnt)
