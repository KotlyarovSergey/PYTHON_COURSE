# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.  
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.

#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
#     Output: 10

list_1 = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = int(input('введите число: '))

nier = list_1[0]
d_min = list_1[0] - x if list_1[0] - x > 0 else x - list_1[0]
for n in list_1:
    d = n - x if n - x > 0 else x - n
    if d < d_min:
        nier = n

print(nier)
