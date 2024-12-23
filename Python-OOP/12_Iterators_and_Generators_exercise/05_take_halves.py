def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        counter = 0
        result = []
        for halve in halves():
            if counter == n:
                return result
            result.append(halve)
            counter += 1

    return (take, halves, integers)

