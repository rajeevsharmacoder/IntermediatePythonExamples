# deprecated
# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
# from abc import Counter
# a = "Hello World!!"
# my_list = a.split()
# my_counter = Counter(my_list)
# print(my_counter)
# print(my_counter.most_commom(1)[0][0]) # gives list of tuples based on how many most commons you want
# print(list(my_counter.elements())) # returns an iterable to will have to covert to list

# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')
# pt = Point(1, -4)
# print(pt)
# print(pt.x, pt.y)

# from collections import OrderedDict
# ordered_dict = OrderedDict()
# ordered_dict['a'] = 1
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# print(ordered_dict)

# from collections import defaultdict
# default_dict = defaultdict(int)
# default_dict['a'] = 1
# default_dict['b'] = 2
# default_dict['c'] = 3
# default_dict['d'] = 4
# print(default_dict)
# print(default_dict['a'])
# print(default_dict['e']) # this returns a default value of an integer which is 0

# from collections import deque
# d = deque()
# d.append(1)
# d.append(2)
# d.append(3)
# print(d)

# d.appendleft(4)
# d.appendleft(5)

# print(d)

# d.pop() # removed last element
# print(d)

# d.popleft() # removed first element
# print(d)

# d.clear()  # removed all elements

# d.extend([4, 5, 6])  # adds all elements to the right
# d.extend([1, 2, 3])  # adds all elements to the left

# d.rotate(1)  # rotate elements 1 place right
# d.rotate(-1)  # rotate elemetns 1 place left
