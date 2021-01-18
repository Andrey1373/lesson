specifications_product = {'name_product': None,
                          'product_price': None,
                          'quantity_product': None,
                          'unit_product': 'шт.'}

i = 0
today_specifications = []
analytics_product = {}

while True:
    specifications_product['name_product'] = input('Введите название товара: ')
    specifications_product['product_price'] = int(input('Введите цену товара: '))
    specifications_product['quantity_product'] = int(input('Введите количество товара: '))
    i += 1
    today_specifications.append(tuple([i, specifications_product.copy()]))
    continue_check = input("Продолжить (да/нет): ")
    if continue_check.lower() == 'нет':
        break

for today_analytics in today_specifications:
    for key, value in today_analytics[1].items():
        if key in analytics_product:
            analytics_product[key].append(value)
        else:
            analytics_product[key] = [value]

print(f'Введены следующие товары: {today_specifications}')
print(f'Собрана следующая аналитика: {analytics_product}')
