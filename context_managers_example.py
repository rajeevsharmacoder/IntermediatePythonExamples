# Context Managers are used to manage resources
# They allow to occupy and release resources as and when you want to
from contextlib import contextmanager
from threading import Lock
with open('notes.txt', 'w') as file:
    file.write('Something\nSomething')
# above with will ensure to close the file even when there is an exception somewhere

# above looks like
file = open('notes.txt', 'w')
try:
    file.write('Something\nSomething')
finally:
    file.close()

# both codes will do same operation but with statement is much cleaner and better
# aquiring releasing locks, connecting disconnecting to/from database

lock = Lock()

lock.acquire()
# thread safe action
lock.release()  # never forget

# better way is with

with lock:
    # thread safe action
    pass


# Context Manager for our own classes
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Enter")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if self.file:
            self.file.close()
        if exception_type is not None:
            print('Exception handled')
        # print('Exception: ' + str(exception_type) + " " + str(exception_value))
        print("Exit")
        return True


with ManagedFile('notes.txt') as file:
    print("Do some stuff")
    file.write("Something to do")
    file.somemethod()

print('Continuing here . . .')


# Implement our own context manager as functions
@contextmanager
def open_managed_file(filename):
    file = open('notes.txt', 'w')
    try:
        yield file
    finally:
        file.close()


with open_managed_file('notes.txt') as f:
    f.write("Something to do in the file")
