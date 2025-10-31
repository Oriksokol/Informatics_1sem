n,m=map(int, input().split())
from math import inf
c = [list(map(int, input().split())) for _ in range(n)]
d = [[-inf,-inf,-inf] * m for i in range(n)]
p = [[-1] * m for i in range(n)]
for y in range(n):
    for x in range(m):
        if y==0 and x==0:
            d[0][0]=c[0][0]
            continue
        if p[y-1][x]!=0:
                d[y][x][0]=max(d[y-1][x])+c[y][x]
                p[y][x]=0
        if p[y][x-1] != 1:
                d[y][x][1] = max(d[y][x-1]) + c[y][x]
                p[y][x] = 1
        if p[y - 1][x-1] != 2:
                d[y][x][2] = max(d[y - 1][x-1]) + c[y][x]
                p[y][x] = 2
print(max(d[n-1][m-1]))