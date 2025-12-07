s=input().split()
words={}
for word in s:
    key=''.join(sorted(word))
    if key in words:
        words[key].append(word)
    else:
        words[key]=[word]
def b(key):
    return(len(words[key]))
def b1(key):
    if len(words[key])==1:
        return words[key][0]
    else:
        return('~')

s=sorted(words,key=b1)
s=sorted(s,key=b, reverse=True)
for group in words:
    words[group].sort()
for i in s:
    print(' '.join(words[i]), end=' ')