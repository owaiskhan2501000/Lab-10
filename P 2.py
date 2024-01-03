class ChunkIterator:
    def __init__(self, iterable, chunk_size):
        self.iterable = iterable
        self.chunk_size = chunk_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            current_chunk = self.iterable[self.index:self.index + self.chunk_size]
            self.index += self.chunk_size
            return current_chunk
        raise StopIteration

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

chunk_iterator = ChunkIterator(numbers_list, 3)

for chunk in chunk_iterator:
    print(chunk)
