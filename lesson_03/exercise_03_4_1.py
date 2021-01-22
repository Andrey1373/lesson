def my_func(x, y):
    i = 0
    c = 1
    while i < y:
        c = c * x
        i += 1
        print(c)
    return 1 / c


number_1 = int(input('Введите целове положительное число: '))
number_2 = abs(int(input('Введите целое отрицательное число: ')))

print(my_func(number_1, number_2))
