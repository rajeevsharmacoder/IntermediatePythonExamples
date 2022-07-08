# lambda arguments: expression

# add10 = lambda x: x + 10
# from functools import reduce
def add10(x): return x + 10


print(add10(5))


# mult = lambda x, y: x * y
def mult(x, y): return x * y


print(mult(2, 3))


def sort_by_y(x):
    return x[1]


points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print(points2D, points2D_sorted)
# default by 1st element of the tuple, if key given then give a function/lambda
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D, points2D_sorted)
points2D_sorted = sorted(points2D, key=sort_by_y)
print(points2D, points2D_sorted)
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D, points2D_sorted)

# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))

b = [x * 2 for x in a]  # list comprehension
print(b)

# filter(func, seq) # func must return true/false here
a.append(6)
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

b = [x for x in a if x % 2 == 0]
print(b)

# deprecated
# reduce(func, seq) # repeatedly applies the function to the element and returns a single value
# b = reduce(lambda x, y: x * y, a)
# print(b)
