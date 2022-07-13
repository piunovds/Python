def type_logger(func):
    def wrapper(number):
        result = func(number)
        print(f'{func.__name__} ({number}: {type(number)})')
        return result
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(10))
