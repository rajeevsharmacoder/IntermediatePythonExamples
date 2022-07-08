# Strings: Ordered, immutable, text representation
from timeit import default_timer as timer
my_string = "Hello World!"
print(my_string)

my_string = 'Hello World!'
print(my_string)

my_string = 'I\'m a programmer'
print(my_string)

my_string = "I'm a programmer"
print(my_string)

# creates new line
my_string = """Hello
World!!"""
print(my_string)

# escapes new line
my_string = """Hello \
World!! \
Java is boring"""
print(my_string)

my_string = "Hello World!!"
char = my_string[6::-1]  # slicing is fun with strings
print(char)

# my_string[1] = 'h'  # not allowed as strings are immutable
print(my_string)

string1 = "Hello"
string2 = "Tom"
sentence = string1 + " " + string2
print(sentence)

for i in string1:
    print(i)

if 'el' in string1:
    print("Yes")
else:
    print("No")

string = '     Hello World !!      '
print(string)
string = string.strip()
print(string)

print(string.upper())
print(string.lower())

print(string.startswith('He'))
print(string.endswith('rld !!'))

print(string.find('la'))

print(string.count('o'))

# this is not mutating the string. It actually creates a new string.
# if to be replaced string is not found then it does nothing
print(string.replace('World', 'Universe'))

string = "How you doin'?"

mylist = string.split()  # default delimiter is space ' '
print(mylist)

string = "How,you,doing?"
mylist = string.split(',')
print(mylist)

newstring = ' '.join(mylist)  # do specify the delimiter in the starting
print(newstring)

mylist = ['a'] * 1000
# print(mylist)

# bad method to create a string from list elements
string = ''
start = timer()
for i in mylist:
    string += i
end = timer()
print(end - start)
# print(string)

# good method to create a string from list elements
start = timer()
string = ''.join(mylist)
end = timer()
print(end - start)
# print(string)

# Formatting strings
# %, format(), f-strings
var = "Tom"
# if var is a integer, use %d, if floating number then use %f (which by default will take 6 digits after decimal, make use of %.Xf where X is the number of decimal places you want)
string = "the variable is %s" % var
print(string)

var = 3.14256932
var1 = "Tom"
string = "the variable is {:.4f} and name is {}".format(var, var1)
print(string)

string = f"the variable is {var:.4f} and name is {var1*2}"
print(string)
