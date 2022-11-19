# Задача 2

month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль' , 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

day_list = list(range(1, 32))
day_list_31 = ['январь', 'март', 'май', 'июль' , 'август', 'октябрь', 'декабрь']
day_list_30 = ['апрель', 'июнь', 'июль' , 'сентябрь', 'ноябрь']

print('Здравствуйте! Чтобы узнать свой знак зодиака, следуйте инструкциям.')
print()

month = input('Введите месяц: ').lower()

while month not in month_list:
    print('Ввeдите правильно название месяцa!')
    month = input('Введите месяц: ').lower()

day = int(input('Введите число: '))

while day <1 or (month in day_list_31 and day > 31) or (month in day_list_30 and day > 30) or (month == 'февраль' and day > 29):
    print('Число должно соответствовать количеству дней в месяце!')
    day = int(input('Введите число: '))

		
if  (22 <= day <= 31 and month == 'декабрь') or (1 <= day <= 20 and month == 'январь'):
    print('Козерог')
    
if (21 <= day <= 31 and month == 'январь') or (1 <= day <= 19 and month == 'февраль'):
    print('Водолей')
    
if (20 <= day <= 29 and month == 'февраль') or (1 <= day <= 20 and month == 'март'):
    print('Рыбы')
        
if (21 <= day <= 31 and month == 'март') or (1 <= day <= 20 and month == 'апрель'):
    print('Овен')
    
if (21 <= day <= 30 and month == 'апрель') or (1 <= day <= 20 and month == 'май'):
    print('Телец')

if (21 <= day <= 31 and month == 'май') or (1 <= day <= 21 and month == 'июнь'):
    print('Близнецы')

if (22 <= day <= 30 and month == 'июнь') or (1 <= day <= 22 and month == 'июль'):
    print('Рак')

if (23 <= day <= 31 and month == 'июль') or (1 <= day <= 23 and month == 'август'):
    print('Лев')

if (24 <= day <= 31 and month == 'август') or (1 <= day <= 23 and month == 'сентябрь'):
    print('Дева')

if (24 <= day <= 30 and month == 'сентябрь') or (1 <= day <= 23 and month == 'октябрь'):
    print('Весы')

if (24 <= day <= 30 and month == 'октябрь') or (1 <= day <= 22 and month == 'ноябрь'):
    print('Скорпион')

if (23 <= day <= 30 and month == 'ноябрь') or (1 <= day <= 21 and month == 'декабрь'):
    print('Стрелец')
