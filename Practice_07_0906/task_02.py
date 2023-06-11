# 7.2[###]. Продолжение предыдущей задачи
# Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# необходимо преобразовать к виду:
# Иванов И.И.
# Петров П.П.
# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# [*] Усложнение. Данные необходимо записать в два разных файла:
# В первый - в виде Иванов И.И.
# Во второй - в виде Иванов-И-И
# [*****] Усложнение. Вам известно, что (в перспективе) подобных спецификаций может быть много. Не две, а пять или десять
# Как улучшить свой код в этом случае, сделать его легко расширяемым?

from os.path import join, abspath, dirname

MAIN_DIR = abspath(dirname(__file__))
file_path = join(MAIN_DIR, 'data', 'fio.scv')
list_1 = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        fam, imya, otch = line.strip().split('#')
        # print(fam, imya, otch)
        list_1.append([fam, imya, otch])
print(list_1)
        
file_path = join(MAIN_DIR, 'rezults', 'rezult1.scv')
with open(file_path, mode='wt',encoding='utf-8') as file:
    # file.write(str(list_1))
    for line in list_1:
        txt = f"{line[0]} {line[1][0]}.{line[2][0]}.\n"
        file.write(txt)

file_path = join(MAIN_DIR, 'rezults', 'rezult2.scv')
with open(file_path, mode='wt', encoding='utf-8') as file:
    # file.write(str(list_1))
    for fam, imya, otch in list_1:
        # txt = f"{line[0]}-{line[1][0]}-{line[2][0]}\n"
        file.write(f"{fam}-{imya[0]}-{otch[0]}\n")