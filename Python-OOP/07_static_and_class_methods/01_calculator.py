class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for el in args:
            result *= el
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for el in args[1:]:
            result /= el
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for el in args[1:]:
            result -= el
        return result
