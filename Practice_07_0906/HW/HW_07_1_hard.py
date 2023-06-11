# ```(*)``` **Усложнение.**

# Функция имеет параметр, который определяет, надо ли возвращать полную информацию о кол-ве гласных букв в фразах. Эта информация возвращается в виде списка словарей. Каждый элемент списка(словарь) соответствует фразе.
    
# 	Примеры/Тесты:
# 		<function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
# 	    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
# 	    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
# 	    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
# 	    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
# 	    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])

# а, е, ё, и, о, у, ы, э, ю, я

def vowel_count(txt: str) -> dict:
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
    result = dict()
    for itm in vowels:
        count = txt.count(itm)
        if count > 0:
            result[itm] = txt.count(itm)
    return result


def check_sum(obj: list):
    sum_values = sum(obj[0].values())
    for ind in range(1, len(obj)):
        if sum_values != sum(obj[ind].values()):
            return False
    return True
    

def rhyme(text: str, full_info: bool):
    words = text.split()
    if len(words) == 0: return None     # пустая строка
    
    count_dict_list = []
    for w in words:
        count_dict_list.append(vowel_count(w))
    
    result = check_sum(count_dict_list)
    if full_info:
        result = (result, count_dict_list)
    
    return result


print(rhyme("пара-ра-рам рам-пам-папам па-ра-па-дам", False))
print(rhyme("пара-ра-рам рам-пам-папам па-ра-па-дам", True))
print(rhyme("пара-ра-рам рам-пум-пупам па-ре-по-дам",True))
print(rhyme("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па",True))
print(rhyme("Пам-парам-пурум Пум-пурум-карам",True))
