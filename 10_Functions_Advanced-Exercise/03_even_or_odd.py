def even_odd(*args):
    if args[-1] == "even":
        return [x for x in args[:len(args) - 1] if x % 2 == 0]
    else:
        return [x for x in args[:len(args) - 1] if x % 2 != 0]
    