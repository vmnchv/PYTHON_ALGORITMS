import cProfile
import functools

def eratosphen(n):

   s = [x for x in range(2, n) if x not in [i for sub in [list(range(2 * j, n, j)) for j in range(2, n // 2)] for i in sub]]

   return s

cProfile.run('eratosphen(100)')
102 function calls in 0.002 seconds

  Ordered by: standard name

  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       1    0.000    0.000    0.003    0.003 <string>:1(<module>)
       1    0.000    0.000    0.003    0.003 DZ4_23.py:4(eratosphen)
      98    0.002    0.000    0.002    0.000 DZ4_23.py:6(<listcomp>)
       1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} 





----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 


import cProfile
import functools
def primes(n):
   a = [0] * n  # создание массива с n количеством элементов
   for i in range(n):  # заполнение массива ...
       a[i] = i  # значениями от 0 до n-1

   # вторым элементом является единица, которую не считают простым числом
   # забиваем ее нулем.
   a[1] = 0

   m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
   while m < n:  # перебор всех элементов до заданного числа
       if a[m] != 0:  # если он не равен нулю, то
           j = m * 2  # увеличить в два раза (текущий элемент простое число)
           while j < n:
               a[j] = 0  # заменить на 0
               j = j + m  # перейти в позицию на m больше
       m += 1

   # вывод простых чисел на экран (может быть реализован как угодно)
   b = []
   for i in a:
       if a[i] != 0:
           b.append(a[i])

   del a
   return b

cProfile.run('primes(100)')

29 function calls in 0.000 seconds

  Ordered by: standard name

  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       1    0.000    0.000    0.000    0.000 DZ4_222.py:3(primes)
       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} 


