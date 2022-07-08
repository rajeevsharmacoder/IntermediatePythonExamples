import json
from json import JSONEncoder

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

# personJSON = json.dumps(
# person, indent=4, separators=('; ', '= '), sort_keys=True)

personJSON = json.dumps(person, indent=4, sort_keys=True)

# print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4, sort_keys=True)

# Deserialisation
person = json.loads(personJSON)
print(person)


# from json file
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)


# encoding custom objects

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


user = User("Tom", "56")
userJSON = json.dumps(user, default=encode_user)
print(userJSON)


# can do this by creating JSONEncoder subclass
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)
# or
userJSON = UserEncoder().encode(user)
print(userJSON)


# deconding custom objects

def decode_user(d):
    if User.__name__ in d:
        return User(name=d['name'], age=d['age'])
    return d


user = json.loads(userJSON)
print(user)
print(type(user))
# or
user = json.loads(userJSON, object_hook=decode_user)
print(user.name, user.age)
print(type(user))
