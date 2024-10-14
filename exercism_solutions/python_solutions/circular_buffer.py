class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.circular_buffer = [None] * capacity
        self.empty_slots = capacity

    def read(self):
        if self.empty_slots == self.capacity:
            raise BufferEmptyException("Circular buffer is empty")
        self.circular_buffer.append(None)
        self.empty_slots += 1
        return self.circular_buffer.pop(0)

    def write(self, data):
        if self.empty_slots == 0:
            raise BufferFullException("Circular buffer is full")
        self.circular_buffer[self.capacity - self.empty_slots] = data
        self.empty_slots -= 1

    def overwrite(self, data):
        if self.empty_slots == 0:
            self.circular_buffer.append(data)
            self.circular_buffer.pop(0)
        else:
            self.write(data)

    def clear(self):
        self.empty_slots = self.capacity