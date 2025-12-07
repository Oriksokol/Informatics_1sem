a=int(input())
for i in range(a):
   v=list(map(int, input().split()))
   print(v)
   b = [list(map(str, input().split())) for f in range(v[1])]
   k=[0]*v[1]
   def q(j):
       return -k[b.index(j)]
   for l in range(v[1]):
      f=0
      d=0
      while f==0:
           for x in range(v[0]-1):
               print(l,x,v[0])
               if b[l][x]>b[l][x+1]:
                    b[l][x],b[l][x+1]=b[l][x+1],b[l][x]
                    k[l]+=1
           if k[l]==d:
               f=1
           else:
               d=k[l]
   b.sort(key=q)
   for x in range(v[1]):
       print(b[x])
print()