class FlattenIterator:
    def __iter__(self):
        return self

    def __init__(self, lst):
        self.a = 0
        self.data = []
        self.rec(lst)
        self.counter = 0

    def __next__(self):
        if not self.counter == self.a - 1:
            self.counter += 1
            return self.data.pop(0)
        else:
            raise StopIteration

    def rec(self, lst):
        for item in lst:
            if not isinstance(item, list):
                self.data.append(item)
                self.a += 1
            else:
                self.rec(item)


# lst = [[1, 1], [2], [1, 1]]
lst = [[1, [1, 3]], 2, [1, 4, [6]]]
for i in FlattenIterator(lst):
    print(i, end=" ")
