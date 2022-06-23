def cache(size):
    def decorator(f):

        f.values = {}

        def wrapper(*args, **kwargs):
            key = args + tuple(kwargs.values())
            if args not in f.values:
                if len(f.values) == size:
                    print("Clearing cache")
                    f.values.clear()
                print("Setting cache")
                f.values[key] = f(*args, **kwargs)
                return f.values[key]
            else:
                print("Returning cached items")
                return f.values[key]

        return wrapper

    return decorator

@cache(2)
def sum(a, b):
    return a + b


print(sum(1, 2))
print(sum(1, 2))
print(sum(3, 2))
print(sum(4, 2))
print(sum(4, 2))
