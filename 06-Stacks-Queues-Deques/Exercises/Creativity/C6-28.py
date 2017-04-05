class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class Full(Exception):
    """Error attempting to insert an element to a full container"""
    pass


class ArrayQueue:
    """FIFO Queue implementation using Python list as underlying storage."""

    DEFAULT_CAPACITY = 10

    def __init__(self, maxlen = None):
        """Create an empty queue."""

        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._maxlen = maxlen

    def __len__(self):
        """Return the number of elements in queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return the element at the front of the queue.

        Raise an exception if queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue.

        Raise Empty exception is queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to back of queue."""
        if self._maxlen is not None and self._size == self._maxlen:
            raise Full('Capacity exceeded.!')

        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._size + self._front) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0