# 1
def double_result(func):
    def inner(a, b):
        return func(a, b) * 2

    return inner


def add_1(a, b):
    return a + b


@double_result
def add_1(a, b):
    return a + b


print(add_1(5, 5))


# 2
def only_odd_parameters(func):
    def inner(*args):
        for i in args:
            if i % 2 != 0:
                return func(*args)
            else:
                return "Please use only odd numbers!"

    return inner


@only_odd_parameters
def add_2(a, b):
    return a + b


print(add_2(5, 5))
print(add_2(4, 4))


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(9, 1, 7, 5, 3))
print(multiply(2, 4, 1, 6, 9))


# 3

def logged(func):
    def inner(*args):
        print(f'You called func{args}')
        result = func(*args)
        return result

    return inner


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


# 4
def type_check(correct_type):
    def type_decorator(func):
        def inner(*args):
            if type(*args) == correct_type:
                return func(*args)
            else:
                return f"Wrong Type: {type(*args)}"

        return inner

    return type_decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
