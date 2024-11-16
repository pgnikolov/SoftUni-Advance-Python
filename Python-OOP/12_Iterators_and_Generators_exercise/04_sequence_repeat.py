class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration

        self.number -= 1
        self.current_index += 1
        if self.current_index > len(self.sequence) - 1:
            self.current_index = 0
        return self.sequence[self.current_index]
