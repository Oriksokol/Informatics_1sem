import heapq
data=list(map(int, input().split()))
minh = []
maxh = []
ms = []
for n in data:
    heapq.heappush(maxh, -n)
    if minh!=[] and -maxh[0] > minh[0]:
        v1 = -heapq.heappop(maxh)
        v2 = heapq.heappop(minh)
        heapq.heappush(maxh, -v2)
        heapq.heappush(minh, v1)
    if len(maxh) > len(minh) + 1:
        v = -heapq.heappop(maxh)
        heapq.heappush(minh, v)
    if len(maxh) == len(minh):
        m = (-maxh[0] + minh[0])//2+(-maxh[0] + minh[0])%2
        ms.append(int(m))
    else:
        m = -maxh[0]
        ms.append(int(m))
for m in ms:
    print(m,end=' ')