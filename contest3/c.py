import math
import sys

def ST(arr):
    n = len(arr)
    logn = int(math.log2(n)) + 1
    st = [ [0]* n for _ in range(logn)] 
    st[0] = arr
    for k in range(1, logn):
        shift =2**(k - 1)
        for i in range(n - (2**k) + 1):
            st[k][i] = max(st[k-1][i], st[k-1][i+shift])
    return st, logn
def rmq(st, LOGN, l, r):
    if l > r:
        return 0
    k = int(math.log2(r - l + 1))
    return max(st[k][l], st[k][r - (2**k) + 1])
def solve():
    border = list(map(int, input().split()))
    n, q = border
    a = list(map(int, input().split()))
    blstarts = []
    blends = []
    blcounts = []
    blindexmap = [0]* n
    start_idx = 0
    for i in range(1, n + 1):
        if i == n or a[i] != a[i-1]:
            end_idx = i - 1
            blstarts.append(start_idx)
            blends.append(end_idx)
            count = end_idx - start_idx + 1
            blcounts.append(count)
            nowblid = len(blstarts) - 1
            for j in range(start_idx, i):
                blindexmap[j] = nowblid  
            if i < n:
                start_idx = i
    st_counts, LOGN_counts = ST(blcounts)
    results = []
    for _ in range(q):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        blidx1 = blindexmap[i]
        blidx2 = blindexmap[j]

        if blidx1 == blidx2:
            results.append(str(j - i + 1))
        else:
            count1 = blends[blidx1] - i + 1
            count2 = j - blstarts[blidx2] + 1
            count3 = rmq(st_counts, LOGN_counts, blidx1 + 1, blidx2 - 1)
            results.append(str(max(count1, count2, count3)))
    print('\n'.join(results))
t = int(input()) 
for p in range(t):
    solve()