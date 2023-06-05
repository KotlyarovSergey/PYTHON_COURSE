# 5.3[35]. Напишите функцию, которая принимает число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя нацело: 1 и само число
# Если число простое - функция возвращает True, если нет - возвращает False
# Примеры/Тесты:
# <function_name>(13) -> True
# <function_name>(10) -> False

def simple(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

print(1,simple(1))
print(2,simple(2))
print(3,simple(3))
print(4,simple(4))
print(5,simple(5))
print(6,simple(6))
print(33,simple(33))
print(34,simple(34))
print(35,simple(35))
print(36,simple(36))
print(37,simple(37))
