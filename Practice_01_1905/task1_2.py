'''
№1.2[3]. В некоторой школе решили набрать три новых математических класса и оборудовать 
кабинеты для них новыми партами.
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
Выведите наименьшее число парт, которое нужно приобрести для них.
Примеры/Тесты:
    20 21 22(ввод чисел НЕ в одну строку)  -> Общее кол-во парт будет 32
    21 21 21(ввод чисел НЕ в одну строку)  -> Общее кол-во парт будет 33
'''

cl1 = int(input("Учеников в 1 классе "))
cl2 = int(input("Учеников в 2 классе "))
cl3 = int(input("Учеников в 3 классе "))
table1 = -(-cl1//2)
table2 = -(-cl2//2)
table3 = -(-cl3//2)
tables = -(-cl1//2 + -cl2//2 + -cl3//2)
print(table1+table2+table3)
print(tables)