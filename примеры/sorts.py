# Пузырёк
# a = [6, 9, 3, -2, 0, 1, 48]
# N = len(a)
# print("Было:", a)
# for i in range(N - 1):
#     for j in range(N - 1 - i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print("Стало:", a)

a = [6, 9, 3, -2, 0, 1, 48]
N = len(a)
print("Было:", a)

def siftDown(a, i):
    if i > len(a)//2 - 1:
        return a
    if 2 * i + 1 == len(a) - 1:
        if a[i] < a[2 * i + 1]:
            a[i], a[2 * i + 1] = a[2 * i + 1], a[i]
        return a
    else:
        maxChild = max(a[2 * i + 1], a[2 * i + 2])
        if a[i] > maxChild:
            return a
        else:
            maxChildIndex = a.index(maxChild)
            a[i], a[maxChildIndex] = a[maxChildIndex], a[i]
            return siftDown(a, maxChildIndex)

# Делаем кучу
for i in range(N//2, -1, -1):
    a = siftDown(a, i)

print("Куча:", a)

# Сортируем
for k in range(N, 0, -1):
    a[0], a[k - 1] = a[k - 1], a[0]
    a = siftDown(a[:k - 1], 0) + a[k - 1:]

print("Стало:", a)