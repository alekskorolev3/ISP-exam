# [[1, 1], 2, [1, 1]]

def generator(lst):
    for item in lst:
        if not isinstance(item, list):
            yield item
        else:
            yield from generator(item)


for i in generator([[[1, [1, 3]], 2, [1, 4, [6]]]]):
    print(i)
