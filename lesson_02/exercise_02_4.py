user_answer = input('Введите несколько слов, разделяя слова пробелом: ').split()
print(user_answer)

for i, el in enumerate(user_answer, 1):
    print(i, el[: 10])
