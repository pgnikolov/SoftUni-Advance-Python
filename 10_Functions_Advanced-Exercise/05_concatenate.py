def concatenate(*args, **kwargs):
    string_ = "".join(args)
    for key, value in kwargs.items():
        if key in kwargs:
            string_ = string_.replace(key, value)
    return string_
