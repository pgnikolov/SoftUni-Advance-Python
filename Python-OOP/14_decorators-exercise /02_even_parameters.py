from functools import wraps


def even_parameters(add):
    @wraps(add)
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) and arg % 2 == 0 for arg in args):
            return add(*args, **kwargs)
        return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
