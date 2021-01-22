def my_sum():
    sum_number = 0
    ex = True
    while ex:
        number = input('Введите числа через пробел или букву q для выхода: ').split()
        i = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = False
                break
            else:
                i = i + int(number[el])
        sum_number = sum_number + i
        print(f'Текущая сумма {sum_number}')
    print(f'Окончательная сумма {sum_number}')


my_sum()
