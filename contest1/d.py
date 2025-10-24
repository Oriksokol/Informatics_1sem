import sys
nm=input().split()
n=int(nm[0])
m=int(nm[1])
f=0
x=0
if (m%2==0) or (n%2==0):
    print(0)
    sys.exit()
else:
    f=1
    n1=(n-1)/2
    m1=(m-1)/2
    while (m1%2!=0) and (n1%2!=0):
       x+=1
       f+=4**x
       n1=(n1-1)/2
       m1=(m1-1)/2
print(f)