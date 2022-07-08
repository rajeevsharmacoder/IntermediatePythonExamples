# - The difference between arguments and parameters
# - Positional and keyword arguments
# - Default arguments
# - Variable length arguments (*args and **kwargs)
# - Container unpacking into function arguments
# - Local vs. Global arguments
# - Parameter passing (by value or by reference)


# Parameters are the variables that are defined and used inside paranthesis while defining a function
# Arguments are the values passed for these parameters while calling a function

def print_name(name):  # name here is the parameter
    print(name)


# 'Alex' string here is the argument to print_name function passed while calling it
print_name('Alex')


def foo(a, b, c):
    print(a, b, c)


foo(1, 2, 3)
# or
foo(a=1, b=2, c=3)
# or
foo(c=1, a=2, b=3)
# or
foo(1, c=3, b=2)
# but not
# foo(1, b=2, a=3) # you have already assigned a as 1 and again assigning a=3, not cool bro


# if c is not passed, c will be taken as 0 so 0 is default value of c already defined while defining the function
# default arguments should always be at the end in parameters list def function_name(a=0, b, c) will throw SyntaxError
def default_argument(a, b, c=0):
    print(a, b, c)


default_argument(1, 2)
# or
default_argument(1, 2, 4)


# if you make 1 star to any parameter then you can pass any number of positional arguments to the function
# if you make 2 stars to any parameter then you can pass any number of keyword arguments to the function
def variable_length_arguments(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)


variable_length_arguments(1, 2, 3, 4, 5, 6, seven=7, eight=8)
# or
variable_length_arguments(1, 2, seven=7, eight=8)
# or
variable_length_arguments(1, 2, 3, 4, 5, 6)


# every argument after * should be a keyword argument while calling the function
def forced_keyword_arguments_1(a, b, *, c, d):
    print(a, b, c, d)


forced_keyword_arguments_1(1, 2, c=3, d=4)


# or

# every parameter after *args should also be a keyword argument
def forced_keyword_arguments_2(*args, c, d):
    for i in args:
        print(i)
    print(c, d)


forced_keyword_arguments_2(1, 2, 3, 4, c=5, d=6)


# Unpacking arguments
def unpacking_arguments(a, b, c):
    print(a, b, c)


my_list = [0, 1, 2]
unpacking_arguments(*my_list)

my_tuple = (1, 2, 3)
unpacking_arguments(*my_tuple)

my_dict = {'a': 1, 'b': 2, 'c': 3}
unpacking_arguments(**my_dict)

# main thing is the length of the iterable must be equal to the number of parameters of the function
# in case of dictionary the keys should be of same name as  the function parameters


# Local vs. Global variables
def variables_1():
    global number
    # read access is there for global variable
    print('Number inside function', number)

    # write access requires to kind of import it using global keyword in the function it is to be used
    number = 3
    print('Changed number', number)


number = 0
variables_1()
print('Number after function call', number)


# Parameter passing (call by object or call by object reference)
def passing_1(x):
    x = 5


var = 10  # immutable objects cannot be changed
passing_1(var)
print(var)


def passing_2(a_list):
    # rebinding reference creates local variable to the function so reference has changed
    # a_list = [200, 300, 400]
    a_list.append(4)
    a_list[1] = 8


my_list = [1, 2, 3]  # mutable objects can be changed
passing_2(my_list)
print(my_list)


def passing_3(a_list):
    # a_list += [200, 300, 400]  # changes list
    a_list = a_list + [200, 300, 400]  # created local variable a_list


my_list = [1, 2, 3]
passing_3(my_list)
print(my_list)
