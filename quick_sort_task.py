import random

def qsort(arr):
    if len(arr) > 1:
        middle = arr[random.randint(0, len(arr) - 1)]
        min = [el for el in arr if el < middle]
        equal = [el for el in arr if el == middle]
        max = [el for el in arr if el > middle]
        arr = qsort(min) + equal + qsort(max)

    return arr

print(qsort([5,3,1,4,2]))
