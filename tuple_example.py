# Tuple: ordered, immutable, allows duplicate elements
# mytuple = ("Max") won't be a tuple, it will be considered as a string so use ("Max",) in case of a single element in tuple
import timeit
import sys
mytuple = ("Max", 28, "Austin")
print(mytuple)

single_tuple = ("Element")
print(single_tuple)
print(type(single_tuple))

single_tuple = ("Single",)
print(single_tuple)
print(type(single_tuple))

mytuple = tuple(["Max", 28, "Awesome"])
print(mytuple)

# access elements
item = mytuple[0]  # negative indexes are allowed like list
print(item)

for i in mytuple:
    print(i)

if "Hello" in mytuple:
    print("Found")
else:
    print("Not found")

mytuple = ('a', 'p', 'p', 'l', 'e')
print(len(mytuple))

print(mytuple.count('e'))

print(mytuple.index('a'))

mylist = list(mytuple)

print(mylist)

mytuple2 = tuple(mylist)

print(mytuple2)

print(mytuple[0:2])
print(mytuple[2:])
print(mytuple[:3])
print(mytuple[::2])
print(mytuple[::-2])


# unpacking
mytuple = ("Max", 28, "Boston")
name, age, city = mytuple

print(name, age, city)

mytuple = (0, 1, 2, 3, 4)

i1, *i2, i3 = mytuple

print(i1)
print(i3)
print(i2)


mylist = [0, 1, 2, "Hello", True]
mytuple = (0, 1, 2, "Hello", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3 ,4 ,5)", number=1000000))

# in short, working with tuples is more efficient than working with lists.
# In case you know you are not going to modify the values, make use of tuples.
