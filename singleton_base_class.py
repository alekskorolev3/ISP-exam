class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class MyClass(Singleton):
    pass

a = MyClass()
b = MyClass()

print(id(a), id(b))