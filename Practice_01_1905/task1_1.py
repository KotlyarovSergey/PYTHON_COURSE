'''
№1.1[1]. За день машина проезжает n километров.
Сколько дней нужно, чтобы проехать маршрут длиной m километров?
Реализуйте пользовательский ввод данных и вывод внятного результата. Используйте .format() или f-строки
Примеры/Тесты:
    n = 700, m = 750  -> Чтобы проехать 750км машине потребуется 2дн
    n = 700, m = 600  -> Чтобы проехать 600км машине потребуется 1дн
    n = 700, m = 1400 -> Чтобы проехать 1400км машине потребуется 2дн

Усложнение[*]. Использовать тернарный оператор

'''

n = int(input("Сколько за день машина проезжает километров? "))
m = int(input("Длинна маршрута, километров: "))
t = m//n

# if(m%n > 0):
#     t+=1

t = m//n if m%n == 0 else m//n+1
t = -(-m//n)
print(f"Чтобы проехать {m}км машине потребуется {t}дн")
