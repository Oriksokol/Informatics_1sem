a =str(input())
m=[]
k=[]
l=[]
j=0
b=int(a)
g=b
while b>1:
    for i in range(2,b+1):
        if b%i==0:
            m.append(i)
            b = b//i
            a=str(b)
            break
for i in range(len(m)):
    if m[i] in k:
       o=int(m[i])
       d=k.index(o)
       l[d]+=1
    else:
        k.append(m[i])
        l.append(1)
    if i == len(m)-1:
        output=[f"{k[i]}^{l[i]}" for i in range(len(k))]
        t = "*".join(output)
        print(f"{g} = {t}")
        exit