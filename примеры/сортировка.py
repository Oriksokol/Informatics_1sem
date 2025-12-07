a= [6,9,3,-2,0,1,48]
N=len(a)
def siftDown(a,i):
    if i>len(a)//2-1:
        return
    index=a.index(max(a[2*i+1,a[2*i+2]]))
    if a[i]>max(a[2*i+1,a[2*i+2]]):
        return
    else:
        a[i],a[index]=a[index],a[i]
        siftDown[a,index]

for i in range(N//2,-1,-1):
    siftDown(a,i)
print(a)