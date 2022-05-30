from functools import wraps

def value_checker(lambda_func):
    def _value_checker(func):
        @wraps(func)
        def wrapper(number):
            if lambda_func(number):
                result = func(number)
            else:
                raise ValueError(f'Incorrect value: {number}')
            return result
        return wrapper
    return _value_checker


@value_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(15))


