n=int(input())
d=[0]*(n+1)
for i in range(n+1):
    d[i]=[1]+[0]*n
for i in range(1,n//2+1):
    for h in range(1,n//2+1):
        d[i][h]=d[i-1][h]+d[i//2][h-i]
for i in range(n//2+1,n+1):
    d[i][n]=d[i-1][n]+d[i//2][n-i]
print(d[-1][-1])