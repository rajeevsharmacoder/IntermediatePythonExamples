# Process: Is an instance of a program (e.g. Python Interpreter)

# + Takes advantage of multiple CPUs and cores
# + Separate memory space - Memory is not shared between processes
# + Great for CPU-bound processing
# + New process is started independently from other processes
# + Processes are interuptible/killable
# + One GIL(global interpreter lock) for each process - Avoids GIL limitation

# - Heavyweight
# - Starting a process is slower than starting a thread
# - More memory
# - IPC (inter-process communication) is more complicated


# Thread: An entity within a process that can be scheduled (also called as lightweight process)
# A process can spawn multiple threads

# + All threads within a process share the same memory
# + Lightweight
# + Starting a thread is faster than starting a process
# + Great for I/O-bound tasks

# - Threading is limited by GIL - only one thread at a time
# - No effect for CPU-bound tasks
# - Not interruptable/killable
# - Careful with race conditions


# GIL: Global Interpreter Lock
# - A lock that allows only one thread at a time to execute in Python

# - Needed in CPython because memory management is not thread-safe

# -Avoid:
#     - Use multiprocessing
#     - Use a different, free-threaded Python (Jython, IronPython)
#     - Use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy


from multiprocessing import Process
import os
import time

from threading import Thread


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


# processes = []
# number_of_processes = os.cpu_count()

# # create processes
# for i in range(number_of_processes):
#     p = Process(target=square_numbers)
#     processes.append(p)

# # start processes
# for p in processes:
#     p.start()

# # join
# for p in processes:
#     p.join()


threads = []
number_of_threads = 10

# creating threads
for i in range(number_of_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# start threads
for t in threads:
    t.start()

# join
for t in threads:
    t.join()


print('end main')
