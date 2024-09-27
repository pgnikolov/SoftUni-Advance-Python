def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


def func_executor(*args):
    result = ""
    for func_name, func_arg in args:
        result += f"{func_name.__name__} - {func_name(*func_arg)}\n"
    return result
