a=int(input())
b = [list(map(int, input().split())) for i in range(a)]
k=0
i=0
x=0
def b2(b):
    return b[1]
b.sort(key=b2)
def b1(b):
    return b[0]
b.sort(key=b1)
i=0
x=0
while i<=(a-1):
    x=b[i][1]
    while i<(a-1) and x>=b[i+1][0]:
        x=min(x,b[i+1][1])
        i+=1
    k+=1
    i+=1
print(k)