def get_primes(numbers_list):
    for numb in numbers_list:
        if numb <= 1:
            continue
        for n in range(2, numb):
            if numb % n == 0:
                break
        else:
            yield numb
