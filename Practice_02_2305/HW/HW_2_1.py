
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2


n = int(input("Введите кол-во монет>? "))
r = 0
a = 0
for i in range(n):
    if input(f"Положение монеты {i}: 0 или 1>? ") == "0":
        r += 1
    else:
        a += 1
    
min = r if r < a else a
print(f"Кол-во монет, чтобы перевернуть: {min}")

