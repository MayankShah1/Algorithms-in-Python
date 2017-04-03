from collections import deque

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class DequeQueue:
    """FIFO Queue implementation using collections.deque as underlying storage"""

    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[0]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data.popleft()

    def enqueue(self,element):
        self._data.append(element)