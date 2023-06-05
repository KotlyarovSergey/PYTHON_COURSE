# 5.2[33]. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите функцию, которая заменяет оценки, переданные в виде списка, но наоборот: все максимальные – на минимальные.
# Функция должна возвращать новый список оценок
# Примечание: Обратите внимание на side effects функции.

# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 4, 2, 5, 5, 2]) -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None
# Примеры/Тесты:
# <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None

# [**] Усложненение: Добавьте параметр в функцию, который определит как будут заменены оценки:
# Друзьям минимальные на максимальные, Врагам - наоборот.
# Примеры/Тесты:
# grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "friend") -> [5, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "enemy") -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

def find_min(nums):
    m = nums[0]
    for i in range(1, len(nums)):
        if m > nums[i]:
            m = nums[i]
    return m

def find_max(nums):
    m = nums[0]
    for i in range(1, len(nums)):
        if m < nums[i]:
            m = nums[i]
    return m

def replase_values(nums, relation):
    minimal = find_min(nums)
    maximal = find_max(nums)
    if(minimal == maximal):
        return None
    
    if relation == "enemy":
        for i in range(len(nums)):
            if nums[i] == maximal:
                nums[i] = minimal
    elif relation == "friend":
        for i in range(len(nums)):
            if nums[i] == minimal:
                nums[i] = maximal
    else:
        return None
    
    return  nums



grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]
print(replase_values(grades, 'enemy'))
grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]
print(replase_values(grades, 'friend'))
grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]
print(replase_values(grades, 'friendd'))
grades = [3, 3, 3, 3, 3, 3, 3, 3, 3]
print(replase_values(grades, 'friend'))
grades = [5, 5, 5, 5, 5, 5, 5, 5, 5]
print(replase_values(grades, 'enemy'))
