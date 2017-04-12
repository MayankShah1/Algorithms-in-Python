class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class LinkedQueue:
    """FIFO Queue implementation using a singly linked list for storage"""

    # --------------- nested _Node class -----------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next


    # -------------------- queue methods ------------------

    def __init__(self):
        """Create an empty queue."""

        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the size of queue."""
        return self._size

    def is_empty(self):
        """Return True if queue is empty."""
        return self._size == 0

    def first(self):
        """Return the first element of the queue.

        Raise Empty exception if stack is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def enqueue(self,e):
        """Add an element at the back of the queue"""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        """ Return and remove the element at the front of the queue.

        Raise empty exception if queue is empty. 
        """
        if self.is_empty():
            raise Empty('Queue is empty.')
        answer = self._head._element
        self._head = self._head._next
        if self.is_empty():
            self._tail = None
        return answer

    def concatenate(self, other):
        """Concatenates the other queue"""
        self._tail._next = other._head
        self._tail = other._tail
        self._size += other._size
        other._size = 0
        other._head = None

    def __str__(self):
        elements = []
        walk = self._head
        while walk is not None:
            elements.append(str(walk._element) + ' ')
            walk = walk._next
        return ''.join(elements)

# Testing
if __name__ == "__main__":
    queue = LinkedQueue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)
    queue.enqueue(40)
    print(queue)
    queue.dequeue()
    print(queue)

    queue_two = LinkedQueue()
    queue_two.enqueue(50)
    queue_two.enqueue(60)
    print(queue_two)

    queue.concatenate(queue_two)
    print(queue)
    print(queue_two)

