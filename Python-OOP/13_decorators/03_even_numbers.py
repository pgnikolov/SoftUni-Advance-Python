def even_numbers(function):
    def wrapper(numbers):
        res = function(numbers)
        filtered_numbers = [n for n in numbers if n % 2 == 0]
        return filtered_numbers

    return wrapper
