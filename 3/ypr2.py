a =str(input())
m=[]
b=int(a)
while b>1:
    for i in range(2,b+1):
        if b%i==0:
            m.append(i)
            b = b//i
            a=str(b)
            break
print(m)