# 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :
#     - Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# 	Напишите функцию
# 	- Аргументы: три указанных параметра
# 	- Возвращает: список элементов арифмитической прогрессии.
# 	Примеры/Тесты:
# 	Ввод: 7 2 5
# 	Вывод: [7 9 11 13 15]
# 	Ввод: 2 3 12
# 	Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

# ```(*)``` **Усложнение.** Для формирования списка внутри функции используйте Comprehension
# ```(**)``` **Усложнение.** Присвоение значений переменным a1,d,n запишите, используя только один input, в одну строку, вам понадобится распаковка и Comprehension или map


def a_progress(a1: int, d: int, n: int) -> list:
    res = []
    for el_ind in range(1, n+1):
        res.append(a1+(el_ind-1)*d)
    return res

def a_progress2(a1: int, d: int, n: int) -> list:
    return [a1+(el_ind-1)*d for el_ind in range(1, n+1)]

print(a_progress2(7, 2, 5))
print(a_progress2(2, 3, 12))

a1, d, n = [int(item) for item in input("введите через пробел a1,d,n: ").split()]
print (a_progress2(a1, d, n))