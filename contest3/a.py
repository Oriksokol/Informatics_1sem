import math, sys
tree=input().split()
BST=True
minmax=[0,0]
if tree[0]=='None':
    print('YES')
    sys.exit()
if tree[1]!='None':
    minmax[0] = int(tree[1])
else:
    minmax[0] = int(tree[0])
if tree[2]!='None':
    minmax[1] = int(tree[2])
else:
    minmax[1] = int(tree[0])   
def right(tree,num,minmax):
    if tree[num]=='None':
        return True
    if tree[2*num+1]!='None':
       minmax[0]=min(minmax[0],int(tree[2*num+1]))
    if tree[2*num+2]!='None':   
       minmax[1]=min(minmax[1],int(tree[2*num+2]))
    if minmax[0]<int(tree[2*num+1]) or minmax[1]<int(tree[2*num+2]):
        return False
    if right(tree,2*num+1,minmax)==True and right(tree,2*num+2,minmax)==True:
        return True
    else:
        return False
if right(tree,0,minmax):
    print('YES')
else:
    print('NO')