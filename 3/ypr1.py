n=20
def fibonacci_right(n):
    numbers_fib=[0]*n
    numbers_fib[0]=1
    numbers_fib[1]=1
    for i in range(2,n):
        numbers_fib[i] = numbers_fib[i-1]+numbers_fib[i-2]
    return numbers_fib[-1] 
print(fibonacci_right(11))