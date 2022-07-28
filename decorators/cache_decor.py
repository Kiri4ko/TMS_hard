cache = {}


def decor_cache(func):
    def wrapper(*args, **kwargs):
        if args in cache.keys():
            return cache[args]
        else:
            result = func(*args, **kwargs)
            cache.update({args: result})
            return result

    return wrapper


@decor_cache
def f_1(a, b, c):
    return a * b * c


@decor_cache
def f_2(a, b, c):
    return a * b * c


@decor_cache
def f_3(a, b, c):
    return a * b * c


print(f_1(1, 2, 3), f_2(1, 4, 3), f_3(1, 2, 3))
