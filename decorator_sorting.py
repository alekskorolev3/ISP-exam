from functools import cmp_to_key


def comparator(a, b):
    if a < b:
        return -1
    if a > b:
        return 1
    if a == b:
        return 0


def compare(comp):
    if not isinstance(comp, type(compare)):
        raise Exception("Comparator should be function!")

    def decorator(func):
        def wrapper(*args, **kwargs):
            args = tuple(sorted(args, key=cmp_to_key(comp)))
            return func(*args)

        return wrapper

    return decorator


@compare(comparator)
def multiply(a, b, c):
    return 100 * a + 10 * b + c


print(multiply(3, 2, 4))
