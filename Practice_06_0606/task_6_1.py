# 1[39]. Даны два списка чисел. Требуется вывести те элементы первого списка , которых нет во втором списке.
# Создайте функцию.
# Аргументы: два списка целых чисел
# Возвращает: список элементов (смотри условие)
# Примеры/Тесты:
# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [2, 3, 12]
# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3,4]
# [*] Усложнение. Элементы необходимо возвращать в том порядке, в котором они находятся в первом списке, с учетом повторений
# Примеры/Тесты:
# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [3, 3, 2, 12]
# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3, 4, 3, 4]

from time import perf_counter
from random import randint

def difference_lists (list1: list, list2: list) -> list:
    # set1 = set(list1)
    # set2 = set(list2)
    # set3 = set1.difference(set2)
    # list_result = list(set3)
    # return list_result
    t1 = perf_counter()
    res = list(set(list1)-set(list2))
    t2 = perf_counter()
    return t2-t1, res

def diff_lists_hard(list1: list, list2: list) -> list:
    set_list2 = set(list2)
    list_result = list()
    for itm in list1:
        if itm not in set_list2:
            list_result.append(itm)
    return list_result



list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1]
print(difference_lists(list_1, list_2))

list_1 = [3, 4, 1, 5, 1, 3, 10, 4, 9, 5]
list_2 = [9, 6, 6, 5, 10, 1, 10, 9, 1, 5]
print(difference_lists(list_1, list_2))

print(diff_lists_hard([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1]))
print(diff_lists_hard([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5]))

n = 100
list_1 = [randint(0, n) for i in range(n)]
list_2 = [randint(0, n) for i in range(n)]