# №3.3[21]. Напишите программу для печати всех уникальных значений в списке словарей.
# Примечание: Список словарей задан изначально. Пользователь его не вводит
# Обратите внимание, что в словарях может быть один или несколько элементов
#     Примеры/Тесты:
#     Input:  [{"V": "S001", "X": "D009"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005", "XI": "D011"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 ", "XII": "D001"}]
#     Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# [*]  Усложнение. Проверку уникальности строк сделайте без учета пробелов до и после значимой части строки
# [**] Усложнение. Запишите алгоритм в одну строку, используйте Comprehension

list_1 = [{"V": "S001", "X": "D009"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005", "XI": "D011"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 ", "XII": "D001"}]
unique = set()
for dct in list_1:
    # print(type(dct))
    # print(dct)
    for k, v in dct.items():
        # print(k, v)
        unique.add(v.strip())
print(unique)

unique.clear()
for dct in list_1:
    for itm in dct.items():
        # print(itm)
        unique.add(itm[-1].strip())
print(unique)

unique.clear()
for dct in list_1:
    for v in dct.values():
        # print(v)
        unique.add(v.strip())
print(unique)


unique.clear()
unique = {v.strip() for dct in list_1 for k, v in dct.items()}
print(unique)

unique.clear()
unique = {itm[-1].strip() for dct in list_1 for itm in dct.items()}
print(unique)

unique.clear()
unique = {v.strip() for dct in list_1 for v in dct.values()}
print(unique)