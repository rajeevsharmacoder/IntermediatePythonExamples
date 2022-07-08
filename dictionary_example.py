# Dictionary: Unordered, Key-Value pairs, Mutable
mydict = {"name": "Max", "age": 28, "city": "Boston"}
print(mydict)

mydict2 = dict(name="Marry", age=27, city="Boston")
print(mydict)

# accessing values
value = mydict['name']  # or mydict.get("name")
print(value)

# adding new keys
mydict['email'] = "max@xyc.com"
print(mydict)

# updating existing keys
mydict['email'] = "coolmax@xyc.com"
print(mydict)

# delete a key
del mydict['name']
print(mydict)

print(mydict.pop("age"))
print(mydict)

# removes last item in >= python 3.x
print(mydict.popitem())
print(mydict)

# existence check
if "name" in mydict2:
    print(mydict2["name"])
else:
    print("Not found")

try:
    print(mydict["name"])
except:
    print("'name' Key does not exist")

for key in mydict2.keys():
    print(key)

for value in mydict2.values():
    print(value)

for key, value in mydict2.items():
    print(key, value)

# copy
mydict_copy = mydict2.copy()  # or mydict_copy = dict(mydict2)
mydict_copy['email'] = "marry@xyx.com"
print(mydict_copy)
print(mydict2)


mydict1 = {"name": "Max", "age": 28, "email": "max@xyz.com"}
mydict2 = dict(name="Marry", age=27, city="Boston")

print(mydict1, mydict2)

# exisitng keys got overwritten and non-existing keys got added
mydict1.update(mydict2)
print(mydict1)

mydict3 = {3: 9, 4: 16, 6: 36, 9: 81}
print(mydict3)

print(mydict3[3])
print(mydict3[9])

mytuple = (8, 7)
mydict = {mytuple: 15}  # tuple can be used as key
print(mydict)

mylist = [8, 7]
# list is NOT possible to be used as a key, you get TypeError
# mydict = {mylist: 15}
# print(mydict)
