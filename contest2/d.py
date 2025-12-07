import heapq
a=int(input())
b = [list(map(int, input().split())) for i in range(a)]
def b2(b):
    return b[1]
b.sort(key=b2)
t=[]
l=0
s=0
for i in range(a):
    heapq.heappush(t,-b[i][0])
    s+=b[i][0]
    if s>b[i][1]:
        f=-heapq.heappop(t)
        s-=f
print(len(t))