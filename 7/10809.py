import sys

corpus = 'abcdefghijklmnopqrstuvwxyz'
corpus = {alphabet:-1 for alphabet in corpus}

word = sys.stdin.readline().rstrip()

for i,w in enumerate(word):
    if w in corpus:
        if corpus[w] == -1:
            corpus[w] = i

a = ''
for i in corpus:
    a += (str(corpus[i])+" ")
a = a[:-1]

print(a)