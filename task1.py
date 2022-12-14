"""
1)      Cделали замеры времени для заполнения массива 3 способами:
    1-конкатенация
    2-аппенд
    3-LC
        Вывод: убедились что LC работает быстрее всего,
    а конкатенация медленее всего
2)      Cделали замеры времени для суммы элементов массива 2 способами:
    1-встроенная функция sum
    2-цикл
        Вывод: убедились что встроенная фунция работает быстрее
"""

from timeit import timeit

print('конкатенация:')
print(timeit("my_array1()", setup="from task1func import my_array1",
             number=1000))
print('append:')
print(timeit("my_array2()", setup="from task1func import my_array2",
             number=1000))
print('LC:')
print(timeit("my_array3()", setup="from task1func import my_array3",
             number=1000))

print("===================================")
print('встроенная функция sum:')
print(timeit("my_sum1", setup="from task1func import my_sum1,data"))
print('цикл:')
print(timeit("my_sum2", setup="from task1func import my_sum2,data"))
