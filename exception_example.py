# Errors and Exceptions

# syntax error
# a = 5 print(a)

# Exceptions : syntactically correct statements may cause exceptions
# a = 10 + '10'  # gives TypeError exception adding int and string

# import somemodule # gives ModuleNotFoundError

a = 5
# b = c # gives NameError as c is not defined

# f = open("somefile.txt") # FileNotFoundError is popped

a = [1, 2, 3, 4, 5]
a.remove(1)
print(a)

# a.remove(6)  # throws ValueError as 6 is not in the list
# print(a)

# throws IndexError as there is no index 6 due to no elements being present at index 6
# print(a[6])

d = {'name': 'Max', 'age': 27}

# print(d['city'])  # throws KeyError as there is no key 'city' in the dictionary d


# Forcing/Raising an exception
x = -5
# if x < 0:
#     raise Exception('x should be positive')

# using Assert statement
# assert(x >= 0), 'x should be positive'  # give AssertionError

print("Hello1")

# Exception Handling
try:
    a = 5 / 0
except:
    print("ZeroDivisionError, division by 0 is not defined")

print("Hello2")

try:
    c = int('hello')
except Exception as e:
    print(e)

print("Hello3")

# handling multiple exceptions, only one except will execute based on the exception raised in try
try:
    c = 5 / 0
    a = -5 + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:  # runs when there is no exception raised in try
    print("Everything is fine")
finally:  # runs always whether there is an exception raised in try or not
    print('cleaning up')

print("Hello4")


# Define own error classes
class ValueTooHighError(Exception):
    pass


class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 1000:
        raise ValueTooHighError('Value is too high')
    if x < 0:
        raise ValueTooLowError('Value is too low', x)


try:
    test_value(-2)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)
