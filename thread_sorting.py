import threading
import random
import time

def sorting(array):
    print("Start thread", threading.currentThread())
    print(array)
    print(sorted(array))
    print("End thread", threading.currentThread())


def sort_arrays(count):
    array = []

    for i in range(0, count):
        for j in range(0, 10):
            array.append(random.randint(0, 10))
        t = threading.Thread(target=sorting, args=(array,))
        t.start()
        time.sleep(1)
        array.clear()


print(sort_arrays(5))
