a= open('input.txt', 'r')
array= a.readline().split()
p=0
for i in range(len(array)):
    array[i]=int(array[i])
b= a.readline()
if b == '+\n':
    p=sum(array)
    print(p)
elif b == '-\n':
    p=sum(array)*(-1)
elif b == '*\n':
    p = 1
    for i in array:
        p*=i
f= open ('output.txt', 'w')
f.write(str(p))
f.close()
