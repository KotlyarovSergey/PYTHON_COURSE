# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
    
# 	Примеры/Тесты:
#     <function_name>(0,0) -> 0
#     <function_name>(0,2) -> 2
#     <function_name>(3,0) -> 3


def sum(a, b):
    if a == b == 0:
        return a
    else:
        dif = sum(a, b-1) if a < b else sum(a-1, b)
        return dif + 1
        
print(sum(0, 4))
print(sum(1, 4))
print(sum(2, 4))
print(sum(8, 2))
print(sum(8, 0))
