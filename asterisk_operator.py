result = 5*7

print(result)

result = 5**7
print(result)

a_list = [0] * 100
print(a_list)

b_list = ['a', 'b', 'c'] * 100
print(b_list)

a_tuple = (1, 2, 3) * 10
print(a_tuple)

string = "Rajeev" * 10
print(string)


def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg, end=' ')
    print()
    for k, v in kwargs.items():
        print(k, v, end=', ')
    print()


foo(1, 2, 3, 4, 5, 6, z=3, y=10, x=17)


def foo_1(a, b, *, c, d):  # c, d are keyword only parameters
    print(a, b)
    print(c, d)


foo_1(1, 2, c=3, d=4)


def foo_2(a, b, c):
    print(a, b, c)


# number of elements in list must match number of arguments in the function
my_list = [1, 2, 3]
foo_2(*my_list)

# number of elements should be same as parameters count of the function and the name of the keys in dictionary should match the name of the parameters in function
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo_2(**my_dict)


numbers = [1, 2, 3, 4, 5, 6]
# unpacking always returns list doesn't matter what iterable the source is
*beginning, last = numbers
print(beginning)
print(last)

beginning, *last = numbers
print(beginning)
print(last)

beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

a, b, c, d, e, f = numbers
print(a, b, c, d, e, f)


my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)


dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'d': 4, 'e': 5, 'f': 6}

my_dict = {**dict_a, **dict_b}
print(my_dict)
