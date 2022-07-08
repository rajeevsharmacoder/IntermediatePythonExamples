import random
import secrets
import numpy as np

a = random.random()  # prints random numbers (float) between 0 and 1
print(a)

# give specific range, float number is generated between given range
a = random.uniform(1, 10)
print(a)

# generates random integers between given range and will include the upper and lower bounds
a = random.randint(1, 10)
print(a)

# this will do the same as randint but it will skip the upper bound
a = random.randrange(1, 10)
print(a)


# gives value from a normal distribution from the mean of 0 and standard deviation of 1
a = random.normalvariate(0, 1)
print(a)


# to pick random element from a given list
mylist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print(mylist)
a = random.choice(mylist)
print(a)

# pick any <given number> of random elements from the list and return a list
a = random.sample(mylist, 3)  # this will pick unique index elements
print(a)

# this can pick the same index element multiple times
a = random.choices(mylist, k=3)
print(a)

random.shuffle(mylist)  # shuffles the given list inplace
print(mylist)

# since the above methods are all pseudo random that means they can be made to repeat, below is how
random.seed(1)
print(random.random())  # prints the same float number between 0-1
print(random.randint(1, 10))  # prints the same integer number between 1 and 10

# re-seeding
random.seed(1)
print(random.random())  # prints the same float number between 0-1
print(random.randint(1, 10))  # prints the same integer number between 1 and 10

# seeding with different value
random.seed(2)
print(random.random())  # prints the same float number between 0-1
print(random.randint(1, 10))  # prints the same integer number between 1 and 10

# seeding with previous value again
random.seed(1)
print(random.random())  # prints the same float number between 0-1
print(random.randint(1, 10))  # prints the same integer number between 1 and 10

# so basically these are pseudo random as we can make them or force them generate the same output everytime
# not recommended for security purposes


# using secrets module for security purposes like passwords, security tokens or account authentication etc.
# disadvantage is that it takes more time but they will generate a true random number
# it has only three functions
a = secrets.randbelow(10)  # exclude the upper bound
print(a)

# any number between 0 - 15 as 4 bits means max will be 15, change this range to play around
a = secrets.randbits(4)
print(a)

mylist = list("ABCDEFGHIJ")
a = secrets.choice(mylist)  # will give an actual random number from my list
print(a)


# numpy
# I want an array with random floats
# generates random 1D array with 3 elements and the values will be between 0 and 1
a = np.random.rand(3)
print(a)

# generates random 2D array of 3x3  and the values will be between 0 and 1
a = np.random.rand(3, 3)
print(a)

# random integers in a range
a = np.random.randint(0, 10, 3)  # excluded upper bound, 1D array
print(a)

# excluded upper bound, 2D array or higher dimensions use a tuple
a = np.random.randint(0, 10, (3, 4))
print(a)


# random shuffle
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)  # shuffles along the 1st axis
print(arr)

# using seed to repeat output, numpy uses a different seed and random generator module than the standard random module in python
np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))
