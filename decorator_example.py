# A decorator is a function that takes another function as an argument and extends the function of the function without explicitly modifying it
import functools


def start_end_decorator(func):
    def wrapper():
        # do something before the function
        print('Start')
        func()
        # do something after the function
        print('End')
    return wrapper


@start_end_decorator
def print_name():
    print('Rajeev')


# print_name()  # normal print

# adds to the functionality of the print_name function
# print_name = start_end_decorator(print_name) # same functionality is obtained by adding start_end_decorator decorator to the print_name function

print_name()

print()

# what if my function has arguments and also returns a value?


def start_end_decorator_2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # do something before the function
        print('Start')
        result = func(*args, **kwargs)
        # do something after the function
        print('End')
        return result
    return wrapper


@start_end_decorator_2
def add5(x):
    return x + 5


result = add5(10)
print(result)

# function identity
# print(help(add5))
print(add5.__name__)


# Template for a nice decorator
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # do something here
        result = func(*args, **kwargs)
        # do something here
        return result
    return wrapper


print()


# Decorators can take function as an argument that means 2 inner functions example


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=5)
def greet(name):
    print("Hello " + str(name))


greet("Rajeev")

print()

# Nested Decorators


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@start_end_decorator_2
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting


say_hello('Rajeev')

# Multiple decroators are executed in the order they are applied to the function


# Class Decorators
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Executed {self.num_calls} time(s)")
        return self.func(*args, **kwargs)


# cc = CountCalls(None)
# cc()


@CountCalls
def say_hello_again(name):
    print("hello" + str(name))


say_hello_again("Rajeev")
say_hello_again("Rajeev")
say_hello_again("Rajeev")
