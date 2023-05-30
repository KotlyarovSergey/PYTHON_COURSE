# 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Если таких чисел нет - выдать внятное диагностическое сообщение

# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры
    
# 	Примеры/Тесты:
#     Input1: 2 4 6 8 10 12 10 8 6 4 2
#     Input2: 3 6 9 12 15 18
#     Output: 6 12     Обратите внимание: Без скобочек, в одну строку

#     Input1: 2 4 6 8 10 10 8 6 4 2
#     Input2: 3 9 12 15 18
#     Output: Повторяющихся чисел нет

input1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
input2 = [3, 6, 9, 12, 15, 18]

# input1 = [2, 4, 6, 8, 10, 10, 8, 6, 4, 2]
# input2 = [3, 9, 12, 15, 18]


list_intesect = list(set(input1).intersection(set(input2)))
list_intesect.sort()
list_str = [str(i) for i in list_intesect]
answer = " ".join(list_str) if len(list_str) > 0 else "Повторяющихся чисел нет"
print(answer)
 

