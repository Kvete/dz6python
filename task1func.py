def my_array1():
    result = []
    for i in range(1000):
        result = result + [i]
    return sum(result)


def my_array2():
    result = []
    for i in range(1000):
        result.append(i)
    return sum(result)


def my_array3():
    result = [el for el in range(1000)]
    return sum(result)


data = [4, 5, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 332, 324, 543, 467, 786, 89, 98,
        345, 234, 123, 43, 432, 1234, 123, 5432, 32421, 43, 54325, 453454, 34,
        432, 34, 4, 54353425435345, 5435342, 4354354, 5345342, 4, 34, 123, 32]


def my_sum1(data):
    return sum(data)


def my_sum2(data):
    res = 0
    for el in data:
        res += el
    return res
