raw = input()
l=raw.split()
N, string= int(l[0]), l[1]
M=len(string)
new= string[M//N-1::-1]
for i in range(0,M,M//N):
    new+=string[i+M//N-1: i-1:-1]
print(new)
