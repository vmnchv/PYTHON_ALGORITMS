#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random
N = 15
arr = [0]*N
for i in range(N):
    arr[i] = int(random()*100)
    print(arr[i], end = ' ')
print()