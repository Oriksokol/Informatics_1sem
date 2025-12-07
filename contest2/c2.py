def d(dn, n):
    c = 0
    for i in range(n):
        for j in range(i, n):
            if dn[i] > dn[j]:
                c += 1
    return(dn, c)
def l(t):
    return(t[1])
a = int(input())
for j in range(a):
    t = []
    n, m = tuple(map(int, input().split()))
    for i in range(m):
        s=input()
        t.append((d(s, n)))
    t.sort(key =l)
    for k in range(len(t)):
        print(t[k][0])
    print(' ')