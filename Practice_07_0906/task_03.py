# 7.3[###]. Имея список вида [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# преобразовать его в списки вида
# 1) ['Иванов-И-И', 'Петров-П-П', 'Соколов-И-Г'...]
# 2) ['Иванов И.И.', 'Петров П.П.', 'Соколов И.Г.'...]
# с использованием Comprehension; Comprehension + функция; Comprehension + lambda; map
# [**] Усложнение. Дополнить обработку списка условием: Выбираем только те элементы, в которых первая буква П

list_1 = [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович'], ['Соколов', 'Илья', 'Григорьевич']]
list_result = []
# for f,i,o in list_1:
#     list_result.append(f"{f}-{i[0]}-{o[0]}")


list_result = [f"{f}-{i[0]}-{o[0]}" for f,i,o in list_1]
print(list_result)

list_result = [f"{f}-{i[0]}-{o[0]}" for f,i,o in list_1 if f[0]=='П' or i[0]=='П' or o[0]=='П']
print(list_result)

# list_1 = list(map(lambda x: x + 10, list_1))
# list_result = list(map(lambda f,i,o: f"{f}-{i[0]}-{o[0]}", list_1))
list_result = list(map(lambda x: f"{x[0]}-{x[1][0]}-{x[2][0]}", list_1))
print(list_result)