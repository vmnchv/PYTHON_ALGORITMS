#1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
#
#Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
import cProfile

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
#print (factorial(7))
#python -m timeit -n 100 -s "import test1" "test1.factorial(10)"
#100 loops, best of 5: 2.69 usec per loop

cProfile.run('factorial(10)')

#14 function calls (4 primitive calls) in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
 #    11/1    0.000    0.000    0.000    0.000 test1.py:3(factorial)
 #       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

