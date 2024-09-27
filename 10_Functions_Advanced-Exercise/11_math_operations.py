def math_operations(*args, **kwargs):
    nums = list(args)
    counter = 0
    while True:
        counter += 1
        if nums:
            new_number = nums.pop(0)
        else:
            break

        if counter == 1:
            kwargs['a'] += new_number
        elif counter == 2:
            kwargs['s'] -= new_number
        elif counter == 3:
            if new_number > 0:
                kwargs['d'] /= new_number
        elif counter == 4:
            kwargs['m'] *= new_number
        if not nums:
            break
        if counter == 4:
            counter = 0
    return '\n'.join([f'{key}: {value:.1f}' for key, value in sorted(kwargs.items(), key=lambda k: (-k[1], k[0]))])
