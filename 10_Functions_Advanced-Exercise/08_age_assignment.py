def age_assignment(*args, **kwargs):
    result = []
    kwargs = sorted(kwargs.items())
    for key, value in kwargs:
        for name in args:
            if name.startswith(key):
                result_name = name
                age = value
                result.append(f"{result_name} is {age} years old.")

    return '\n'.join(result)
