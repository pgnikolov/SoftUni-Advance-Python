from functools import wraps


def cache(func):
    @wraps(func)
    def wrapper(arg):
        if arg not in wrapper.log:
            wrapper.log[arg] = func(arg)
        return wrapper.log[arg]

    wrapper.log = {}
    return wrapper
