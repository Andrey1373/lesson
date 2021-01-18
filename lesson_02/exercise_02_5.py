user_answer = int(input('Введите число: '))

my_list = list([7, 5, 3, 1])
my_list.append(user_answer)
my_list.sort(key=int, reverse=True)
print(my_list)
