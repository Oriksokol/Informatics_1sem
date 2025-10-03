n=list(map(int,input().split ()))
a=n[0]
print(n)
del n[0]
print (((1+a)/2)*a - sum(n))