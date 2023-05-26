'''
Дано натуральное число A > 1. Определите, каким по 
счету числом Фибоначчи оно является, то есть 
выведите такое число n, что φ(n)=A. Если А не 
является числом Фибоначчи, выведите число -1

'''

a = int(input("n: "))
fibo = 1
last = 0
i = 2
while fibo < a:
    #print(f'{i+1}:  {last} + {fibo} = {last+fibo}')
    fibo = fibo + last
    last = fibo - last
    i+=1
    
if fibo == a:
    print(i)
else:
    print(-1)
