from functools import wraps


def make_bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"

    return wrapper


def make_italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"

    return wrapper


def make_underline(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"

    return wrapper
