import sys
n=int(input())
d=[0,0]
k=0
g=0
l=0
#s.insert(,)
if n<3:
    print(k+1)
    sys.exit()
for i in range(1,11):
   d=[1,1]
   d[1]=n-1
   if i!=1:
    for h in range(1,i):
     d.insert(h,2**h)
     d[-1]-=2**h
    if i!=1:
      for f in range(1,666):
        for h in range(len(d)-1):
            d[-1]-=d[h]*(f-1)
            d[h]*=f
        if d[-1]>=2*d[-2]:
            k+=1
            print(d,k)
        else:
            d=[1,1]
            d[1]=n-1
            if i!=1:
                for h in range(1,i):
                    d.insert(h,2**h)
                    d[-1]-=2**h
            break
        d=[1,1]
        d[1]=n-1
        if i!=1:
            for h in range(1,i):
                d.insert(h,2**h)
                d[-1]-=2**h
   b=0
   if not (d[-1]>=2*d[-2]):
      print(k+2)
      sys.exit()
   while b==0:
        if i!=1:
           for m in range(i+1):
               while (d[-m]-1)>=2*(d[-m-1]+1):
                   k+=1
                   d[-m]-=1
                   d[-m-1]+=1
                   print(d,k)
        else:
            while (d[-1]-1)>=2*(d[-2]+1):
                   d[-1]-=1
                   d[-2]+=1
                   k+=1
                   print(d,k)
        if k==g:
            b=1
        else:
            g=k
   if l==k:
       print(k+2)
       sys.exit()
   else:
       l=k
print(k+2)