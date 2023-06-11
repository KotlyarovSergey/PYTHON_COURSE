# 6.2[32]: Напишите функцию ```print_operation_table(operation, num_rows=6, num_columns=6)```, 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, 
# т.е. функцию двух аргументов. Аргументы ```num_rows``` и ```num_columns``` указывают число строк и 
# столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
	
# 	Примеры/Тесты:
#     print_operation_table(lambda x,y: x**y,4,4)
# 	1   1   1   1
# 	2   4   8  16
# 	3   9  27  81
# 	4  16  64 256

#     print_operation_table(lambda x,y: x*y)
# 	1   2   3   4   5   6
# 	2   4   6   8  10  12
# 	3   6   9  12  15  18
# 	4   8  12  16  20  24
# 	5  10  15  20  25  30
# 	6  12  18  24  30  36



def print_operation_table(operation, num_rows=6, num_columns=6):
    result = ''
    for r in range(1, num_rows+1):
        for c in range(1, num_columns+1):
            result += f"{str(operation(r,c)):3}" + ' '
        result += '\n'
    print (result)


def to_length(s: str, n: int) -> str:
    result = s
    for ind in range(n - len(s)):
        result = ' '+ result
    return result


def max_length(matrix: list) -> list:
    result = [0 for i in range(len(matrix[0]))]
    for line in matrix:
        for ind in range(len(line)):
            if len(line[ind]) > result[ind]:
                result[ind] = len(line[ind])
    return result


def print_operation_table2(operation, num_rows=6, num_columns=6):
    result_str = []
    for r in range(1, num_rows+1):
        line = []
        for c in range(1, num_columns+1):
            line.append(str(operation(r,c)))
        result_str.append(line)
    # print (result_str)
    width = max_length(result_str)
    print_format(result_str, width)


def print_format(matrix: list, width: list)->None:
    result = ''
    for line in matrix:
        # print(line)
        for ind in range(len(line)):
            # print(line[ind])
            result += to_length(line[ind], width[ind]) + ' '
        result += '\n'
    print (result)



print_operation_table(lambda x,y: x**y,4,4)
print_operation_table2(lambda x,y: x**y,4,4)

# print_operation_table(lambda x,y: x**y,8,4)
# print_operation_table2(lambda x,y: x**y,8,4)

# print_operation_table(lambda x,y: x*y)
# print_operation_table2(lambda x,y: x*y)