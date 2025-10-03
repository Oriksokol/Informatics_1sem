a=input()
b=int(a[0])
c=a[2]
d=b//2+b%2+16
e=b//2
for i in range(d):
    print(c*i)
for i in range(e):
    print(c*(e-i))