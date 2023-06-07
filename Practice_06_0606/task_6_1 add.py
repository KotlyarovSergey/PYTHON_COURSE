from time import perf_counter
from random import randint

def difference_list(list1: list, list2: list) -> list:
    t1 = perf_counter()
    res = [itm for itm in list1 if itm not in list2]
    t2 = perf_counter()
    return t2-t1

def difference_set(list1: list, list2: list) -> list:
    t1 = perf_counter()
    set_list2 = set(list2)
    res = [itm for itm in list1 if itm not in set_list2]
    t2 = perf_counter()
    return t2-t1


n = 10000
list_1 = [randint(0, n) for i in range(n)]
list_2 = [randint(0, n) for i in range(n)]
print(f" SET: {difference_set(list_1, list_2):2e}")
print(f"LIST: {difference_list(list_1, list_2):2e}")
