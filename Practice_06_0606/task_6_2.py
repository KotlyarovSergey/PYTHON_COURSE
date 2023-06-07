# 6.2[41] Дан список, целых чисел.
# Напишите функцию, которая определит те элементы списка, у которых два соседних и, при этом, 
# оба соседних элемента меньше данного.
# Функция
# Аргументы: список целых чисел
# Возвращает: список элементов (смотри условие)
# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 5]) -> [5]
# <function_name>([1, 5, 1, 6, 1]) -> [5,6]
# <function_name>([7, 5, 1, 6, 8]) -> [8]
# <function_name>([8, 1, 5, 4, 5]) -> [8,5]

def neighbours(data: list) -> list:
    list2 = data + [data[0]]
    res = list()
    for i in range(0, len(list2)-1):
        if list2[i-1] < list2[i] and list2[i+1] < list2[i]:
            res.append(list2[i])
    return res

def neighbours2(data: list) -> list:
    res = list()
    for i in range(0, len(data)):
        nex_idx = 0 if i == len(data)-1 else i+1
        if data[i-1] < data[i] and data[nex_idx] < data[i]:
            res.append(data[i])
    return res

def neighbours3(data: list) -> list:
    res = list()
    for i in range(0, len(data)-1):
        if data[i-1] < data[i] > data[i+1]:
            res.append(data[i])
    idx = len(data)-1
    if data[idx-1] < data[idx] > data[0]:
            res.append(data[i])
    return res


print(neighbours3([1, 3, 3, 3, 5]))
print(neighbours3([1, 5, 1, 6, 1]))
print(neighbours3([7, 5, 1, 6, 8]))
print(neighbours3([8, 1, 5, 4, 5]))

