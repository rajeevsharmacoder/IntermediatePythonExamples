# Generator are functions that return objects that can be iterated over
# They generate the items inside the objects lazily meaning they generate the items only one at a time and only when asked
# This is why they are much more memory efficient than other sequence objects while dealing with large data sets
import sys


def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4


g = my_generator()
# print(g)

# for i in g:
#     print(i)

# v = next(g)
# print(v)

# v = next(g)
# print(v)

# v = next(g)
# print(v)

# v = next(g)
# print(v)

# StoIteration is raised an only 4 yields were present
# v = next(g)
# print(v)

# print(sum(g))

print(sorted(g))

# at a time only one cumulative function works on a generator


def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)

v = next(cd)
print(v)

# second call remembers the previous yield and this goes till there is nothing to yield
v = next(cd)
print(v)

v = next(cd)
print(v)

v = next(cd)
print(v)


def firstn(num):
    n = []
    i = 0
    while i < num:
        n.append(i)
        i += 1
    return n


# mylist = firstn(10)
# print(mylist)
# print(sum(mylist))


# Lets use generator now
def firstn_generator(n):
    j = 0
    while j < n:
        yield j
        j += 1


# mylist1 = firstn_generator(10)
# print(sum(mylist1))
# or
# print(sum(firstn_generator(10)))

print(sys.getsizeof(sum(firstn(1000000))))
print(sys.getsizeof(sum(firstn_generator(1000000))))


# Fibonacci using generators
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + bn


fib = fibonacci(100)

for i in fib:
    print(i)


# Generator expressions
# They are written as list comprehensions but using parenthesis instead of square brackets
mygenerator = (i for i in range(1000000) if i % 2 == 0)
# print(list(mygenerator))
# for i in mygenerator:
#     print(i)


# accessing elements in generators can only be done once as they are not stored in memory for long


print(sys.getsizeof(mygenerator))

mylist = [i for i in range(1000000) if i % 2 == 0]

print(sys.getsizeof(mylist))
