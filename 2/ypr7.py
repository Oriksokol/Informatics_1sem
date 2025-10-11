a=list(map(int,input().split()))
i=0
count=0
while i<=len(a)-1:
   m=a[i]
   c=a.count(m)
   if count<c:
      d=m
      count=c
   i+=1
print(d)