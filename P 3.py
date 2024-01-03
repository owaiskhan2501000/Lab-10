class ReverseIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            current_element = self.sequence[self.index]
            self.index -= 1
            return current_element
        raise StopIteration

strings_list = ["apple", "banana", "cherry", "date", "elderberry"]

reverse_iterator = ReverseIterator(strings_list)

for element in reverse_iterator:
    print(element)
