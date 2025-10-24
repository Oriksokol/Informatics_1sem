nk=input().split()
a=list(map(int,input().split()))
n=int(nk[0])
k=int(nk[1])
max=0
for i in range(2**n):
    j=i^k
    if j>len(a):
        continue
    sum=a[i]+a[j]
    if max<sum:
        max=sum
print(max)