# №4.1[25]. Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Примеры/Тесты:
# 
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
          
# 
# Input: a b c d a a a a a a a
# Output: a b c d a_1 a_2 a_3 a_4 a_5 a_6 a_7
# Строку не обязательно вводить с клавиатуры

data = "aaabcaadcdd"
result = []
for ind, val in enumerate(data):
    n = data[0:ind].count(val)
    result.append(f"{val}_{n}" if n > 0 else  val)
    # if n>0:
    #     result.append(f"{val}_{n}")
    # else:
    #     result.append(val)
print(" ".join(result))        


result.clear()
d = dict()
for ind, val in enumerate(data):
    if val in d.keys():
        d[val] += 1
        result.append(f"{val}_{d[val]}")
    else:
        d[val] = 0
        result.append(val)

print(d)
print(" ".join(result))


input_String ="a b c d a a a a a a a" 
amount_of_letters = dict()
output_String =""
for el in input_String:
    if el!=" ":
        if el not in amount_of_letters:
            amount_of_letters[el]=1
            output_String+=  el
        else:
            output_String+= el + "_" + str(amount_of_letters[el])
            amount_of_letters[el] +=1            
    else:
        output_String=output_String+el
print(output_String)



