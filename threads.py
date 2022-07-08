from threading import Thread, Lock
import time


database_value = 0


# this is an example of race condition as well
# def increase():
#     global database_value
#     local_copy = database_value

#     # processing
#     local_copy += 1

#     time.sleep(0.1)

#     database_value = local_copy


# resolving race condition using lock
def increase(lock):
    global database_value

    # lock.acquire()
    # local_copy = database_value

    # # processing
    # local_copy += 1
    # # this is an example of race condition as well
    # time.sleep(0.1)

    # database_value = local_copy
    # lock.release() # always remember to release lock

    # or below way is better in with we do not need to specify lock.acquire() and lock.release() methods

    with lock:  # context manager acquires and releases the lock
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":

    lock = Lock()
    print('Start Value', database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('End Value', database_value)

    print('end main')
