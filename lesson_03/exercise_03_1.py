def division():
    while True:
        number_1 = float(input('Введите число: '))
        number_2 = float(input('Введите число: '))
        if number_1 == 0 or number_2 == 0:
            print('На ноль делить нельзя. Повторите ввод данных')
        else:
            c = number_1 / number_2
            break
    return c


print(division())
