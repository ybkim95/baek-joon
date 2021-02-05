import sys

def check(word):
    corpus = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    cnt = 0

    for c in corpus:
        if word.find(c) != -1:
            cnt += 1

    if cnt == 0:
        return True
    
    else:
        return False


def num_words(word):
    
    corpus = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    # base-case
    if check(word):
        return len(word)
    
    for c in corpus:
        if word.find(c) != -1:
            sp = word.find(c)
            sub1,sub2 = word[:sp], word[sp+len(c):]

            return num_words(sub1)+num_words(sub2) + 1



word = sys.stdin.readline().rstrip()
print(num_words(word))





