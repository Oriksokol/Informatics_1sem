grades =list(map(int, input().split()))
b=1
for i in range(0,len(grades)):
    b*=grades[i]
b=b**(1/len(grades))
print(b)