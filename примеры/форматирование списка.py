#1024=2*2*2*2*2*2*2*2*2*2=2^10
a=1024
#....
numbers=[2,3]
degrees=[10,1]
output=[f"{numbers[i]}^{degrees[i]}" for i in range(len(numbers))]
print(f"{a} = {"*".join(output)}")