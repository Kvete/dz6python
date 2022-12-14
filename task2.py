"""
1)      Cделали замеры памяти для массива и сжали его в json str
        Вывод: убедились что json str сильно экономит память (в 5-10 раз)
2)      Cделали замеры памяти выделяемого для  массива и для генератора
        на одинаковое количество  элементов.
        Вывод: убедились что генератор занимает на порядки меньше памяти
        нежели массив
"""
from json import dumps
from pympler import asizeof

input_array = list(range(10000))
input_array1 = dumps(input_array)
print(type(input_array))
print(type(input_array1))
print(
    f'экономия памяти (list/json.str): '
    f'{asizeof.asizeof(input_array) / asizeof.asizeof(input_array1)} раз')

print("====================================")
new_array = (el for el in range(10000))
new_array1 = list(range(10000))
print(type(new_array))
print(type(new_array1))
print(f'экономия памяти (list/generator): '
      f'{asizeof.asizeof(new_array1) / asizeof.asizeof(new_array)} раз')
