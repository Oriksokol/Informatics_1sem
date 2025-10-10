raw=list(map(int,input().split()))
for i in range(0,(len(raw))//2):
    print(raw[2*i],raw[2*i+1], end=' ')