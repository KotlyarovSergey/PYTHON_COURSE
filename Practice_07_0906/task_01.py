# 7.1[###]. Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО
# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич
# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович
# 2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# [*] Усложнение. Файл находится в поддиретории data текущей директории. 
# Сформировать путь к нему с использованием os.path и pathlib

from io import open
from os.path import join, abspath, dirname
from os import getcwd
from pathlib import Path


MAIN_DIR = abspath(dirname(__file__))
print(MAIN_DIR)
print(getcwd())

file = open('fio.scv',  'r', encoding='utf-8')
file.close()

list_1 = []
with open('fio.scv',  'r', encoding='utf-8') as f:
    s = f.readline()
    while(len(s)>0):
        name, last_name, sur_name = s.strip().split('#')
        print(name, last_name, sur_name)
        list_1.append([name,last_name,sur_name])
        s = f.readline()
        
#print(dir(str))
print()
print(list_1)
print()

# file_path = join('.', 'data','fio.scv')
file_path = join(MAIN_DIR, 'data','fio.scv')
print(file_path)
with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip().split('#'))
print()

# file_path=Path('.', 'data','fio.scv')
file_path=Path(MAIN_DIR, 'data','fio.scv')
print(file_path)
with open(file_path, 'r', encoding='utf-8') as f:
    print(f.readline())
print()
