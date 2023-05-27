lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for itm in lst:
    lst2 = itm.split()
    print("Привет", lst2[-1].capitalize())
    print("Привет", lst2[-1].title())
    
    #print(lst2)
    
#print(dir(str))