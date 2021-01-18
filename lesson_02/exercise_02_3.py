user_answer = int(input('Введите любой номер месяця в виде целого числа: '))

period = ['зиме', 'весне', 'лету', 'осени']
month = {1: 'Январь',
         2: 'Февраль',
         3: 'Март',
         4: 'Апрель',
         5: 'Май',
         6: 'Июнь',
         7: 'Июль',
         8: 'Август',
         9: 'Сентябрь',
         10: 'Октябрь',
         11: 'Ноябрь',
         12: 'Декабрь'}

if user_answer <= 2 or user_answer == 12:
    print(f'{month.get(user_answer)} относится к {period[0]}')
elif user_answer == 3 or user_answer == 4 or user_answer == 5:
    print(f'{month.get(user_answer)} относится к {period[1]}')
elif user_answer == 6 or user_answer == 7 or user_answer == 8:
    print(f'{month.get(user_answer)} относится к {period[2]}')
else:
    print(f'{month.get(user_answer)} относится к {period[3]}')
