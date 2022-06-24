class MetaCounter(type):
    _counter = {}

    def __new__(cls, name, bases, dict):
        cls._counter[name] = 0
        return super().__new__(cls, name, bases, dict)

    def __call__(cls, *args, **kwargs):
        cls._counter[cls.__name__] += 1
        return super().__call__(*args, **kwargs)


class SimpleClassA(metaclass=MetaCounter):
    pass


class SimpleClassB(metaclass=MetaCounter):
    pass


x = SimpleClassA()
y = SimpleClassA()
z = SimpleClassA()
a = SimpleClassB()
b = SimpleClassB()
print(MetaCounter._counter)
print(SimpleClassA._counter)
print(SimpleClassB._counter)
