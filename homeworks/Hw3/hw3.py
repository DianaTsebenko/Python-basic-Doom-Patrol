import functools

# 1
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a))
# #9790720
print(id(str_b))
# #139839115447024
print(id(set_c))
# #140640987957504
print(id(lst_d))
# #139969279143488
print(id(dict_e))
# #140647959630400

# 2
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
# 140192594832960

# 3
print(type(int_a))
# #<class 'int'>
print(type(str_b))
# #<class 'str'>
print(type(set_c))
# #<class 'set'>
print(type(lst_d))
# #<class 'list'>
print(type(dict_e))
# #<class 'dict'>


# 4
print(isinstance(int_a, int))
# True
print(isinstance(str_b, str))
# True
print(isinstance(set_c, set))
# True
print(isinstance(lst_d, list))
# True
print(isinstance(dict_e, dict))
# True


# 5
print("Anna has {} apples and {} peaches.".format(3, 7))
# Anna has 3 apples and 7 peaches.

# 6
print("Anna has {0} apples and {1} peaches.".format("one", "two"))
# Anna has one apples and two peaches.


# 7
print("Anna has {a} apples and {b} peaches.".format(a="eight", b="five"))
# Anna has eight apples and five peaches.


# 8
print("Anna has {0:4} apples and {1:3} peaches.".format("ten", "four"))
# Anna has ten  apples and four peaches.


# 9
a = 10
b = 7
print(f"Anna has {a} apples and {b} peaches.")
# Anna has 10 apples and 7 peaches.

# 10
a = 5
b = 2
print("Anna has %d apples and %d peaches." % (a, b))
# Anna has 5 apples and 2 peaches.


# 11
a = 7
b = 4
data_dict = {"c": a, "d": b}
print("Anna has %(c)d apples and %(d)d peaches." % data_dict)
# Anna has 7 apples and 4 peaches.


# 12
lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]


# 13
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension)
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]


# 14
dict_comprehension = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comprehension)
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}


# 15
dict_comprehension = {num: (num ** 2 if num % 2 == 1 else num // 0.5) for num in range(1, 11)}
print(dict_comprehension)
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}


# 16
dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
print(dict_comprehension)
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}


# 17
dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
    else:
        dict_comprehension[x] = x
print(dict_comprehension)
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}


# 18
foo = lambda x, y: x if x < y else y
print(foo(3, 5))


# 3


# 19
def foo(x, y, z):
    if x < y and x > z:
        return z
    else:
        return y


print(foo(3, 5, 7))
# 5


# 20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
# [1, 5, 13, 15, 18, 24, 33, 55]


# 21
print(sorted(lst_to_sort, reverse=True))
# [55, 33, 24, 18, 15, 13, 5, 1]


# 22
lst = list(map(lambda x: x * 2, lst_to_sort))
print(lst)
# [10, 36, 2, 48, 66, 30, 26, 110]


# 23
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_AB = list(map(lambda x, y: x ** y, list_A, list_B))
print(list_AB)
# [32, 729, 16384]


# 24
suma = (lambda x, y: x + y)
result = functools.reduce(suma, lst_to_sort)
print(result)
# 164


# 25
lst_fl = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(lst_fl)
# [5, 1, 33, 15, 13, 55]


# 26
lst_n = list(filter(lambda x: x < 0, range(-10, 10)))
print(lst_n)
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]


# 27
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
list_cm = list(filter(lambda x: x in list_1, list_2))
print(list_cm)
# [2, 3, 5, 7]
