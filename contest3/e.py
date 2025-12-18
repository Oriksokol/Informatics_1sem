nq=list(map(int, input().split()))
s_input = input().strip()
string = list(s_input) 
for i in range(nq[1]):
    ijk=list(map(int, input().split()))
    if ijk[2]==1:
        string[(ijk[0]-1):ijk[1]]=sorted(string[(ijk[0]-1):ijk[1]])
    else:
        string[(ijk[0]-1):ijk[1]]=sorted(string[(ijk[0]-1):ijk[1]], reverse=True)
print(''.join(string))