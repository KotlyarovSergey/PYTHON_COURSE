# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.  
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.

#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
#     Output: 10

lst = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = int(input('введите Х: '))
# x = 5

if x in lst:
    print(x)
else:
    d_min = abs(lst[0]-x)
    near = lst[0]
    for n in lst:
        if abs(n-x) < d_min:
            d_min = abs(n-x)
            near = n
    print(near, end=" ")
