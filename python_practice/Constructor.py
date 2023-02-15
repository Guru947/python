def hey():
    print('hey')
    print('hello')


def add(a, b):
    c = a + b
    return c


result = add(2, 4)
print(result)


def add_sub(a, b):
    c = a + b
    d = a - b
    return c, d


result1, result2 = add_sub(4, 7)
print(result1, result2)

hey()
