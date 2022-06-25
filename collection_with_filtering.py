from typing import Any, Collection, Iterable
from copy import deepcopy as dc


class CollectionFormater:
    def __init__(self, collection: Iterable):
        self.iterable = collection

    def __iter__(self):
        return self.iterable.__iter__()

    def select(self, func: bool(Any)):
        new_col = dc(CollectionFormater(self.iterable))
        for el in self.iterable:
            if not func(el):
                del new_col.iterable[self.iterable.index(el)]
        return new_col


a = CollectionFormater([1, 2, 4, 0, 6, 5])
v = a.select(lambda x: x > 0)

for i in v:
    print(i)
