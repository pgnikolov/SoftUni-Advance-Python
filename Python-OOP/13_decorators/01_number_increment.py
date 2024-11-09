def number_increment(numbers):
    def increase():
        increased = [el + 1 for el in numbers]
        return increased
    return increase()
