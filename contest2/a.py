a=input()
c=[a[0]]
for i in range (1,len(a)):
    c.append(a[i])
    if len(c)==1:
        continue
    if c[-1]==')' and c[-2]=='(' or c[-1]==']' and c[-2]=='[' or c[-1]=='}' and c[-2]=='{':
        del c[-1]
        del c[-1]
if c!=[]:
    print('No')
else:
    print('Yes')