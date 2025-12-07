a=int(input())
b = [list(map(int, input().split())) for i in range(a)]
def b1(b):
    return b[0]
b.sort(key=b1)
def b2(b):
    return b[1]
b.sort(key=b2,reverse=True)
v=b[0][1]
for i in range(a):
        if b[i][1]>v:
             v=b[i][1]
n=[0]*(v+1)
k=0
for i in range(a):
    for x in range(b[i][0], b[i][1]+1):
        n[x]+=1
while a>0:
   f = b[0][0]
   m = n[b[0][0]]
   for x in range(b[0][0] + 1, b[0][1] + 1):
      if n[x] > m:
        f = x
        m = n[x]
   i = 0
   while i < a:
        if f in range(b[i][0], b[i][1] + 1):
           for x in range(b[i][0], b[i][1] + 1):
                n[x] -= 1
           del b[i]
           i -= 1
           a -= 1
        i += 1
   k += 1
print(k)