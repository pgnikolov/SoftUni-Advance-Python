from functools import wraps


def type_check(type):
    @wraps(type)
    def wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type):
                    return "Bad Type"
            return func(*args, **kwargs)
        return wrapper
    return wrapper
