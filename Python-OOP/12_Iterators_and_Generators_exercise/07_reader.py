def read_next(*args):
    for item in args:
        for symb in item:
            yield str(symb)
