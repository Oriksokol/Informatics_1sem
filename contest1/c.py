import sys
n=int(input())
s=[0,0]
d=[0,0]
s[0]=1
s[1]=n-1
k=0
g=0
l=0
#s.insert(,)
for i in range(1,11):
   print(s,d)
   print(len(d))
   if i!=1 and i!=2:
       for h in range(1,len(d)-2):
           del d[h]
   d[0]=s[0]
   d[-1]=s[1]
   if i!=1:
       for h in range(i):
           d.insert(h,2**h)
           d[-1]-=2**h
   print(s,d)
   b=0
   while b==0:
        if i!=1:
           for m in range(i):
               while d[-m]>=2*d[-m-1]:
                   d[-m]-=1
                   d[-m-1]+=1
                   k+=1
        else:
            while d[-1]>=2*d[-2]:
                   d[-1]-=1
                   d[-2]+=1
                   k+=1
        if k==g:
            b=1
        else:
            g=k
   if l==k:
       print(k+1)
       sys.exit()
   else:
       l=k
print(k+1)