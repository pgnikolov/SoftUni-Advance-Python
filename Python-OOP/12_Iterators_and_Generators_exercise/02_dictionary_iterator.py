class dictionary_iter:
    def __init__(self, rand_dict):
        self.rand_dict = list(rand_dict.items())
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.rand_dict:
            raise StopIteration
        self.counter += 1
        return self.rand_dict.pop(0)
