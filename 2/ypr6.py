a=list(map(int,input().split()))
print(','.join(f"{a[i]}" for i in range(len(a)) if a.count(a[i])==1 ))