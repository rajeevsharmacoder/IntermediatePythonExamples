# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator
a = [1, 2]
b = [3, 4]
# repeat basically increases degree of the multiplication, you might see a lot of duplicates with different ordered tuples
# usually keep the repeat to 1 or don't pass it at all, by default repeat is set to 1
prod = product(a, b, repeat=1)  # gives cartesian product tuples
print(list(prod))

a = [1, 2, 3]
perm = permutations(a, 2)  # second argument is length
print(list(perm))

comb = combinations(a, 2)  # second argument is mandatory in combinations
print(list(comb))

# gives combinations with self as well
comb = combinations_with_replacement(a, 2)
print(list(comb))

a = [1, 2, 3, 4]
accum = accumulate(a)
# basically a cumulative sum with same length of list as the input, we can also do other arithmatic operations using operators but default is sum
print(a, list(accum))
accum = accumulate(a, func=operator.mul)
print(a, list(accum))
accum = accumulate(a, func=max)
print(a, list(accum))
accum = accumulate(a, func=min)
print(a, list(accum))


def smaller_than_three(x):
    return x < 3


a = [1, 2, 3, 4, 0, 9, -5, 5, 7]
# groups elements based on a fucntion condition given as key
group = groupby(a, key=smaller_than_three)
# printing will happen sequentially for the list so multiple groups of return value of the function are made
for k, v in group:
    print(k, list(v))
print()
# we can make use of lambda functions as key
group = groupby(a, key=lambda x: x < 3)
for k, v in group:
    print(k, list(v))


persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Clair', 'age': 28}]

group = groupby(persons, key=lambda x: x['age'])
for k, v in group:
    print(k, list(v))

for i in count(10):
    print(i)  # runs infinitely until if condition below is true
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a):
    print(i)  # runs infinitely until if condition below is true
    if i == 3:
        break

for i in repeat(1, 5):  # second arguments gives the termination condition
    print(i)  # runs infinitely until second argument termination is reached or if not given then if condition below is true
    # if i == 1:
    #     break
