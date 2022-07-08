# A process pool can be used to manage multiple processes.
# A process pool object contains pool of worker processes to which jobs can be submitted.
from multiprocessing import Pool


def cube(number):
    return number * number * number


if __name__ == "__main__":

    numbers = range(1, 11)
    pool = Pool()

    # most important pool methods are -
    # map, apply, join and close

    # calculates cores in machine and split iterable into equal sized chunks and submit to the function and it will be executed in parallel by different processes
    result = pool.map(cube, numbers)

    # if you simply want 1 function to be executed by pool
    # pool.apply(cube, numbers[0])

    pool.close()
    pool.join()

    print(result)
