# Sets: Unordered, mutable, doesn't allow duplicates
myset = {1, 2, 3, 1, 2}
print(myset)

myset = set([5, 6, 7])
print(myset)

myset = set("Hello")
print(myset)

myset = set()
print(type(myset))

myset.add(1)
myset.add(2)
myset.add(3)

print(myset)

# if you remove a value that is not present in the set then you will get KeyError
myset.remove(3)
print(myset)

# better to use discard in case you are not sure if element is present in the set or not, it does not through any exception
myset.discard(4)
print(myset)

myset.clear()
print(myset)

myset = {5, 6, 7, 8}
print(myset.pop())
print(myset)

for i in myset:
    print(i)

if 5 in myset:
    print("Yes")
else:
    print("No")


odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
B = {1, 2, 3, 10, 11, 12}

d = A.difference(B)  # or simply A - B
print(d)

# it will skip common elements and return only the uncommon ones which are there in set A and set B
d = A.symmetric_difference(B)
print(d)

A.update(B)  # copies uncommon elements from set B to set A
print(A)

# finds intersection between A and B first and then adds/copies uncommon elements from set B to set A
A.intersection_update(B)
print(A)

A.difference_update(B)  # no longer works
print(A)

A.symmetric_difference_update(B)  # returns set B
print(A)

A = {1, 2, 3, 4, 5, 6}
B = {1, 2, 3}

print(B.issubset(A))

print(B.issuperset(A))

print(A.isdisjoint(B))  # return true if no intersection else false

C = A.copy()  # make use of copy method or C = set(A)
C.add(9)
print(A)
print(C)

a = frozenset([1, 2, 3, 4])  # frozen set is immutable
# a.add(5)  # this will give error, only main methods like intersection, union and difference will work and that too for a different set as output
print(a)
