value = list(input('Введите буквы или цифры: '))

for i in range(0, len(value) - 1, 2):
    value[i], value[i + 1] = value[i + 1], value[i]
print(' '.join(value))
