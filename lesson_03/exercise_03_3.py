def my_func(a, b, c):
    value = [a, b, c]
    z = min(a, b, c)
    value.remove(z)
    return sum(value)


print(my_func(-2, 10, 1))
