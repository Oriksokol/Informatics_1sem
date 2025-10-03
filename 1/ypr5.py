a = int(input())
b = 0
while not (2 <= b <= 10):
    b = int(input())
c = ''
while a > 0:
    d= a % b
    new = str(d) + c
    a = a // b
print(c)