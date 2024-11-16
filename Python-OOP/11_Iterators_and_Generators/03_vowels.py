class vowels:
    def __init__(self, string: str):
        self.string = string
        self.start_index = 0
        self.end_index = len(string)
        self.vowels = ('a', 'e', 'i', 'o', 'u')

    def __iter__(self):
        return self

    def __next__(self):
        while self.start_index < self.end_index:
            output = self.string[self.start_index]
            self.start_index += 1

            if output.lower() in self.vowels:
                return output
        else:
            raise StopIteration()
