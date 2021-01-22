def user_data(a, b, c, d, e, f):
    print(f'Данные о пользователе: имя - {a}; фамилие - {b}; год рождения - {c}; '
          f'город проживания - {d}; адрес электронной почты - {e}; номер телефона - {f}')


name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
birth = int(input('Введите год рождения: '))
city = input('Введите город проживания: ')
mail = input('Введите почтовый адрес: ')
mobile = int(input('Введите номер телефона: '))

user_data(a=name, b=last_name, c=birth, d=city, e=mail, f=mobile)
