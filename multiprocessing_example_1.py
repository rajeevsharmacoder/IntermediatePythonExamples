from multiprocessing import Process, Value, Array, Lock, Queue
import time


def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


def add_10(numbers, lock):
    for i in range(10):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1


def square(numbers, q):
    for i in numbers:
        q.put(i*i)


def make_negative(numbers, q):
    for i in numbers:
        q.put(-1*i)


if __name__ == "__main__":
    lock = Lock()
    shared_number = Value('i', 0)

    print('Shared Number at beginning is', shared_number.value)

    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))

    # race condition will happen so getting 200 will be difficult. To prevent this we have used lock.
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # every time answer is 200 with lock. Without lock the value mostly will always be <200. Sometimes it may get to 200 but that will be a rare thing.
    print('Shared Number at end is', shared_number.value)

    # lets do same thing with shared Array instead of just a single shared Value
    shared_array = Array('d', [0.0, 100.0, 200.0])

    print('Shared Array at beginning is', shared_array[:])

    p3 = Process(target=add_10, args=(shared_array, lock))
    p4 = Process(target=add_10, args=(shared_array, lock))

    p3.start()
    p4.start()

    p3.join()
    p4.join()

    print('Shared Array at end is', shared_array[:])

    # lets use queue
    q = Queue()
    numbers = range(1, 6)

    p5 = Process(target=square, args=(numbers, q))
    p6 = Process(target=make_negative, args=(numbers, q))

    p5.start()
    p6.start()

    p5.join()
    p6.join()

    while not q.empty():
        print(q.get())

    print("end main")
