def operate(operator, *args):
    result = args[0]
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        for x in args[1:]:
            result -= x
    elif operator == "/":
        for x in args[1:]:
            result /= x
    elif operator == "*":
        for x in args[1:]:
            result *= x
    return result
