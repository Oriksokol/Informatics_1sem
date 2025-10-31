n,m=map(int, input().split())
from math import inf
c = [list(map(int, input().split())) for _ in range(n)]
d = [[[-inf,-inf,-inf] for t in range(m)] for i in range(n)]
for y in range(n):
    for x in range(m):
        if y==0 and x==0:
            d[0][0][0],d[0][0][1],d[0][0][2]=c[0][0],c[0][0],c[0][0]
            continue
        d[y][x][0]=max(d[y-1][x][1],d[y-1][x][2])+c[y][x]
        d[y][x][1] = max(d[y][x-1][0],d[y][x-1][2]) + c[y][x]
        d[y][x][2] = max(d[y - 1][x-1][0],d[y - 1][x-1][1]) + c[y][x]
print(max(d[n-1][m-1]))