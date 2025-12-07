a=int(input())
b = [list(map(int, input().split())) for i in range(a)]
v=b[0][1]
for i in range(a):
        if b[i][1]>v:
             v=b[i][1]
n=[0]*(v+1)
k=0
for i in range(a):
    for x in range(b[i][0], b[i][1]+1):
        n[x]+=1

f=n[b[0][0]:b[0][1]+1].index(max(n[b[0][0]:b[0][1]+1]))+1
print(f)