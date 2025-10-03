a= open('input.txt', 'r')
array= a.readline().split( )
p=0
m=0
m=int(m)
b= a.readline()
e =int(a.readline())
for i in range(len(array)):
    z=0
    for z in range(len(array[i])):
        h=-1*(z+1)
        m+=int(array[i][h])*e**z
    array[i]=m
    m=0
    print(array[i])
if b == '+\n':
    p=sum(array)
elif b == '-\n':
    p=sum(array)*(-1)
elif b == '*\n':
    p = 1
    for i in array:
        p*=i
if e> 10:
    exit()
c = ''
while p > 0:
    d= p % e
    c = str(d) + c
    p = p // e
print(c)
f= open ('output.txt', 'w')
f.write(c)
f.close()