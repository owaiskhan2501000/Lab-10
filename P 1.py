class UniqueIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.seen = set()  # Set to keep track of unique elements
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.iterable):
            current_element = self.iterable[self.index]
            self.index += 1
            if current_element not in self.seen:
                self.seen.add(current_element)
                return current_element
        raise StopIteration

my_list = [1, 2, 3, 1, 4, 2, 5, 6, 3, 7]

unique_iterator = UniqueIterator(my_list)

for unique_element in unique_iterator:
    print(unique_element)
