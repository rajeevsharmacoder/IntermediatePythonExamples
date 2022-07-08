# Queues: are excellent for thread safe and process safe data exchanges and data processing in multithreaded or multiprocessing environments
from threading import Thread, Lock, current_thread
from queue import Queue
import time


def worker(q, lock):
    # with daemon thread enabled only we can use infinite loop as it terminates when the main thread closes and loop terminates automatically
    # without daemon thread we would need to give an explicit condition to breadk the loop which must happen at some point after computations
    while True:
        value = q.get()
        with lock:
            print(
                f"We are in {current_thread().name} where we got queue item {value}")
        q.task_done()


if __name__ == "__main__":

    q = Queue()
    lock = Lock()

    # q.put(1)
    # q.put(2)
    # q.put(3)

    # # 3 2 1 -> front

    # # methods of queue to remember
    # first = q.get()
    # print(first)

    # # q.empty() # tells if q is empty or not, True/False value

    # q.task_done()  # to be used when we are done processing object of q in threading

    # q.join()  # block the main thread and wait until all elements in queueu are processed

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        # by default threads are not daemon, it is a background thread that dies with main thread
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print('end main')
