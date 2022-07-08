mylist = ["banana", "cherry", "apple"]

print(mylist)

mylist2 = list()
print(mylist2)

mylist3 = [1, False, "Guava", "Apple", "Apple"]
print(mylist3)

print(mylist3[3])
print(mylist3[0])
print(mylist3[4])
print(mylist3[-1])
print(mylist3[-3])

for i in mylist3:
    print(i)

if "Apple" in mylist3:
    print("Found")
else:
    print("Not found")

print(len(mylist3))

mylist3.append("Lemon")
print(mylist3)

mylist3.insert(1, "BlueBerry")
print(mylist3)

print(mylist3.pop())
print(mylist3)

mylist3.remove("Guava")
print(mylist3)

mylist3.reverse()
print(mylist3)

# mylist3.sort()  # can only be done for same data type elements list
# print(mylist3)

mylist3.clear()
print(mylist3)

mylist4 = ["Apple", "Banana", "Mango", "Lemon"]
mylist4.sort()
print(mylist4)

new_list = sorted(mylist4)
print(new_list)

mylist1 = [0] * 20
mylist2 = [1, 2, 3, 4, 5]

new_list = mylist1 + mylist2
print(new_list)

print(mylist2[3:5])
print(mylist2[:3])
print(mylist2[3:])
print(mylist2[::-1])


list_org = ["Banana", "Cherry", "Apple"]

# or use list_copy = list(list_org) or use list_copy = list_org[:]
list_copy = list_org.copy()

print(list_org, list_copy)

list_org.insert(1, "Papaya")

list_copy.remove("Cherry")

print(list_org, list_copy)


a = [1, 2, 3, 4, 5, 6]
b = [i*i for i in a]

print(a, b)
