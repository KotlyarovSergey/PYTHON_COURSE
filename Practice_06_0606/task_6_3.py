# 6.3[43] Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.
# Напишите функцию
# Аргументы: список целых чисел
# Возвращает: кол-во пар
# Примеры/Тесты:
# <function_name>([1, 2, 3, 2, 3]) -> 2
# <function_name>([1, 2, 3, 2, 3, 3, 2, 4]) -> 6

def pairs(data: list) -> list:
    list_set = set(data)
    res = 0
    for itm in list_set:
        count = data.count(itm)
        if count > 1:
            res += count
    return res

def pairs2(data: list) -> list:
    res = 0
    length = len(data)
    for ind in range(length-1):
        for ind2 in range(ind+1, length):
            if data[ind] == data[ind2]:
                res += 1
    return res

def pairs3(data: list) -> list:
    res = 0
    length = len(data)
    for ind in range(length-1):
        res += data[ind+1:].count(data[ind])
    return res

print(pairs3([1, 2, 3, 2, 3]))
print(pairs3([1, 2, 3, 2, 3, 3, 2, 4]))