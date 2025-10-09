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
    if i == range(len(m)):
        output=[f"{k[i]}^{l[i]}" for i in range(len(k))]
        print(f"{g} = {"*".join(output)}")
        exit
    if m[i] in k:
       d=k.index[m[i]]
       l[d]+=1
    else:
        k.append(m[i])
        l.append(1)