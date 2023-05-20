'''
1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет 
счастливость билета.

	Примеры/Тесты:
	385916 >>> yes
	123456 >>> no

```(*)``` **Усложнение.** Вывод результат на экран сделайте одной строкой(только один print), для этого используйте 
тернарный оператор
'''

ticket = int(input("Номер билета: "))
rightSum =  ticket % 10 + ticket // 10 % 10 + ticket // 100 % 10 
leftSum = ticket // 1000 % 10 + ticket // 10000 % 10 + ticket // 100000 % 10

if(ticket > 100000 and ticket < 999999):
    if leftSum == rightSum:
        print(f"{ticket} >>> yes")
    else:
        print(f"{ticket} >>> no")
else:
    print("error")

# (*)
result = "yes" if leftSum == rightSum else "no"
print(f"{ticket} >>> {result}")