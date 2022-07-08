import copy
# Shallow Copy: is only one level deep, only references of nested child objects
# Deep Copy: full independent copy

# immutable types
org = 5
cpy = org
print(org, cpy)
# above created a reference cpy for value of org it does not create another memory block with value 5

# but if I change org, immediately cpy is changed to point to another object with first value of org
org += 10
print(org, cpy)


# mutable types
a_list = [0, 1, 2, 3, 4]
b_list = a_list  # not an actual copy

b_list[0] = -1

print(a_list, b_list)


# shallow copy
c_list = [0, 1, 2, 3, 4]
# or d_list = c_list.copy() or d_list = list(c_list) or d_list = c_list[:]
d_list = copy.copy(c_list)
d_list[0] = -10

print(c_list, d_list)


# works for 1 level of nesting also
org_list = [[0, 1, 2, 3], [4, 5, 6, 7]]
cpy_list = list(org_list)
cpy_list[0][3] = -1
print(org_list, cpy_list)


# deep copy
org_list = [[0, 1, 2, 3], [4, 5, 6, 7]]
cpy_list = copy.deepcopy(org_list)
cpy_list[0][3] = -1
print(org_list, cpy_list)  # original list did not get affected


# We can use deep copy for custom objects as well

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Rajeev', 31)
p2 = p1  # not an actual copy
p2.age = 32

print(p1.age, p2.age)  # both dates changed

# shallow copy
p3 = copy.copy(p1)
p3.age = 33
print(p1.age, p3.age)  # p1 did not change on changing p3


# shallow copy
boss = Person('Boss', 45)
employee = Person('Employee', 32)
company = Company(boss, employee)
company_clone = copy.copy(company)

company_clone.boss.age = 56
print(company.boss.age, company_clone.boss.age)  # both got changed

# deep copy
company_clone_deep = copy.deepcopy(company)
company_clone_deep.boss.age = 57
# only clone deep objects boss's age changes
print(company.boss.age, company_clone_deep.boss.age)
