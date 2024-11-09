from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"you called {func.__name__}{args}\nit returned {func(*args, **kwargs)}"

    return wrapper
